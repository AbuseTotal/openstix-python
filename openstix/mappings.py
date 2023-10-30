from ._base import _load_submodules, _map_types

SCOS_MAPPING = _map_types(_load_submodules("stix2.v21.observables", "objects"))
SCOS_EXTENSIONS_MAPPING = _map_types(_load_submodules("stix2.v21.observables", "extensions"))

SDOS_MAPPING = _map_types(_load_submodules("stix2.v21.sdo", "objects"))
SDOS_EXTENSIONS_MAPPING = _map_types(_load_submodules("stix2.v21.sdo", "extensions"))

SROS_MAPPING = _map_types(_load_submodules("stix2.v21.sro", "objects"))
SROS_EXTENSIONS_MAPPING = _map_types(_load_submodules("stix2.v21.sro", "extensions"))

SMOS_MAPPING = _map_types(_load_submodules("stix2.v21.common", "meta"))

STIX_OBJECTS_MAPPING = {}
STIX_OBJECTS_MAPPING.update(SCOS_MAPPING)
STIX_OBJECTS_MAPPING.update(SDOS_MAPPING)
STIX_OBJECTS_MAPPING.update(SROS_MAPPING)
STIX_OBJECTS_MAPPING.update(SMOS_MAPPING)

STIX_OBJECTS_EXTENSIONS_MAPPING = {}
STIX_OBJECTS_EXTENSIONS_MAPPING.update(SCOS_EXTENSIONS_MAPPING)
STIX_OBJECTS_EXTENSIONS_MAPPING.update(SDOS_EXTENSIONS_MAPPING)
STIX_OBJECTS_EXTENSIONS_MAPPING.update(SROS_EXTENSIONS_MAPPING)
