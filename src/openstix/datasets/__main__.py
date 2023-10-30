import click

from .geolocations import GeoLocationsDataset
from .mitre import MITREDataset
from .tlps import TLPsDataset

datasets_classes = [
    GeoLocationsDataset,
    MITREDataset,
    TLPsDataset,
]

@click.command()
@click.option('--source', default=None, help='The name of the source you want to download.')
@click.option('--all', 'download_all', is_flag=True, default=False, help='Download all available sources.')
def main(source, download_all):
    for dataset_class in datasets_classes:
        if download_all or source == dataset_class.source:
            dataset_class().download()

if __name__ == "__main__":
    main()

