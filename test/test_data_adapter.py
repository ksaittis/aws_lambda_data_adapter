from typing import Dict
import unittest
import unittest.mock
import sys
sys.path.append("..")
from src.data_adapter import get_key_mappings, transform_data


class TestDataTransformer(unittest.TestCase):

    def test_it_should_be_able_to_get_key_mappings_from_env_vars(self):
        # Given
        expected_mappings = {"userid": "user_id"}

        # When
        with unittest.mock.patch.dict('os.environ', {'KEY_MAPPINGS': '{"userid":"user_id"}'}):
            actual_mappings = get_key_mappings()
            # actual_mappings = get_key_mappings()

        # Then
        self.assertDictEqual(actual_mappings, expected_mappings)

    def test_it_should_be_able_to_tranform_data_based_on_mapping(self):
        # Given
        data = {"userid": "Kostas"}
        key_mappings = {"userid": "user_id"}
        expected_transformed_data = {"user_id": "Kostas"}

        # When
        actual_tranformed_data = transform_data(data=data, key_mapping=key_mappings)

        # Then
        self.assertDictEqual(actual_tranformed_data, expected_transformed_data)

    def test_it_should_be_able_to_return_subset_of_values(self):
        # Given
        data = {"userid": "Kostas","email":"email@gmail.com"}
        key_mappings = {"userid": "userid"}
        expected_transformed_data = {"userid": "Kostas"}

        # When
        actual_tranformed_data = transform_data(data=data, key_mapping=key_mappings)

        # Then
        self.assertDictEqual(actual_tranformed_data, expected_transformed_data)


if __name__ == '__main__':
    unittest.main()
