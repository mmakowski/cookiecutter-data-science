# -*- coding: utf-8 -*-
import logging
import click
from sklearn.model_selection import train_test_split


@click.command()
@click.argument('input_dir', type=click.Path(exists=True))
@click.argument('output_dir', type=click.Path())
def main(input_dir, output_dir):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    dataset_name = "TODO-dataset-name"
    base_path = "%s/%s" % (input_dir, dataset_name)
    id_text_labels = _read_raw_data(base_path)
    logger.info("parsed %d examples", len(id_text_labels))
    train, holdout = _train_holdout_split(id_text_labels)
    _write_tsv("%s/train.tsv" % output_dir, train)
    _write_tsv("%s/holdout.tsv" % output_dir, holdout)
    logger.info("data processing completed")


def _read_raw_data(raw_data_path):
    logger = logging.getLogger(__name__)
    logger.info('reading data from %s', raw_data_path)
    # TODO: replace the lines below with transformation from raw data to a
    # list of id/text/label
    logger.error("TODO: implement _read_raw_data() in src/data/process.py")
    return [(i, "dummy item %d" % i, i % 2) for i in range(100)]


def _train_holdout_split(id_text_labels):
    all_features = [(doc_id, text)
                    for (doc_id, text, label) in id_text_labels]
    all_labels = [label for (doc_id, text, label) in id_text_labels]
    train_features, holdout_features, train_labels, holdout_labels = \
        train_test_split(all_features,
                         all_labels,
                         test_size=0.1,
                         random_state=0)

    def _recombine(features, labels):
        return [(doc_id, text, label)
                for ((doc_id, text), label) in zip(features, labels)]

    return _recombine(train_features, train_labels),\
        _recombine(holdout_features, holdout_labels)


def _write_tsv(path, data):
    with open(path, "w") as output_file:
        output_file.write("id\ttext\tlabel\n")
        for line_data in data:
            output_file.write("%s\t%s\t%s\n" % line_data)
    logger = logging.getLogger(__name__)
    logger.info('wrote %d entries to %s', len(data), path)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    main()
