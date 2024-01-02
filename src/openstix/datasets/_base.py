import os
from abc import ABC
from pathlib import Path

import requests

from openstix.toolkit import Workspace as Workspace
from openstix.toolkit.filters import Filter
from openstix.utils.common import parse


FOLDER_PATH = "~/.openstix"
NOT_REVOKED_FILTER = Filter("revoked", "=", False)


class Dataset(ABC):
    source = None
    files = None
    folder = Path(os.path.expanduser(FOLDER_PATH))

    def __init__(self):
        self.workspace = Workspace()

    def download(self):
        if self.source is None or self.files is None:
            return

        source_folder = self.folder / self.source
        source_folder.mkdir(parents=True, exist_ok=True)

        for filename, url in self.files.items():
            filepath = source_folder / filename

            if os.path.exists(filepath):
                print(f"Skipping {filepath} ...")
                continue

            print(f"Collecting {filepath} ...")
            response = requests.get(url)
            with open(filepath, "w") as f:
                f.write(response.text)

    def load(self):
        if self.source is None or self.files is None:
            return

        source_folder = self.folder / self.source
        if not source_folder.exists():
            return

        for filename in os.listdir(source_folder):
            with open(source_folder / filename) as fp:
                data = fp.read()
                self._parse(data)

    def _parse(self, data):
        bundle = parse(data, allow_custom=True)
        self.workspace.add(bundle.objects)
        self._check_not_supported_objects()

    def _check_not_supported_objects(self):
        for obj in self.workspace.query():
            if isinstance(obj, dict):
                print(f"Unsupported object type: {obj.type}")

    def _query(self, filters=[], revoked=False):
        if not revoked:
            filters.append(NOT_REVOKED_FILTER)
        return self.workspace.query(filters)

    def _query_one(self, filters=[], revoked=False):
        objects = self._query(filters, revoked=revoked)
        if objects:
            return objects[0]
        return None
