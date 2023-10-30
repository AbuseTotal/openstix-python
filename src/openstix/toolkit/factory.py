from tracemalloc import start
import uuid

from stix2.canonicalization.Canonicalize import canonicalize
from stix2.base import _make_json_serializable
from stix2.environment import ObjectFactory

__all__ = [
    "DeterministicObjectFactory",
    "ObjectFactory"
]

ID_CONTRIBUTING_PROPERTIES = {
    "relationship": [
        "source_ref",
        "target_ref",
        "relationship_type",
        "start_time",
        "stop_time",
    ],
    "sighting": [
        "sighting_of_ref",
        "observed_data_refs",
        "where_sighted_refs"
    ],
    "location": [
        "name",
        "region",
        "country",
        "city",
        "latitude",
        "longitude",
    ]
}

class DeterministicObjectFactory(ObjectFactory):

    def __init__(self, *args, namespace, **kwargs):
        self.namespace = namespace
        super().__init__(*args, **kwargs)

    def create(self, cls, **kwargs):
        _id = self._generate_id(cls, **kwargs)
        return super().create(cls, id=_id, **kwargs)

    def _generate_id(self, cls, **kwargs):
        id_ = None
        json_serializable_object = {}

        if hasattr(cls, "_id_contributing_properties"):
            contributing_properties = cls._id_contributing_properties
        else:
            contributing_properties = ID_CONTRIBUTING_PROPERTIES.get(cls._type, [])

        for key in contributing_properties:

            if key in kwargs and kwargs[key] is not None:
                serializable_value = _make_json_serializable(kwargs[key])
                json_serializable_object[key] = serializable_value

        if json_serializable_object:
            data = canonicalize(json_serializable_object, utf8=False)
            uuid_ = uuid.uuid5(self.namespace, data)
            id_ = "{}--{}".format(cls._type, str(uuid_))

        return id_