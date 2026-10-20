# Stock Market Pipeline Architecture

## Overview

The project is organized around stock data ingestion, transformation, validation, and structured output.

## Data Flow

```text
Sample Stock JSON
       |
       v
Apache NiFi Pipeline Design
       |
       v
Split and Extract Stock Records
       |
       v
Prepare Structured JSON Output
       |
       v
Stock Data Output
```

## Validation and Testing

The Python validation script checks required fields, price values, timestamps, and duplicate stock records.

Unit tests cover the core validation function. GitHub Actions runs the Python test suite automatically on pushes to the main branch and pull requests targeting main.

## Project Components

- **Input:** Sample stock data in JSON format.
- **Pipeline design:** Documents the intended Apache NiFi processor sequence.
- **Validation:** Python-based data quality checks.
- **Testing:** Unit tests and GitHub Actions.
- **Output:** Example of the expected structured stock record.

The NiFi pipeline design describes the intended architecture; its processor configuration and execution need to be implemented and verified separately.
