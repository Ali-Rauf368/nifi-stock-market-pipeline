# Pipeline Design

## Overview

This project demonstrates a simple stock market data pipeline using Apache NiFi. The pipeline is designed to process JSON data and prepare individual stock records for further analysis.

## Data Flow

1. **Get Data** – Start with sample stock market data in JSON format.
2. **Split Records** – Separate the stock array into individual stock records.
3. **Extract Fields** – Extract the stock symbol, company name, price, and timestamp.
4. **Prepare Output** – Format each record as structured JSON.
5. **Log Results** – Log the processed records for basic verification.

## Sample Files

- `sample_stock_data.json` contains example input data.
- `sample_output.json` shows the expected format of a processed stock record.
- `nifi_stock_pipeline.json` documents the planned processor sequence.

## Current Status

The project structure and sample data are available on GitHub. The actual Apache NiFi flow has not yet been created or exported.

The stock values used in the sample files are illustrative and do not represent verified market prices.

## Future Improvements

- Implement the flow in Apache NiFi.
- Connect to a stock market API.
- Add data validation and error handling.
- Save processed records to a database or file.
