# Build Ecosystem — Usage Guide

Build Ecosystem installs the full Build family in one command. It has no CLI
and no API of its own beyond a version string.

## Install

```bash
# Everything, core dependencies only
pip install build-ecosystem

# Everything, including each member's GUI extra
pip install "build-ecosystem[gui]"

# Everything, including each member's full optional extras
pip install "build-ecosystem[all]"
```

Requires Python 3.10+.

## What gets installed

- `build-color` — color-science library
- `build-finance` — algorithmic trading toolkit
- `build-oracle` — time-series forecasting and anomaly detection
- `build-engine` — self-improving prediction and trading engine
- `calibrate-pro` — professional display calibration
- `build-ui` — shared PyQt6 theme/widget layer (via the `gui`/`all` extras)

## Usage

Import each member package directly — `build_ecosystem` does not re-export
their APIs:

```python
import build_color
import build_finance
import build_oracle
import build_engine
import calibrate_pro

print(build_color.__version__)
```

See each member's own README and USAGE.md for its CLI and Python API.

## See also

- `README.md` — project overview.
- `ARCHITECTURE.md` — the umbrella structure and version-pinning contract.
