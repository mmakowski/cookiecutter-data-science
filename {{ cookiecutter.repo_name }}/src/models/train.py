# -*- coding: utf-8 -*-
import logging
import click
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.linear_model import LogisticRegression
from sklearn2pmml import PMMLPipeline
from sklearn2pmml.feature_extraction.text import Splitter
import data


@click.command()
@click.argument('training_data_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
def main(training_data_file, output_file):
    """ Fits the pipeline.
    """
    logger = logging.getLogger(__name__)
    x, y = data.load(training_data_file)
    pipeline = _train(x, y)
    _write_pkl(output_file, pipeline)


def _train(x, y):
    logger = logging.getLogger(__name__)
    # TODO: replace the below with actual implementation
    logger.error("TODO: implement _train() in src/model/train.py")
    vectorizer = CountVectorizer(ngram_range=(1, 2), token_pattern=None, tokenizer=Splitter())
    feature_selector = SelectKBest(score_func=chi2, k=10)
    classifier = LogisticRegression()
    pipeline = PMMLPipeline([
        ("vectorizer", vectorizer),
        ("feature_selector", feature_selector),
        ("classifier", classifier)
    ])
    logger.info("fitting the pipeline...")
    pipeline.fit(x, y)
    return pipeline


def _write_pkl(output_file, pipeline):
    logger = logging.getLogger(__name__)
    joblib.dump(pipeline, output_file)
    logger.info("pipeline written to %s", output_file)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
