from openstix.toolkit.custom import CustomObservable
from openstix.properties import StringProperty


@CustomObservable(
    "x-dns-record",
    [
        ("record_class", StringProperty(required=True)),
        ("record_type", StringProperty(required=True)),
        ("record_ttl", StringProperty(required=True)),
        ("value", StringProperty(required=True)),
    ],
    [
        "record_class",
        "record_type",
        "record_ttl",
        "value",
    ],
)
class DNSRecord:
    pass
