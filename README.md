# obdGateway

A small OBD-II telemetry gateway: reads live vehicle data (RPM, speed, coolant temp) and uploads it
to a configurable HTTP endpoint on an interval.

Two data sources, selected by config:
- **`SIMULATION`** — generates plausible random telemetry, no hardware needed.
- **`REAL`** — reads from an actual OBD-II adapter via [`python-obd`](https://github.com/brendan-w/python-OBD).

## Structure

```
src/
├── main.py           # entrypoint: loads config, picks data source, upload loop
├── config_loader.py  # reads config/settings.json
├── data_source.py     # SimulationDataSource / RealOBDDataSource
└── uploader.py        # posts telemetry to server_url
config/
└── settings.json      # mode, upload_interval_seconds, obd_port, server_url, vehicle_id
```

## Running

```bash
python src/main.py
```

Configure `config/settings.json` first — set `"mode"` to `"SIMULATION"` or `"REAL"` (the latter
needs `obd_port` pointing at a real ELM327-compatible adapter).
