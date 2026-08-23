import fs from 'node:fs';

function assertFinite(value, label) {
  if (!Number.isFinite(value)) {
    throw new Error(`${label} must be finite`);
  }
}

export function validatePayload(payload) {
  if (payload.kernel_version !== 'PRK-1.0') {
    throw new Error('kernel_version must equal PRK-1.0');
  }

  const n = payload.x.length;
  const m = payload.u.length;

  if (n === 0 || m === 0) {
    throw new Error('non-empty state and control vectors are required');
  }

  assertFinite(payload.dt, 'dt');
  if (payload.dt <= 0) {
    throw new Error('dt must be strictly positive');
  }

  if (
    payload.r.length !== n ||
    payload.h.length !== n ||
    payload.weights.length !== n ||
    payload.D.length !== n ||
    payload.A.length !== n ||
    payload.B.length !== n
  ) {
    throw new Error('dimension mismatch');
  }

  let weightSum = 0;
  for (let i = 0; i < n; i += 1) {
    if (payload.D[i].length !== n || payload.A[i].length !== n || payload.B[i].length !== m) {
      throw new Error(`matrix shape mismatch at row ${i}`);
    }
    assertFinite(payload.x[i], `x[${i}]`);
    assertFinite(payload.r[i], `r[${i}]`);
    assertFinite(payload.h[i], `h[${i}]`);
    assertFinite(payload.weights[i], `weights[${i}]`);

    if (payload.x[i] < 0 || payload.x[i] > 1) {
      throw new Error('input state x must lie in [0,1]^n');
    }
    if (payload.r[i] < 0) {
      throw new Error('recovery vector r must be componentwise non-negative');
    }
    if (payload.weights[i] < 0) {
      throw new Error('weights must be componentwise non-negative');
    }
    weightSum += payload.weights[i];

    for (let j = 0; j < n; j += 1) {
      assertFinite(payload.D[i][j], `D[${i}][${j}]`);
      assertFinite(payload.A[i][j], `A[${i}][${j}]`);
    }
    for (let q = 0; q < m; q += 1) {
      assertFinite(payload.B[i][q], `B[${i}][${q}]`);
    }
  }

  for (let q = 0; q < m; q += 1) {
    assertFinite(payload.u[q], `u[${q}]`);
  }

  if (Math.abs(weightSum - 1) > 1e-12) {
    throw new Error('weights must sum to one within 1e-12');
  }
}

export function step(payload) {
  validatePayload(payload);

  const n = payload.x.length;
  const phi = payload.x.map(Math.tanh);
  const dx = new Array(n);
  const xNext = new Array(n);

  let weightedServiceNext = 0;

  for (let i = 0; i < n; i += 1) {
    let degradation = 0;
    let coupling = 0;
    let controlEffect = 0;

    for (let j = 0; j < n; j += 1) {
      degradation += payload.D[i][j] * payload.x[j];
      coupling += payload.A[i][j] * phi[j];
    }
    for (let q = 0; q < payload.u.length; q += 1) {
      controlEffect += payload.B[i][q] * payload.u[q];
    }

    dx[i] =
      -degradation +
      coupling +
      payload.r[i] * (1 - payload.x[i]) -
      payload.h[i] +
      controlEffect;

    const proposal = payload.x[i] + payload.dt * dx[i];
    xNext[i] = Math.max(0, Math.min(1, proposal));
    weightedServiceNext += payload.weights[i] * xNext[i];
  }

  return {
    kernel_version: payload.kernel_version,
    fixture_id: payload.fixture_id,
    dx,
    x_next: xNext,
    weighted_service_next: weightedServiceNext,
  };
}

if (process.argv[1]?.endsWith('kernel.mjs')) {
  if (process.argv.length !== 3) {
    throw new Error('usage: node kernel.mjs <fixture.json>');
  }
  const payload = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  process.stdout.write(`${JSON.stringify(step(payload))}\n`);
}
