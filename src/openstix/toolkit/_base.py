from stix2 import MemoryStore, Environment
from openstix.toolkit.factory import DeterministicObjectFactory
from stix2.environment import ObjectFactory
import uuid

__all__ = [
    "Workspace",
    "ObjectFactory",
    "Environment",
]

class Workspace(Environment):
    """
    Extends the `stix2.Environment` class to provide a customized environment for handling
    STIX objects in a workspace context. Offers functionality for creating, querying, and
    removing STIX objects, including handling multiple versions of objects.
    """

    def __init__(self, namespace):
        """
        Initializes the Workspace with a MemoryStore and a DeterministicObjectFactory.

        Args:
            namespace (str): The namespace URI for generating deterministic STIX object IDs.
        """
        store = MemoryStore()
        factory = DeterministicObjectFactory(namespace=uuid.UUID(namespace))
        super().__init__(store=store, factory=factory)

    def stats(self, query):
        """
        Generates statistics on the STIX objects within the store.

        This function will count the number of occurrences for each type of STIX object.

        Args:
            query (Optional[List], optional): A list of filters representing the query. Defaults to None.

        Returns:
            Dict[str, int]: A dictionary with STIX object types as keys and their counts as values.
        """
        stats = dict()
        for obj in self.query(query):
            stats[obj.type] = stats.get(obj.type, 0) + 1
        return stats

    def create(self, cls, **kwargs):
        """
        Overrides the `create` method of the `Environment` class to add new STIX objects
        to the store immediately upon creation.

        Args:
            cls: the python-stix2 class of the object to be created (eg. Indicator)
            **kwargs: The property/value pairs of the STIX object to be created

        Returns:
            stix2.base._STIXBase: The newly created STIX object.
        """
        obj = super().create(cls, **kwargs)
        self.add(obj)
        return obj

    def query(self, query, unique=True):
        """
        Executes a query against the memory store to retrieve STIX objects.

        Args:
            query (Optional[List], optional): A list of filters representing the query. Defaults to None.
            unique (bool, optional): When True, only the most recent version of each unique object
                                     is returned. Defaults to True.

        Returns:
            List[stix2.base._STIXBase]: A list of STIX objects that match the query criteria. When `unique`
                                        is True, the list will contain only the most recent version of each
                                        unique object.
        """
        all_objects = super().query(query)
        if not unique or not all_objects:
            return all_objects

        def get_most_recent_unique_objects():
            """
            Yields the most recent versions of unique objects, sorted in reverse order of addition.

            Yields:
                stix2.base._STIXBase: Each unique STIX object in the memory store.
            """
            seen = set()
            for obj in reversed(all_objects):
                if obj.id not in seen:
                    seen.add(obj.id)
                    yield obj

        return list(get_most_recent_unique_objects())

    def remove(self, object_id):
        """
        Removes an object, along with all its versions, from the memory store.

        Args:
            object_id (str): The ID of the STIX object to be removed.

        Raises:
            ValueError: If no object with the provided ID could be found.
        """
        try:
            for source in self.source.data_sources:
                del source._data[object_id]
        except KeyError:
            raise ValueError(f"No object found with ID: {object_id}")



