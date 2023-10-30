from pathlib import Path
from abc import ABC
import uuid
import os

import requests

from ..toolkit.stores import MemoryStore as MemoryStore
from ..toolkit import Workspace as Workspace
from ..utils.common import parse

XITS_NAMESPACE = uuid.UUID("52117afa-30ca-4b46-bb7b-0531fa2f8aec")
FOLDER_PATH = "~/.xits2"

class Dataset(ABC):
    source = None
    files = None
    folder = Path(os.path.expanduser(FOLDER_PATH))

    def __init__(self):
        self.workspace = Workspace(namespace=XITS_NAMESPACE)

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
            with open(filepath, 'w') as f:
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

    def _query(self, filters=[]):
        return self.workspace.query(filters)

    def _query_one(self, filters=[]):
        objects = self._query(filters)
        if objects:
            return objects[0]
        return None
