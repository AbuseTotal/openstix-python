from stix2.v21.bundle import Bundle

from openstix._base import _load_submodules

imports = {}
imports.update(_load_submodules("stix2.v21.observables", "objects"))
imports.update(_load_submodules("stix2.v21.sdo", "objects"))
imports.update(_load_submodules("stix2.v21.sro", "objects"))
imports.update(_load_submodules("stix2.v21.common", "meta"))

globals().update(imports)

from openstix.objects import custom

__all__ = list(imports.keys)