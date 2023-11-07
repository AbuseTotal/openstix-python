from openstix.datasets import GeoLocationsDataset
from openstix.datasets import MITREDataset
from openstix.toolkit import Workspace

from openstix.objects import Malware, IPv4Address, DomainName, Relationship

import uuid


mitre = MITREDataset()
mitre.load()

geolocation = GeoLocationsDataset()
geolocation.load()

workspace = Workspace(namespace=uuid.UUID("4b4f4769-85f5-4b3c-b950-48b2f90803de"))

domain = workspace.create(DomainName, value="abusetotal.com")
ipv4 = workspace.create(IPv4Address, value="54.74.172.227")
workspace.create(Relationship, relationship_type="resolves-to", source_ref=domain.id, target_ref=ipv4.id)

pass
