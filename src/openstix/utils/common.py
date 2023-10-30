from stix2.environment import object_equivalence, object_similarity, graph_equivalence, graph_similarity
from stix2.utils import is_stix_type, deduplicate, is_marking, is_object, is_sro, is_sdo, is_sco
from stix2.utils import parse_into_datetime, get_type_from_id, format_datetime
from stix2.parsing import parse_observable, dict_to_stix2, parse
from stix2.utils import get_timestamp as get_current_timestamp
from stix2.hashes import infer_hash_algorithm, check_hash
from stix2.versioning import remove_custom_stix


def class_for_type(stix_type):
    """
    Returns the class for a given STIX type.

    Args:
        stix_type (str): The STIX type to get the class for.

    Returns:
        class: The class for the given STIX type.

    """

    from ..mappings import STIX_OBJECTS_MAPPING

    if is_stix_type(stix_type):
        return STIX_OBJECTS_MAPPING[stix_type]
    else:
        raise ValueError("Invalid STIX type: %s" % stix_type)

def get_object_type(stix_object):
    if is_sco(stix_object):
        return "sco"

    if is_sdo(stix_object):
        return "sdo"

    if is_sro(stix_object):
        return "sro"

    if is_marking(stix_object):
        return "marking"

    if hasattr(stix_object, "_type") and stix_object._type.endswith("-ext"):
        return "extension"

    raise ValueError("Invalid STIX object: %s" % stix_object)