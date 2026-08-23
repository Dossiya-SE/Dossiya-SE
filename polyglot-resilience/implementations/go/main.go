package main

import (
    "encoding/json"
    "fmt"
    "math"
    "os"
)

type Payload struct {
    KernelVersion string      `json:"kernel_version"`
    FixtureID     string      `json:"fixture_id"`
    Dt            float64     `json:"dt"`
    X             []float64   `json:"x"`
    D             [][]float64 `json:"D"`
    A             [][]float64 `json:"A"`
    R             []float64   `json:"r"`
    H             []float64   `json:"h"`
    B             [][]float64 `json:"B"`
    U             []float64   `json:"u"`
    Weights       []float64   `json:"weights"`
}

type Output struct {
    KernelVersion       string    `json:"kernel_version"`
    FixtureID           string    `json:"fixture_id"`
    Dx                  []float64 `json:"dx"`
    XNext               []float64 `json:"x_next"`
    WeightedServiceNext float64   `json:"weighted_service_next"`
}

func validate(p Payload) error {
    if p.KernelVersion != "PRK-1.0" {
        return fmt.Errorf("kernel_version must equal PRK-1.0")
    }

    n := len(p.X)
    m := len(p.U)
    if n == 0 || m == 0 {
        return fmt.Errorf("non-empty state and control vectors are required")
    }
    if !math.IsNaN(p.Dt) && !math.IsInf(p.Dt, 0) && p.Dt <= 0 {
        return fmt.Errorf("dt must be strictly positive")
    }
    if math.IsNaN(p.Dt) || math.IsInf(p.Dt, 0) {
        return fmt.Errorf("dt must be finite")
    }

    if len(p.R) != n || len(p.H) != n || len(p.Weights) != n {
        return fmt.Errorf("x, r, h and weights must have the same length n")
    }
    if len(p.D) != n || len(p.A) != n || len(p.B) != n {
        return fmt.Errorf("matrix row-count mismatch")
    }

    weightSum := 0.0
    for i := 0; i < n; i++ {
        if len(p.D[i]) != n || len(p.A[i]) != n || len(p.B[i]) != m {
            return fmt.Errorf("matrix shape mismatch at row %d", i)
        }
        if p.X[i] < 0 || p.X[i] > 1 || math.IsNaN(p.X[i]) || math.IsInf(p.X[i], 0) {
            return fmt.Errorf("input state must lie in [0,1]^n and be finite")
        }
        if p.R[i] < 0 || math.IsNaN(p.R[i]) || math.IsInf(p.R[i], 0) {
            return fmt.Errorf("recovery vector must be finite and non-negative")
        }
        if p.Weights[i] < 0 || math.IsNaN(p.Weights[i]) || math.IsInf(p.Weights[i], 0) {
            return fmt.Errorf("weights must be finite and non-negative")
        }
        weightSum += p.Weights[i]

        for j := 0; j < n; j++ {
            values := []float64{p.D[i][j], p.A[i][j]}
            for _, value := range values {
                if math.IsNaN(value) || math.IsInf(value, 0) {
                    return fmt.Errorf("D and A must contain finite values")
                }
            }
        }
        for q := 0; q < m; q++ {
            if math.IsNaN(p.B[i][q]) || math.IsInf(p.B[i][q], 0) {
                return fmt.Errorf("B must contain finite values")
            }
        }
        if math.IsNaN(p.H[i]) || math.IsInf(p.H[i], 0) {
            return fmt.Errorf("h must contain finite values")
        }
    }

    for _, value := range p.U {
        if math.IsNaN(value) || math.IsInf(value, 0) {
            return fmt.Errorf("u must contain finite values")
        }
    }

    if math.Abs(weightSum-1.0) > 1e-12 {
        return fmt.Errorf("weights must sum to one within 1e-12")
    }
    return nil
}

func step(p Payload) (Output, error) {
    if err := validate(p); err != nil {
        return Output{}, err
    }

    n := len(p.X)
    phi := make([]float64, n)
    dx := make([]float64, n)
    xNext := make([]float64, n)

    for i, value := range p.X {
        phi[i] = math.Tanh(value)
    }

    weightedService := 0.0
    for i := 0; i < n; i++ {
        degradation := 0.0
        coupling := 0.0
        controlEffect := 0.0

        for j := 0; j < n; j++ {
            degradation += p.D[i][j] * p.X[j]
            coupling += p.A[i][j] * phi[j]
        }
        for q := 0; q < len(p.U); q++ {
            controlEffect += p.B[i][q] * p.U[q]
        }

        dx[i] = -degradation + coupling + p.R[i]*(1.0-p.X[i]) - p.H[i] + controlEffect
        proposal := p.X[i] + p.Dt*dx[i]
        if proposal < 0 {
            proposal = 0
        }
        if proposal > 1 {
            proposal = 1
        }
        xNext[i] = proposal
        weightedService += p.Weights[i] * proposal
    }

    return Output{
        KernelVersion:       p.KernelVersion,
        FixtureID:           p.FixtureID,
        Dx:                  dx,
        XNext:               xNext,
        WeightedServiceNext: weightedService,
    }, nil
}

func main() {
    if len(os.Args) != 2 {
        panic("usage: go run main.go <fixture.json>")
    }

    raw, err := os.ReadFile(os.Args[1])
    if err != nil {
        panic(err)
    }

    var payload Payload
    if err := json.Unmarshal(raw, &payload); err != nil {
        panic(err)
    }

    output, err := step(payload)
    if err != nil {
        panic(err)
    }

    encoder := json.NewEncoder(os.Stdout)
    encoder.SetEscapeHTML(false)
    if err := encoder.Encode(output); err != nil {
        panic(err)
    }
}
