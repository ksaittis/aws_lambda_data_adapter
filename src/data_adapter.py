from typing import Dict
import os
import json

def transform_data(data: Dict[str,str], key_mapping: Dict[str,str]) -> Dict[str,str]:
    transformed_data = {}
    for key, value in data.items():
        if key in key_mapping:
          transformed_key = key_mapping[key]
          transformed_data[transformed_key] = value
    return transformed_data


def get_key_mappings() -> Dict[str, str]:
    key_mappings: str = os.environ.get("KEY_MAPPINGS", "{}")
    try:
        return json.loads(key_mappings)
    except json.JSONDecodeError as e:
        return dict()
