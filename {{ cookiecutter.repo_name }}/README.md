{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Setup
-----

Prerequisites:

* [Anaconda](https://www.anaconda.com/distribution/) installed and avaiable on `PATH`

With `conda` on `PATH`, in the project directory:

    make create_environment
    source activate {{cookiecutter.repo_name}}
    make requirements evaluate

This will setup the sandbox, install all required libraries and then train and evaluate the pipeline.

You can type `make` without any arguments to see the available commands.


Project Organization
------------

    ├── Makefile             <- Makefile with commands like `make data` or `make train`
    ├── README.md            <- The top-level README for data scientists using this project.
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
    └── src                  <- Source code for use in this project.
        ├── data             <- Scripts to download, generate and transform data
        ├── models           <- Scripts to train, evaluate and export the pipeline
        └── visualization    <- Scripts to create exploratory and results oriented visualizations

