
import json
from datetime import datetime
from pathlib import Path

INPUT_FILE = Path(__file__).parent / "sample_stock_data.json"

REQUIRED_FIELDS = ["symbol", "company", "price", "currency", "timestamp"]


def validate_stock(record):
    errors = []

    for field in REQUIRED_FIELDS:
        if field not in record or record[field] in (None, ""):
            errors.append(f"Missing required field: {field}")

    price = record.get("price")
    if price is not None:
        if isinstance(price, bool) or not isinstance(price, (int, float)):
            errors.append("Price must be numeric")
        elif price < 0:
            errors.append("Price must not be negative")

    timestamp = record.get("timestamp")
    if timestamp:
        try:
            datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        except (ValueError, AttributeError):
            errors.append("Timestamp must be a valid ISO 8601 date-time")

    return errors


def main():
    with INPUT_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    stocks = data.get("stocks")
    if not isinstance(stocks, list):
        raise ValueError("Input JSON must contain a 'stocks' list")

    seen = set()
    valid_count = 0
    invalid_count = 0

    for index, stock in enumerate(stocks, start=1):
        if not isinstance(stock, dict):
            print(f"Record {index}: INVALID - expected a JSON object")
            invalid_count += 1
            continue

        errors = validate_stock(stock)
        symbol = stock.get("symbol")
        timestamp = stock.get("timestamp")

        if symbol and timestamp:
            key = (symbol, timestamp)
            if key in seen:
                errors.append("Duplicate stock symbol and timestamp")
            else:
                seen.add(key)

        if errors:
            invalid_count += 1
            print(f"Record {index}: INVALID")
            for error in errors:
                print(f"  - {error}")
        else:
            valid_count += 1
            print(f"Record {index}: VALID ({symbol})")

    print("\nValidation Summary")
    print(f"Valid records: {valid_count}")
    print(f"Invalid records: {invalid_count}")


if __name__ == "__main__":
    main()
