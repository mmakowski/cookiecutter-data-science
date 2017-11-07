# -*- coding: utf-8 -*-
import logging
import click
from sklearn import metrics
from sklearn.externals import joblib
import data


@click.command()
@click.argument('pipeline_file', type=click.Path(exists=True))
@click.argument('holdout_data_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
def main(pipeline_file, holdout_data_file, output_file):
    """ Evaluates the pipeline.
    """
    logger = logging.getLogger(__name__)
    x, y_true = data.load(holdout_data_file)
    logger.info("loading the pipeline from %s...", pipeline_file)
    pipeline = joblib.load(pipeline_file)
    y_pred = pipeline.predict(x)
    results = _format_metrics(y_true, y_pred)
    logger.info("results:\n%s", results)
    _write_results(results, output_file)


def _format_metrics(y_true, y_pred):
    return """auROC: %.4f

%s

confusion matrix:
%s
""" % (metrics.roc_auc_score(y_true, y_pred),
       metrics.classification_report(y_true, y_pred),
       metrics.confusion_matrix(y_true, y_pred))


def _write_results(results, output_file_path):
    with open(output_file_path, "w") as output_file:
        output_file.write(results)
    logging.getLogger(__name__).info("results written to %s", output_file_path)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
