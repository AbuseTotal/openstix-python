from ._base import _load_submodules

globals().update(_load_submodules("stix2.v21.observables", "vocab"))
globals().update(_load_submodules("stix2.v21.sdo", "vocab"))
globals().update(_load_submodules("stix2.v21.sro", "vocab"))