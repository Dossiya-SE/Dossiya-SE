"""Generate deterministic mathematical art for the GitHub profile.

The script creates a state-space visualization of a four-sector coupled
infrastructure system. It intentionally uses only NumPy and Matplotlib.
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


OUT = Path(__file__).resolve().parents[1] / "assets" / "resilience-phase-space.png"


def simulate(steps: int = 900, dt: float = 0.015) -> np.ndarray:
    """Simulate a bounded nonlinear coupled-service model."""
    A = np.array([
        [0.00, 0.22, 0.08, 0.06],
        [0.18, 0.00, 0.05, 0.11],
        [0.09, 0.06, 0.00, 0.04],
        [0.12, 0.17, 0.03, 0.00],
    ])
    d = np.array([0.36, 0.32, 0.29, 0.34])
    r = np.array([0.24, 0.21, 0.18, 0.22])
    x = np.array([0.92, 0.88, 0.95, 0.84], dtype=float)
    history = np.empty((steps, 4), dtype=float)

    for k in range(steps):
        t = k * dt
        hazard = 0.28 * np.exp(-((t - 3.2) / 0.75) ** 2) * np.array([1.0, 0.82, 0.55, 0.92])
        control = 0.12 * np.exp(-((t - 5.1) / 1.15) ** 2) * np.array([0.92, 1.0, 0.62, 0.85])
        dx = -d * x + A @ np.tanh(2.2 * x - 0.9) + r * (1.0 - x) - hazard + control
        x = np.clip(x + dt * dx, 0.0, 1.0)
        history[k] = x

    return history


def main() -> None:
    state = simulate()
    t = np.arange(len(state))

    fig, ax = plt.subplots(figsize=(14, 6), dpi=180)
    for i, label in enumerate(["Power", "Water", "Transport", "Solid waste"]):
        ax.plot(t, state[:, i], linewidth=1.8, label=label)

    service = state.mean(axis=1)
    ax.plot(t, service, linewidth=3.0, label="Mean critical service")
    ax.axhline(0.70, linestyle="--", linewidth=1.2, label="Illustrative viability threshold")
    ax.set_xlabel("Simulation step")
    ax.set_ylabel("Normalized service state")
    ax.set_ylim(0, 1.02)
    ax.set_title("Coupled Infrastructure Disturbance and Recovery Geometry")
    ax.legend(ncol=3, frameon=False)
    fig.tight_layout()

    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT, bbox_inches="tight")
    plt.close(fig)
    print(OUT)


if __name__ == "__main__":
    main()
