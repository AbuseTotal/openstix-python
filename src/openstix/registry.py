from stix2.registry import STIX2_OBJ_MAPS


def register_objects(sdos=[], scos=[], markings=[], extensions=[]):
    data = {
        "observables": scos,
        "objects": sdos,
        "markings": markings,
        "extensions": extensions,
    }

    for key, objects in data.items():
        for stix_object in objects:
            STIX2_OBJ_MAPS["2.1"][key].update({stix_object._type: stix_object})
