#### Extract from a file, data transformation, and load to Postgres using Pentaho DI with a simple notification via Telegram using Python.

- staging.ktr - extract;
- staging->dw.ktr - data transformation;
- abort.py, success.py - sends notification
- etl_job.kjb - orchestrating job