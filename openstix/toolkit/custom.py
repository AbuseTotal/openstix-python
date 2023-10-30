from .._base import _load_submodules

globals().update(_load_submodules("stix2.v21.common", "custom"))
globals().update(_load_submodules("stix2.v21.observables", "custom"))
globals().update(_load_submodules("stix2.v21.sdo", "custom"))
globals().update(_load_submodules("stix2.v21.sro", "custom"))