from openstix._base import _load_submodules, _map_types


SCOS_MAPPING = _map_types(_load_submodules("openstix.objects.scos", "objects"))
SCOS_EXTENSIONS_MAPPING = _map_types(_load_submodules("openstix.objects.scos", "extensions"))

SDOS_MAPPING = _map_types(_load_submodules("openstix.objects.sdos", "objects"))
SDOS_EXTENSIONS_MAPPING = _map_types(_load_submodules("openstix.objects.sdos", "extensions"))

SROS_MAPPING = _map_types(_load_submodules("openstix.objects.sros", "objects"))
SROS_EXTENSIONS_MAPPING = _map_types(_load_submodules("openstix.objects.sros", "extensions"))

SMOS_MAPPING = _map_types(_load_submodules("openstix.objects.smos", "objects"))

STIX_OBJECTS_MAPPING = {}
STIX_OBJECTS_MAPPING.update(SCOS_MAPPING)
STIX_OBJECTS_MAPPING.update(SDOS_MAPPING)
STIX_OBJECTS_MAPPING.update(SROS_MAPPING)
STIX_OBJECTS_MAPPING.update(SMOS_MAPPING)

STIX_OBJECTS_EXTENSIONS_MAPPING = {}
STIX_OBJECTS_EXTENSIONS_MAPPING.update(SCOS_EXTENSIONS_MAPPING)
STIX_OBJECTS_EXTENSIONS_MAPPING.update(SDOS_EXTENSIONS_MAPPING)
STIX_OBJECTS_EXTENSIONS_MAPPING.update(SROS_EXTENSIONS_MAPPING)
