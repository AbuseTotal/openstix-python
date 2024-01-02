import click

from openstix.datasets.geolocations import GeoLocationsDataset
from openstix.datasets.mitre import MITREDataset
from openstix.datasets.tlps import TLPsDataset


datasets_classes = [
    GeoLocationsDataset,
    MITREDataset,
    TLPsDataset,
]


@click.group()
def cli():
    """Command line interface for OpenSTIX."""
    pass


@click.group(help="Datasets operations.")
def datasets():
    pass


@datasets.command(help="Download datasets.")
@click.option("--source", default=None, help="Download the specified source.")
@click.option("--all", "download_all", is_flag=True, default=False, help="Download all available sources.")
@click.pass_context
def download(ctx, source, download_all):
    if not (source or download_all):
        click.echo("Error: You must specify either --source or --all.")
        click.echo()
        click.echo(ctx.get_help())
        ctx.exit(1)

    for dataset_class in datasets_classes:
        if download_all or source == dataset_class.source:
            dataset_class().download()


cli.add_command(datasets)

if __name__ == "__main__":
    cli()
