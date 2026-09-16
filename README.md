# quillon

A small library for ingesting and normalising batch data files.

## Install

```bash
pip install quillon
```

## Usage

```python
from quillon import Pipeline
Pipeline.from_config("quillon.toml").run()
```

See `docs/architecture.md` for design notes.

## Licence

MIT.
