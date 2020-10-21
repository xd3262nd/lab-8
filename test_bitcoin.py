import unittest
from unittest import TestCase
from unittest.mock import patch

import bitcoin


class TestBitCoin(TestCase):

    # Mock the API response data function
    @patch('bitcoin.get_current_exchange_rate')
    def test_get_bitcoin_exchange_rate(self, mock_data):
        mock_rate = 1000
        example_json_response = {
            "time": {"updated": "Oct 13, 2020 16:40:00 UTC", "updatedISO": "2020-10-13T16:40:00+00:00",
                     "updateduk": "Oct 13, 2020 at 17:40 BST"},
            "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
            "chartName": "Bitcoin", "bpi": {
                "USD": {"code": "USD", "symbol": "&#36;", "rate": "11,382.7917", "description": "United States Dollar",
                        "rate_float": mock_rate}, "GBP": {"code": "GBP", "symbol": "&pound;", "rate": "8,776.5991",
                                                          "description": "British Pound Sterling",
                                                          "rate_float": 8776.5991},
                "EUR": {"code": "EUR", "symbol": "&euro;", "rate": "9,697.7856", "description": "Euro",
                        "rate_float": 9697.7856}}}
        mock_data.side_effect = [example_json_response]
        converted_num = bitcoin.get_conversion_to_dollars(100)
        self.assertEqual(100000.00, converted_num)

    # Mock user input
    @patch('builtins.input', side_effect=['string input', 'zebra', 'rainbow', '  ', '999'])
    def test_user_input_validation(self, mock_input):
        bitcoin_num = bitcoin.get_user_bitcoin_value()
        self.assertEqual(999, bitcoin_num)

    # Mock display function
    @patch('builtins.print')
    def test_display_conversion(self, mock_print):
        example_bitcoin_num = 10
        example_conversion_val = 10000

        expected_print = f'With your {example_bitcoin_num:.2f} of bitcoin, you will be able to get {example_conversion_val}USD.'
        bitcoin.display(example_bitcoin_num, example_conversion_val)
        mock_print.assert_called_with(expected_print)
