from mitreattack.stix20.custom_attack_objects import (  # noqa: F401
    Asset,
    DataComponent,
    DataSource,
    Matrix,
    Tactic,
)

from openstix.datasets._base import Dataset
from openstix.properties import StringProperty
from openstix.toolkit.custom import CustomObject
from openstix.toolkit.filters import Filter
from openstix.toolkit.filters.presets import (
    CAMPAIGN_FILTER,
    COURSE_OF_ACTION_FILTER,
    INTRUSION_SET_FILTER,
    MALWARE_FILTER,
    SOFTWARE_FILTER,
    TOOL_FILTER,
)


@CustomObject(
    "x-mitre-collection",
    [
        ("name", StringProperty(required=True)),
        ("description", StringProperty(required=True)),
    ],
)
class Collection:
    pass


MITIGATIONS_FILTER = COURSE_OF_ACTION_FILTER
TECHNIQUE_FILTER = Filter("x_mitre_is_subtechnique", "=", False)
SUBTECHNIQUE_FILTER = Filter("x_mitre_is_subtechnique", "=", True)
DATASOURCE_FILTER = Filter("type", "=", "x-mitre-datasource")
DATA_COMPONENT_FILTER = Filter("type", "=", "x-mitre-data-component")
ASSET_FILTER = Filter("type", "=", "x-mitre-asset")
MATRIX_FILTER = Filter("type", "=", "x-mitre-matrix")
TACTIC_FILTER = Filter("type", "=", "x-mitre-tactic")
COLLECTION_FILTER = Filter("type", "=", "x-mitre-collection")


class MITREDataset(Dataset):
    source = "mitre"
    files = {
        "attack-enterprise.json": "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack.json",
        "attack-mobile.json": "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/mobile-attack/mobile-attack.json",
        "attack-ics.json": "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/ics-attack/ics-attack.json",
        "capec.json": "https://raw.githubusercontent.com/mitre/cti/master/capec/2.1/stix-capec.json",
    }

    def _query_name_and_alias(self, filters, name, alias=True, revoked=False):
        filters += [Filter("name", "=", name)]
        if alias:
            filters += [Filter("aliases", "contains", name)]

        return self._query_one(filters, revoked=False)

    def techniques(self, include_subtechniques=True, revoked=False) -> list:
        filters = [TECHNIQUE_FILTER]
        if not include_subtechniques:
            filters += [SUBTECHNIQUE_FILTER]
        return self._query(filters, revoked)

    def subtechniques(self, revoked=False) -> list:
        return self._query([SUBTECHNIQUE_FILTER], revoked)

    def technique(self, external_id, revoked=False):
        external_id_filter = [
            TECHNIQUE_FILTER,
            Filter("external_references.external_id", "=", external_id),
        ]
        return self._query_one(external_id_filter)

    def subtechnique(self, external_id, revoked=False):
        external_id_filter = [
            SUBTECHNIQUE_FILTER,
            Filter("external_references.external_id", "=", external_id),
        ]
        return self._query_one(external_id_filter)

    def intrusion_sets(self, revoked=False):
        return self._query([INTRUSION_SET_FILTER])

    def intrusion_set(self, name, alias=True, revoked=False):
        return self._query_name_and_alias([INTRUSION_SET_FILTER])

    def campaigns(self, revoked=False):
        return self._query([CAMPAIGN_FILTER])

    def campaign(self, name, alias=True, revoked=False):
        return self._query_name_and_alias([CAMPAIGN_FILTER])

    def malwares(self, revoked=False):
        return self._query([MALWARE_FILTER])

    def malware(self, name, alias=True, revoked=False):
        return self._query_name_and_alias([MALWARE_FILTER])

    def tools(self, revoked=False):
        return self._query([TOOL_FILTER])

    def tool(self, name, alias=True, revoked=False):
        return self._query_name_and_alias([TOOL_FILTER])

    def collections(self, revoked=False):
        return self._query([COLLECTION_FILTER])

    def collection(self, name, alias=True, revoked=False):
        return self._query_name_and_alias([COLLECTION_FILTER])

    def matrices(self, revoked=False):
        return self._query([MATRIX_FILTER])

    def matrix(self, name, alias=True, revoked=False):
        return self._query_name_and_alias([MATRIX_FILTER])

    def tactics(self, revoked=False):
        return self._query([TACTIC_FILTER])

    def tactic(self, name, alias=False, revoked=False):
        return self._query_name_and_alias([TACTIC_FILTER])

    def mitigations(self, revoked=False):
        return self._query([MITIGATIONS_FILTER])

    def mitigation(self, name, alias=False, revoked=False):
        return self._query_name_and_alias([MITIGATIONS_FILTER])

    def softwares(self, revoked=False):
        return self._query([SOFTWARE_FILTER])

    def software(self, name, alias=True, revoked=False):
        return self._query_name_and_alias([SOFTWARE_FILTER])

    def data_sources(self, revoked=False):
        return self._query([DATASOURCE_FILTER])

    def data_source(self, name, alias=False, revoked=False):
        return self._query_name_and_alias([DATASOURCE_FILTER])

    def data_components(self, revoked=False):
        return self._query([DATA_COMPONENT_FILTER])

    def data_component(self, name, alias=False, revoked=False):
        return self._query_name_and_alias([DATA_COMPONENT_FILTER])

    def assets(self, revoked=False):
        return self._query([ASSET_FILTER])

    def asset(self, name, alias=False, revoked=False):
        return self._query_name_and_alias([ASSET_FILTER])
