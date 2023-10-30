from countryinfo import CountryInfo

from ..toolkit.filters.presets import LOCATION_FILTER
from ..objects import Relationship, Location
from ..toolkit.filters import Filter
from ._base import Dataset

REGION_FILTER = Filter("x_location_type", "=", "region")
SUBREGION_FILTER = Filter("x_location_type", "=", "sub-region")
COUNTRY_FILTER = Filter("x_location_type", "=", "country")
CITY_FILTER = Filter("x_location_type", "=", "city")

COMMON_PROPERTIES_VALUES = {
    "confidence": 100,
    "revoked": False,
    "allow_custom": True,
}

class GeoLocationsDataset(Dataset):

    source = "geolocations"
    files = None

    def regions(self):
        return self._query([LOCATION_FILTER, REGION_FILTER])

    def region(self, region):
        region_filter = [LOCATION_FILTER, REGION_FILTER, Filter("region", "=", region)]
        return self._query_one(region_filter)

    def subregions(self):
        return self._query([LOCATION_FILTER, SUBREGION_FILTER])

    def subregion(self, subregion):
        subregion_filter = [LOCATION_FILTER, SUBREGION_FILTER, Filter("region", "=", subregion)]
        return self._query_one(subregion_filter)
    
    def countries(self):
        return self._query([LOCATION_FILTER, COUNTRY_FILTER])

    def country(self, country):
        country_filter = [LOCATION_FILTER, COUNTRY_FILTER, Filter("country", "=", country)]
        return self._query_one(country_filter)

    def cities(self):
        return self._query([LOCATION_FILTER, CITY_FILTER])

    def city(self, city):
        city_filter = [LOCATION_FILTER, CITY_FILTER, Filter("city", "=", city)]
        return self._query_one(city_filter)

    def load(self):
        for key in CountryInfo().all():

            item = CountryInfo(key).info()

            region = None
            subregion = None
            country = None
            capital = None

            if "region" in item and item["region"] != "":
                region = self.workspace.create(
                    Location,
                    name=item["region"],
                    region=item["region"],
                    x_location_type="region",
                    **COMMON_PROPERTIES_VALUES,
                )

            if "subregion" in item and item["subregion"] != "":
                subregion = self.workspace.create(
                    Location,
                    name=item["subregion"],
                    region=item["subregion"],
                    x_location_type="sub-region",
                    **COMMON_PROPERTIES_VALUES,
                )

            if region and subregion:
                self.workspace.create(
                    Relationship,
                    relationship_type="located-at",
                    source_ref=subregion.id,
                    target_ref=region.id,
                    **COMMON_PROPERTIES_VALUES,
                )

            if "name" in item and item["name"] != "" and "ISO" in item and item["ISO"]["alpha2"] != "":
                latitude, longitude = None, None
                if "latlng" in item:
                    latitude = item["latlng"][0]
                    longitude = item["latlng"][1]

                # WORKAROUND: https://github.com/oasis-open/cti-python-stix2/issues/572
                if latitude == 0:
                    latitude = 0.01
                if longitude == 0:
                    longitude = 0.01

                country = self.workspace.create(
                    Location,
                    name=item["name"],
                    country=item["ISO"]["alpha2"],
                    latitude=latitude,
                    longitude=longitude,
                    x_location_type="country",
                    **COMMON_PROPERTIES_VALUES,
                )

            if country and region:
                self.workspace.create(
                    Relationship,
                    relationship_type="located-at",
                    source_ref=country.id,
                    target_ref=region.id,
                    **COMMON_PROPERTIES_VALUES,
                )

            if country and subregion:
                self.workspace.create(
                    Relationship,
                    relationship_type="located-at",
                    source_ref=country.id,
                    target_ref=subregion.id,
                    **COMMON_PROPERTIES_VALUES,
                )

            if "capital" in item and item["capital"] != "":
                latitude, longitude = None, None
                if "capital_latlng" in item:
                    latitude = item["capital_latlng"][0]
                    longitude = item["capital_latlng"][1]

                # WORKAROUND: https://github.com/oasis-open/cti-python-stix2/issues/572
                if latitude == 0:
                    latitude = 0.01
                if longitude == 0:
                    longitude = 0.01

                capital = self.workspace.create(
                    Location,
                    name=item["capital"],
                    city=item["capital"],
                    latitude=latitude,
                    longitude=longitude,
                    country=item["ISO"]["alpha2"],
                    x_location_type="city",
                    **COMMON_PROPERTIES_VALUES,
                )

            if country and capital:
                self.workspace.create(
                    Relationship,
                    relationship_type="located-at",
                    source_ref=capital.id,
                    target_ref=country.id,
                    **COMMON_PROPERTIES_VALUES,
                )

            if "provinces" in item:
                for _province in item["provinces"]:

                    if _province == "":
                        continue

                    province = self.workspace.create(
                        Location,
                        name=_province,
                        city=_province,
                        country=item["ISO"]["alpha2"],
                        x_location_type="city",
                        **COMMON_PROPERTIES_VALUES,
                    )

                    if not country:
                        continue

                    self.workspace.create(
                        Relationship,
                        relationship_type="located-at",
                        source_ref=province.id,
                        target_ref=country.id,
                        **COMMON_PROPERTIES_VALUES,
                    )
