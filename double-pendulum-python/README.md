# Double Pendulum — Numerical Simulation

A MEK4100 midterm project studying the dynamics of a double pendulum.

The project compares a linear small-angle approximation with numerical simulation and explores nonlinear behaviour for different initial conditions. The report derives normal-mode frequencies and compares analytical and numerical solutions before moving to the general nonlinear equations.

## Files

- `small_angle_comparison.py` — Euler-Cromer simulation compared with the analytical small-angle solution.
- `nonlinear_double_pendulum.py` — nonlinear double-pendulum simulation for several initial conditions.
- `docs/MEK4100-midterm-project.pdf` — project report.

The Python files were reconstructed from the code included in the supplied report so that the project can be browsed directly on GitHub.

## Requirements

```bash
pip install -r requirements.txt
```

## Run

```bash
python small_angle_comparison.py
python nonlinear_double_pendulum.py
```
