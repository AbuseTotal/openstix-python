import importlib
import inspect

IGNORE = {"NOW", "itertools", "OrderedDict", "STIXDeprecationWarning", "EXTENSION_TYPE"}
WORKAROUND_NAMES = {"AlternateDataStream", "WindowsPESection", "EmailMIMEComponent"}

def _is_relevant_member(name, member):
    """Check if a member is relevant for mapping."""

    return inspect.isclass(member) and hasattr(member, "_type")

def _map_types(types):
    """Return a mapping of _type attributes to class members for a given module."""

    return {object_class._type: object_class for object_class in types.values() if hasattr(object_class, "_type")}

def categorize_name(name):
    """Categorize a module attribute by its name."""

    if name.startswith('_') or name.islower() or name in IGNORE:
        return None

    if name in WORKAROUND_NAMES:
        return "property_types"

    if name in ['ExternalReference', 'KillChainPhase']:
        return "properties"

    if name == "URL":
        return "objects"

    if name.isupper():
        return "vocab"

    if name.startswith('Custom'):
        return "custom"

    if name.endswith('Marking') or name == "LanguageContent":
        return "meta"

    if name.endswith('Definition'):
        return "definitions"

    if name.endswith('Property'):
        return "properties"

    if name.endswith('Type'):
        return "property_types"

    if name.endswith('Ext'):
        return "extensions"

    if name.endswith('Error'):
        return "errors"

    return "objects"

def collect_module_data(module):
    """Categorize and collect module attributes."""

    data = {
        "custom": [],
        "objects": [],
        "properties": [],
        "property_types": [],
        "extensions": [],
        "errors": [],
        "vocab": [],
        "definitions": [],
        "meta": [],
    }

    for name in dir(module):
        category = categorize_name(name)
        if category:
            data[category].append(name)

    return data

def _load_submodules(module_name, section):
    """Load and return submodules of a module based on the provided section."""

    module = importlib.import_module(module_name)
    data = collect_module_data(module)
    
    return {name: getattr(module, name) for name in data[section]}