from ..toolkit.filters.presets import ATTACK_PATTERN_FILTER, INTRUSION_SET_FILTER
from ..toolkit.custom import CustomObject
from ..properties import StringProperty
from ..toolkit.filters import Filter
from ._base import Dataset

# Objects:
# 'x-mitre-tactic'
# 'intrusion-set'
# 'tool'
# 'malware'
# 'x-mitre-collection'
# 'attack-pattern'
# 'campaign'
# 'x-mitre-matrix'
# 'course-of-action'
# 'relationship'
# 'x-mitre-data-source'
# 'x-mitre-data-component'
# 'identity'

class MITREDataset(Dataset):

    source = "mitre"
    files = {
        "attack-enterprise.json": "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack.json",
        "attack-mobile.json": "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/mobile-attack/mobile-attack.json",
        "attack-ics.json": "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/ics-attack/ics-attack.json",
        "capec.json": "https://raw.githubusercontent.com/mitre/cti/master/capec/2.1/stix-capec.json",
    }

    def attack_patterns(self):
        return self._query(ATTACK_PATTERN_FILTER)

    def attack_pattern(self, external_id):
        external_id_filter = [ATTACK_PATTERN_FILTER, Filter("external_references.external_id", "=", external_id)]
        return self._query_one(external_id_filter)

    def intrusion_sets(self):
        return self._query(INTRUSION_SET_FILTER)

    def intrusion_set(self, name):
        name_filter = [INTRUSION_SET_FILTER, Filter("name", "=", name)]
        aliases_filter = [INTRUSION_SET_FILTER, Filter("aliases", "contains", name)]

        obj = self._query_one(name_filter)
        if obj:
            return obj
        return self._query_one(aliases_filter)


@CustomObject(
    "x-mitre-collection",
    [
        ("name", StringProperty(required=True)),
        ("description", StringProperty(required=True)),
    ]
)
class MITRECollection:
    # "type",
    # "id",
    # "spec_version",
    # "x_mitre_attack_spec_version",
    # "name",
    # "x_mitre_version",
    # "description",
    # "created_by_ref",
    # "created",
    # "modified",
    # "object_marking_refs",
    # "x_mitre_contents"
    pass

@CustomObject(
    "x-mitre-data-component",
    [
        ("name", StringProperty(required=True)),
        ("description", StringProperty(required=True)),
    ]
)
class MITREDataComponent:
    # "object_marking_refs",
    # "id",
    # "type",
    # "created",
    # "created_by_ref",
    # "modified",
    # "name",
    # "description",
    # "x_mitre_data_source_ref",
    # "x_mitre_version",
    # "x_mitre_attack_spec_version",
    # "x_mitre_modified_by_ref",
    # "spec_version",
    # "x_mitre_domains"
    pass

@CustomObject(
    "x-mitre-data-source",
    [
        ("name", StringProperty(required=True)),
        ("description", StringProperty(required=True)),
    ]
)
class MITREDataSource:
    # "x_mitre_platforms",
    # "x_mitre_domains",
    # "x_mitre_contributors",
    # "x_mitre_collection_layers",
    # "object_marking_refs",
    # "id",
    # "type",
    # "created",
    # "created_by_ref",
    # "external_references",
    # "modified",
    # "name",
    # "description",
    # "x_mitre_version",
    # "x_mitre_attack_spec_version",
    # "x_mitre_modified_by_ref",
    # "spec_version"
    pass

@CustomObject(
    "x-mitre-matrix",
    [
        ("name", StringProperty(required=True)),
        ("description", StringProperty(required=True)),
        # ("tactic_refs", ListProperty(ObjectReferenceProperty(valid_types=["x-mitre-tactic"]))),
    ]
)
class MITREMatrix:
    # "tactic_refs",
    # "x_mitre_domains",
    # "object_marking_refs",
    # "created",
    # "description",
    # "created_by_ref",
    # "external_references",
    # "id",
    # "modified",
    # "name",
    # "type",
    # "x_mitre_attack_spec_version",
    # "x_mitre_modified_by_ref",
    # "x_mitre_version",
    # "spec_version"
    pass

@CustomObject(
    "x-mitre-tactic",
    [
        ("name", StringProperty(required=True)),
        ("description", StringProperty(required=True)),
    ]
)
class MITRETactic:
    # "modified",
    # "name",
    # "description",
    # "x_mitre_deprecated",
    # "x_mitre_domains",
    # "x_mitre_version",
    # "x_mitre_shortname",
    # "type",
    # "id",
    # "created",
    # "created_by_ref",
    # "revoked",
    # "external_references",
    # "object_marking_refs",
    # "x_mitre_attack_spec_version",
    # "x_mitre_modified_by_ref",
    # "spec_version"
    pass