---
hide:
  - navigation
  - toc
---

# OpenSTIX

OpenSTIX is an unofficial library and toolkit built upon the foundations of the STIX2 library, aimed at enhancing the efficiency and productivity of cybersecurity professionals. It's developed and maintained by AbuseTotal, a startup committed to delivering high-quality software solutions in the cybersecurity domain.


## Features

- **Modular Design**: Organizes the functionalities provided by STIX2 library into modules for easy consumption and extension.
- **Workspace Class**: Extends the `Environment` class into a `Workspace` class to facilitate seamless creation, removal, and management of STIX SDOs (Structured Data Objects) based on contributing properties.
- **Static Namespace Management**: Allows users to define a static namespace for their organization, ensuring consistent identification and management across STIX objects.
- **Contributing Properties-based ID Management**: Enables operations on STIX SDOs with identical IDs, governed by specific contributing properties.
- **Built-in Datasets**: Provides ready-to-use datasets including MITRE frameworks, geolocations, custom TLP markings, and industries to expedite the analytical process.
- **Custom Objects and Extensions**: Offers custom objects and extensions to assist analysts with additional informational resources such as Whois and DNS-Records.