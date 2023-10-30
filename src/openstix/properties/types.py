from .._base import _load_submodules

globals().update(_load_submodules("stix2.v21.observables", "property_types"))
globals().update(_load_submodules("stix2.v21.sdo", "property_types"))
globals().update(_load_submodules("stix2.v21.sro", "property_types"))