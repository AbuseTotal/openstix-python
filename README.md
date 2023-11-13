# OpenSTIX

OpenSTIX is an **unofficial STIX 2.1 library and toolkit** built upon the foundations of the [STIX2 library](https://github.com/oasis-open/cti-python-stix2/), aimed at enhancing the efficiency and productivity of cybersecurity professionals. It's developed and maintained by AbuseTotal, a startup committed to delivering high-quality software solutions in the cybersecurity domain.

[![PyPI version](https://badge.fury.io/py/openstix.svg)](https://badge.fury.io/py/openstix)

## Features

- **Modular Design**: Organizes the functionalities provided by STIX2 library into modules for easy consumption and extension.
- **Workspace Class**: Extends the `Environment` class into a `Workspace` class to facilitate seamless creation, removal, and management of STIX SDOs (Structured Data Objects) based on contributing properties.
- **Static Namespace Management**: Allows users to define a static namespace for their organization, ensuring consistent identification and management across STIX objects.
- **Contributing Properties-based ID Management**: Enables operations on STIX SDOs with identical IDs, governed by specific contributing properties.
- **Built-in Datasets**: Provides ready-to-use datasets including MITRE frameworks, geolocations, custom TLP markings, and industries to expedite the analytical process.
- **Custom Objects and Extensions**: Offers custom objects and extensions to assist analysts with additional informational resources such as Whois and DNS-Records.


## Installation

```bash
pip install openstix
```

## Usage

Import the necessary modules and get started with creating and managing STIX objects within your defined workspace.

#### Start workspace
```python
from openstix.toolkit.workspace import Workspace

# Create a new workspace with your organization's namespace
workspace = Workspace(namespace="<your-namespace-uuid>")
```

#### Parse and load stix data into workspace
```python
data = """
{
    "type": "bundle",
    "id": "bundle--0ef10afc-6a6b-4df7-bc4b-099977bfcba8",
    "objects": [
        {
            "type": "domain-name",
            "spec_version": "2.1",
            "id": "domain-name--9076dffc-9b97-55f6-a720-bc115b25fe31",
            "value": "openstix.dev"
        }
    ]
}
"""

# Parse STIX data and load automatically the objects in workspace
workspace.parse(data)
```


#### Create SCO within workspace
```python
from openstix.objects import DomainName

# Add STIX observable object (SCO)
domain = self.workspace.create(Domain, value="abusetotal.com")
```

#### Remove object from workspace
```python
# Remove STIX observable object (SCO)
self.workspace.remove(domain.id)
```

#### Create SDO within workspace
```python
from openstix.objects import Malware

# Add STIX domain object (SDO)
self.workspace.create(Malware, name="Malicious", is_family=False)
```

#### Filter workspace objects using presets filters
```python
from openstix.toolkit.filters.presets import MALWARE_FILTER

# Filter objects using presets
malwares = self.workspace.query(MALWARE_FILTER)
```

#### Download STIX datasets

```bash
$ openstix datasets download --all
```

#### Get MITRE TTP using MITRE Datasets

**Note:** make sure you have downloaded the dataset using openstix cli

```python
from openstix.datasets import MITREDataset

dataset = MITREDataset()
dataset.load()

# Use Attack Pattern objects from MITRE Dataset
attack_pattern = dataset.attack_pattern("T1090")
```

#### Get country and regions objects using GeoLocation Datasets

**Note:** make sure you have downloaded the dataset using openstix cli

```python
from openstix.datasets import GeoLocationsDataset

dataset = GeoLocationsDataset()
dataset.load()

# Use Location objects from GeoLocation Dataset
country = dataset.country("PT")
region = dataset.region("Europe")
```

## Contributing

We welcome contributions to OpenSTIX! Whether you're reporting bugs, proposing new features, or contributing code, we appreciate your help. Please make sure to read our Contributing Guidelines before making a contribution.

## License

OpenSTIX is licensed under the Apache 2.0.

## Contact

For any inquiries, issues, or support related to OpenSTIX, feel free to reach out to us at support@abusetotal.com.

## Acknowledgements

OpenSTIX is an initiative by AbuseTotal to foster the development of cybersecurity tools and libraries. We thank the OASIS Cyber Threat Intelligence Technical Committee and all STIX community for laying down the robust foundation upon which OpenSTIX is built.