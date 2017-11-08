# Cookiecutter DR DS

Based on [cookiecutter-data-science](http://drivendata.github.io/cookiecutter-data-science/).

### Requirements to use the cookiecutter template:

 - Python 2.7 or 3.5
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:

    cookiecutter https://github.com/mmakowski/cookiecutter-dr-ds


### The resulting directory structure

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile             <- Makefile with commands like `make data` or `make train`
├── README.md            <- The top-level README for developers using this project.
├── data
│   ├── external         <- Data from third party sources.
│   ├── processed        <- The final, canonical data sets for modeling.
│   └── raw              <- The original, immutable data dump.
│
├── docs                 <- A default Sphinx project; see sphinx-doc.org for details
│
├── models               <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks            <- Jupyter notebooks. Naming convention is a number (for ordering),
│                           the creator's initials, and a short `-` delimited description, e.g.
│                           `01.0-mm-initial-data-exploration`.
│
├── references           <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports              <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures          <- Generated graphics and figures to be used in reporting
│
├── requirements.txt     <- The requirements file for reproducing the analysis environment, e.g.
│                           generated with `pip freeze > requirements.txt`
│
├── src                  <- Source code for use in this project.
│   ├── __init__.py      <- Makes src a Python module
│   │
│   ├── data             <- Scripts to download, generate and transform data
│   │   └── process.py   <- [template] transforms the raw data into the canonical format and
|   |                       splits into the training and holdout.
│   │
│   ├── models           <- Scripts to train, evaluate and export the pipeline
│   │   ├── evaluate.py  <- [template] evaluates the trained pipeline on the holdout set.
|   |   ├── export.py    <- [template] exports the trained pipeline to PMML.
│   │   └── train.py     <- [template] Trains the pipeline.
│   │
│   └── visualization    <- Scripts to create exploratory and results oriented visualizations
│
└── tox.ini              <- tox file with settings for running tox; see tox.testrun.org
```

### First steps

To set up the development sandbox, run:

```
make create_environment
source activate <project name>
make requirements
```

Then `make evaluate` will train and evaluate a dummy model.

### Next steps

1. Put the raw data in `data/raw`, or create a script to download the data from source repository.
2. Edit `src/data/process.py` to transform the raw data into TSV files.
3. Edit `src/models/train.py` to specify how the model should be trained.


### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests
