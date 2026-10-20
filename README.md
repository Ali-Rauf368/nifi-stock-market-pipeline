# Stock Market Data Pipeline using Apache NiFi

## Overview

A stock market data engineering project focused on JSON data ingestion, validation, transformation, and structured output. The repository includes sample datasets, pipeline design documentation, Python validation logic, unit tests, and automated testing with GitHub Actions.

## Technologies

- Apache NiFi
- Python
- JSON
- Git and GitHub
- GitHub Actions

## Architecture

1. Read stock records from JSON.
2. Split the stock collection into individual records.
3. Extract relevant stock fields.
4. Prepare structured JSON output.
5. Validate data quality.
6. Run automated Python tests.

## Repository Contents

- `sample_stock_data.json` — sample input records.
- `sample_output.json` — example processed record.
- `nifi_stock_pipeline.json` — pipeline specification.
- `pipeline_design.md` — pipeline design.
- `architecture.md` — architecture overview.
- `data_quality_rules.md` — data validation rules.
- `validate_stock_data.py` — Python validation script.
- `test_validate_stock_data.py` — unit tests.
- `RUNNING.md` — execution instructions.
- `.github/workflows/python-tests.yml` — automated test workflow.

## Running the Validator

Python 3.9 or later is recommended.

```bash
python validate_stock_data.py
```

Run the unit tests with:

```bash
python -m unittest discover -v
```

## Project Status

The sample data, Python validation, and automated testing workflow are included in the repository. The Apache NiFi flow design is documented; the actual NiFi flow still needs to be implemented and verified.

## Data Disclaimer

The included stock prices are illustrative sample values and do not represent verified live market data.

