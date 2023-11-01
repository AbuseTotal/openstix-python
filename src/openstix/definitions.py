from openstix._base import _load_submodules

submodules = {}
submodules.update(_load_submodules("stix2.v21.common", "definitions"))
submodules.update(_load_submodules("stix2.v21.observables", "definitions"))
submodules.update(_load_submodules("stix2.v21.sdo", "definitions"))
submodules.update(_load_submodules("stix2.v21.sro", "definitions"))

__all__ = list(submodules.keys())

globals().update(submodules)
