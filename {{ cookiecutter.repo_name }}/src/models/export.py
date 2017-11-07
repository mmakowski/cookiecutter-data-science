# -*- coding: utf-8 -*-
import logging
import click
from sklearn.externals import joblib
from sklearn2pmml import sklearn2pmml


@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
def main(input_file, output_file):
    """ Exports the pipeline to PMML.
    """
    logger = logging.getLogger(__name__)
    logger.info("loading the pipeline from %s...", input_file)
    pipeline = joblib.load(input_file)
    logger.info("exporting the pipeline to %s...", output_file)
    sklearn2pmml(pipeline, output_file, with_repr=True)
    logger.info("pipeline exported")


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
