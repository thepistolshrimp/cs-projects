# SEIR Disease Model — Python

A numerical modelling project for epidemic dynamics using an extended SEIR-type compartment model.

The project models susceptible, exposed, infected, asymptomatic, and recovered populations. It also explores time-dependent transmission rates, a lockdown scenario, and imported infections.

## Files

- `SEIRO.py` — base epidemic model and numerical simulation.
- `SEIR.py` — extension supporting constant or time-dependent transmission rates.
- `outbreak.py` — outbreak scenario with a change in transmission rate.
- `lockdown.py` — reads time-dependent beta values and applies them to the model.
- `covid19.py` — extends the model with imported infections.

## Requirements

```bash
pip install -r requirements.txt
```

## Additional files required

The supplied source code imports `ODESolver.py` and `lockdown.py` expects `beta_values.txt`. `ODESolver.py` and `beta_values.txt` were not among the files provided for this repository, so the complete project will not run until those files are added.
