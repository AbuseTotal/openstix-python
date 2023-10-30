def _build_filters():
    from stix2.datastore.filters import Filter

    from ...mappings import SROS_MAPPING, SDOS_MAPPING, SCOS_MAPPING

    object_types = list(SROS_MAPPING.keys()) + list(SDOS_MAPPING.keys()) + list(SCOS_MAPPING.keys())

    data = {}

    for object_type in object_types:
        constant = object_type.replace('-', '_').upper() + "_FILTER"
        data[constant] = Filter('type', '=', object_type)

    return data

globals().update(_build_filters())