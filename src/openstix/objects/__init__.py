from openstix._base import _load_submodules

submodules = {}
submodules.update(_load_submodules("stix2.v21.observables", "objects"))
submodules.update(_load_submodules("stix2.v21.sdo", "objects"))
submodules.update(_load_submodules("stix2.v21.sro", "objects"))
submodules.update(_load_submodules("stix2.v21.common", "meta"))

__all__ = list(submodules.keys())

globals().update(submodules)
