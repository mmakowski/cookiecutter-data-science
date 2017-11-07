# -*- coding: utf-8 -*-
import logging
import pandas as pd


def load(data_file):
    """ Loads data from provided TSV file. Returns the pair of X (text)
        and Y (0/1 labels)
    """
    logger = logging.getLogger(__name__)
    logger.info("loading data from %s...", data_file)
    data = pd.read_csv(data_file, sep='\t')
    x_text = data['text']
    y = data['label']
    logger.info("loaded %d examples", len(x_text))
    return x_text, y
