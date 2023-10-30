from ._base import _load_submodules

globals().update(_load_submodules("stix2.v21.common", "definitions"))
globals().update(_load_submodules("stix2.v21.observables", "definitions"))
globals().update(_load_submodules("stix2.v21.sdo", "definitions"))
globals().update(_load_submodules("stix2.v21.sro", "definitions"))
