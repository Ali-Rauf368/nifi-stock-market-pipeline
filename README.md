# Stock Market Data Pipeline using Apache NiFi

## Overview

This project demonstrates a data pipeline designed to process stock market data using Apache NiFi. It focuses on JSON ingestion, record transformation, and structured output for downstream analysis.

## Architecture

The pipeline follows a simple data processing workflow:

1. **Data Ingestion** – Read stock market data from a JSON source.
2. **Record Splitting** – Separate multiple stock records into individual entries.
3. **Field Extraction** – Extract relevant fields such as stock symbol, company name, price, and timestamp.
4. **Data Transformation** – Prepare records in a consistent JSON format.
5. **Output** – Produce structured stock records for further processing or storage.

## Technology Stack

- Apache NiFi
- JSON
- REST API integration
- Git and GitHub

## Repository Structure

```text
nifi-stock-market-pipeline/
├── README.md
├── pipeline_design.md
├── nifi_stock_pipeline.json
├── sample_stock_data.json
└── sample_output.json
```

## Data Format

The pipeline uses JSON input containing stock records and produces structured JSON output. The sample files illustrate the expected input and output formats.

## Potential Extensions

- Integrate a live stock market data API.
- Add data validation and error handling.
- Store processed records in a database.
- Schedule recurring data ingestion.
- Add monitoring and logging.

## Notes

Sample stock values are illustrative and should not be interpreted as live market prices.
