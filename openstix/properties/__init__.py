from .._base import _load_submodules

globals().update(_load_submodules("stix2.properties", "properties"))

from . import types
