# Stock Market Data Pipeline using Apache NiFi

## About the Project

This project uses Apache NiFi to collect stock market data, process JSON responses, and save the results in a structured format.

The goal is to build a simple data flow that demonstrates how data can be fetched from an API, transformed, and prepared for further analysis.

## Tools Used

- Apache NiFi
- REST API
- JSON
- GitHub

## Pipeline Flow

1. Fetch stock market data from an API.
2. Extract the required fields from the JSON response.
3. Transform the data into a structured format.
4. Save the processed data to a file.

## Project Structure

```text
nifi-stock-market-pipeline/
├── README.md
├── nifi_stock_pipeline.json
└── sample_stock_data.json
```

## Current Status

The project is being developed. The NiFi flow and sample data will be added as the implementation progresses.

## Future Improvements

- Connect a live stock market API.
- Add data validation.
- Store processed data in a database.
- Handle API errors and missing values.
