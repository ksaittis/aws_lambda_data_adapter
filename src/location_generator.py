from typing import Dict

from enum import Enum


class EntityType(Enum):
    ASSET = 'asset_name'
    USER = 'username'

    @classmethod
    def get(cls, value):
        for entity in cls:
            if value in entity.value:
                return entity
        return None

    @classmethod
    def get_entity_from_payload(cls, payload):
        entity_type = get_entity_type(payload)
        return EntityType.get(entity_type)


def get_entity_type(payload: Dict) -> str:
    if 'entity_type' in payload:
        return payload['entity_type']
    return ''


def generate_location(payload: Dict):
    values = []
    entity = EntityType.get_entity_from_payload(payload)
    allowed_keys = ['venue_name', 'building_name', 'region_name', entity.value]
    for key in allowed_keys:
        if key in payload and payload[key]:
            values.append(payload[key].replace(" ", "-"))
    return "-".join(values)
