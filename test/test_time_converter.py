import sys
import unittest

sys.path.append("..")
from src.time_converter import convert_timestamp

class TestConvertTimestamp(unittest.TestCase):
    def test_it_should_convert_timestamp_in_milliseconds(self):
        # Given
        timestamp_in_millis = 1675416802951
        expected_output = '2023-02-03T09:33:22Z'
        
        # Then
        self.assertEqual(convert_timestamp(timestamp_in_millis), expected_output)
    
    def test_it_should_convert_timestamp_in_seconds(self):
        # Given
        timestamp_in_seconds = 1675416802
        expected_output = '2023-02-03T09:33:22Z'
        
        # Then
        self.assertEqual(convert_timestamp(timestamp_in_seconds), expected_output)
        
    def test_it_should_be_able_to_handle_zero_timestamp(self):
        # Given
        timestamp = 0
        expected_output = '1970-01-01T00:00:00Z'
        
        # Then
        self.assertEqual(convert_timestamp(timestamp), expected_output)

if __name__ == '__main__':
    unittest.main()
