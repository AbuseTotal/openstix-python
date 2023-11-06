from openstix._base import _load_submodules

def vocab():
    modules = {}
    modules["stix2.v21.observables"] = _load_submodules("stix2.v21.observables", "vocab").keys()
    modules["stix2.v21.sdo"] = _load_submodules("stix2.v21.sdo", "vocab").keys()
    modules["stix2.v21.sro"] = _load_submodules("stix2.v21.sro", "vocab").keys()
    return modules

def objects():
    modules = {}
    modules["stix2.v21.observables"] = _load_submodules("stix2.v21.observables", "objects").keys()
    modules["stix2.v21.sdo"] = _load_submodules("stix2.v21.sdo", "objects").keys()
    modules["stix2.v21.sro"] = _load_submodules("stix2.v21.sro", "objects").keys()
    modules["stix2.v21.common"] = _load_submodules("stix2.v21.common", "meta").keys()
    return modules

def printa(modules):
    for module, classes_name in modules.items():
        print("")
        for class_name in classes_name:
            print(f"from {module} import {class_name}")

modules = objects()
printa(modules)
pass


