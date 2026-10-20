# Data Quality Rules

## Purpose

These rules define basic validation checks for stock market records before they are processed by the pipeline.

## Required Fields

Each stock record should contain the following fields:

| Field | Data Type | Validation Rule |
|---|---|---|
| symbol | String | Must not be empty |
| company | String | Must not be empty |
| price | Number | Must be greater than or equal to zero |
| timestamp | String | Must use a valid date-time format |
| currency | String | Must not be empty |

## Validation Checks

### 1. Missing Values

Records with missing required fields should be identified for review.

### 2. Price Validation

The stock price must be numeric and non-negative.

### 3. Timestamp Validation

The timestamp should follow ISO 8601 format, including a timezone where available.

Example: `2026-10-20T14:30:00Z`

### 4. Duplicate Records

Records with the same stock symbol and timestamp should be checked for duplicates.

### 5. Invalid Records

Invalid records should be separated from valid records so they can be investigated without interrupting the entire processing workflow.

## Future Implementation

These rules describe the intended validation logic. They can later be implemented using Apache NiFi processors and tested against sample input data.
