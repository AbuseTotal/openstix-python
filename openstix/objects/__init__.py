from stix2.v21.bundle import Bundle

from .._base import _load_submodules

globals().update(_load_submodules("stix2.v21.observables", "objects"))
globals().update(_load_submodules("stix2.v21.sdo", "objects"))
globals().update(_load_submodules("stix2.v21.sro", "objects"))
globals().update(_load_submodules("stix2.v21.common", "meta"))

from . import custom
