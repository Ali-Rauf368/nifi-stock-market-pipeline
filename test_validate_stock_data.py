
import unittest

from validate_stock_data import validate_stock


class TestValidateStock(unittest.TestCase):

    def setUp(self):
        self.valid_record = {
            "symbol": "AAPL",
            "company": "Apple Inc.",
            "price": 225.50,
            "currency": "USD",
            "timestamp": "2026-10-20T14:30:00Z"
        }

    def test_valid_record(self):
        self.assertEqual(validate_stock(self.valid_record), [])

    def test_missing_symbol(self):
        record = self.valid_record.copy()
        del record["symbol"]

        errors = validate_stock(record)

        self.assertTrue(
            any("Missing required field: symbol" in error for error in errors)
        )

    def test_negative_price(self):
        record = self.valid_record.copy()
        record["price"] = -10

        errors = validate_stock(record)

        self.assertIn("Price must not be negative", errors)

    def test_non_numeric_price(self):
        record = self.valid_record.copy()
        record["price"] = "unknown"

        errors = validate_stock(record)

        self.assertIn("Price must be numeric", errors)

    def test_invalid_timestamp(self):
        record = self.valid_record.copy()
        record["timestamp"] = "not-a-date"

        errors = validate_stock(record)

        self.assertIn(
            "Timestamp must be a valid ISO 8601 date-time",
            errors
        )


if __name__ == "__main__":
    unittest.main()
