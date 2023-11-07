from openstix._base import _load_submodules

submodules = {}
submodules.update(_load_submodules("stix2.v21.sro", "extensions"))

__all__ = list(submodules.keys())

globals().update(submodules)
