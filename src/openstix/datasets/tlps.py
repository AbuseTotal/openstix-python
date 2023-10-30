from stix2.v21.common import TLP_WHITE as _WHITE
from stix2.v21.common import TLP_GREEN as _GREEN
from stix2.v21.common import TLP_AMBER as _AMBER
from stix2.v21.common import TLP_RED as _RED

from ._base import Dataset


class TLPsDataset(Dataset):

    source = "tlps"

    def get(name):
        if name == "white":
            return _WHITE
        elif name == "green":
            return _GREEN
        elif name == "amber":
            return _AMBER
        elif name == "red":
            return _RED
        else:
            raise ValueError("Invalid TLP name: {}".format(name))

    @property
    def red(self):
        return _RED

    @property
    def amber(self):
        return _AMBER

    @property
    def green(self):
        return _GREEN

    @property
    def white(self):
        return _WHITE