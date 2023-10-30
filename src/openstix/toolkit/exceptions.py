from stix2.datastore import DataSourceError

from .._base import _load_submodules

globals().update(_load_submodules("stix2.v21.observables", "errors"))
globals().update(_load_submodules("stix2.v21.sdo", "errors"))
globals().update(_load_submodules("stix2.v21.sro", "errors"))
globals().update(_load_submodules("stix2.v21.common", "errors"))

from stix2.exceptions import *
