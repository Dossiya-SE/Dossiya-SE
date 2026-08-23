-- PRK-1.0 evidence-storage adapter.
-- SQL is intentionally not presented as an independent numerical solver.

CREATE TABLE IF NOT EXISTS resilience_run (
    run_id TEXT PRIMARY KEY,
    kernel_version TEXT NOT NULL,
    implementation_id TEXT NOT NULL,
    fixture_id TEXT,
    git_commit TEXT,
    runtime_version TEXT,
    platform TEXT,
    input_sha256 TEXT NOT NULL,
    output_sha256 TEXT NOT NULL,
    created_at_utc TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS resilience_state (
    run_id TEXT NOT NULL,
    step_index INTEGER NOT NULL,
    state_index INTEGER NOT NULL,
    x_value REAL NOT NULL CHECK (x_value >= 0.0 AND x_value <= 1.0),
    PRIMARY KEY (run_id, step_index, state_index),
    FOREIGN KEY (run_id) REFERENCES resilience_run(run_id)
);

CREATE TABLE IF NOT EXISTS conformance_result (
    run_id TEXT NOT NULL,
    implementation_id TEXT NOT NULL,
    fixture_id TEXT NOT NULL,
    max_abs_error_dx REAL NOT NULL,
    max_abs_error_x_next REAL NOT NULL,
    weighted_service_error REAL NOT NULL,
    tolerance REAL NOT NULL,
    passed INTEGER NOT NULL CHECK (passed IN (0, 1)),
    FOREIGN KEY (run_id) REFERENCES resilience_run(run_id)
);
