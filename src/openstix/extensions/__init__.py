from .._base import _load_submodules

globals().update(_load_submodules("stix2.v21.observables", "extensions"))
globals().update(_load_submodules("stix2.v21.sdo", "extensions"))
globals().update(_load_submodules("stix2.v21.sro", "extensions"))

from . import custom
