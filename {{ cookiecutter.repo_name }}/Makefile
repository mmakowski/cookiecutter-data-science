.PHONY: clean data train evaluate export lint requirements create_environment test_environment

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME = {{ cookiecutter.repo_name }}
PYTHON_INTERPRETER = {{ cookiecutter.python_interpreter }}

ifeq (,$(shell which conda))
HAS_CONDA=False
else
HAS_CONDA=True
endif

ifeq (,$(shell which git))
IN_GIT_REPO=False
else
ifeq (true,$(shell git rev-parse --is-inside-work-tree 2>/dev/null))
IN_GIT_REPO=True
else
IN_GIT_REPO=False
endif
endif

ifeq (,$(shell which md5sum))
MD5=md5
else
MD5=md5sum
endif

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install Python dependencies
requirements: test_environment
	pip install -r requirements.txt

## Transform raw data into the datasets
data: $(PROJECT_DIR)/data/processed/train.tsv $(PROJECT_DIR)/data/processed/holdout.tsv

## Train and save the pipeline
train: $(PROJECT_DIR)/models/pipeline.pkl

## Evaluate the pipeline
evaluate: $(PROJECT_DIR)/models/results.txt

## Export the pipeline to PMML
export: $(PROJECT_DIR)/models/pipeline.pmml $(PROJECT_DIR)/models/pipeline.manifest

## Delete all compiled Python files and derived data files
clean:
	find . -name "*.pyc" -exec rm {} \;
	rm -rf $(PROJECT_DIR)/data/processed/*
	rm -rf $(PROJECT_DIR)/models/*

## Lint using flake8
lint:
	flake8 --exclude=lib/,bin/,docs/conf.py .

## Set up python interpreter environment
create_environment:
ifeq (True,$(HAS_CONDA))
		@echo ">>> Detected conda, creating conda environment."
ifeq (3,$(findstring 3,$(PYTHON_INTERPRETER)))
	conda create --name $(PROJECT_NAME) python=3
else
	conda create --name $(PROJECT_NAME) python=2.7
endif
		@echo ">>> New conda env created. Activate with:\nsource activate $(PROJECT_NAME)"
else
	@pip install -q virtualenv virtualenvwrapper
	@echo ">>> Installing virtualenvwrapper if not already intalled.\nMake sure the following lines are in shell startup file\n\
	export WORKON_HOME=$$HOME/.virtualenvs\nexport PROJECT_HOME=$$HOME/Devel\nsource /usr/local/bin/virtualenvwrapper.sh\n"
	@bash -c "source `which virtualenvwrapper.sh`;mkvirtualenv $(PROJECT_NAME) --python=$(PYTHON_INTERPRETER)"
	@echo ">>> New virtualenv created. Activate with:\nworkon $(PROJECT_NAME)"
endif

## Test python environment is setup correctly
test_environment:
	$(PYTHON_INTERPRETER) test_environment.py

#################################################################################
# PROJECT RULES                                                                 #
#################################################################################

$(PROJECT_DIR)/data/processed/train.tsv: src/data/process.py $(PROJECT_DIR)/data/raw
	$(PYTHON_INTERPRETER) src/data/process.py $(PROJECT_DIR)/data/raw $(PROJECT_DIR)/data/processed

$(PROJECT_DIR)/data/processed/holdout.tsv: src/data/process.py $(PROJECT_DIR)/data/raw
	$(PYTHON_INTERPRETER) src/data/process.py $(PROJECT_DIR)/data/raw $(PROJECT_DIR)/data/processed

$(PROJECT_DIR)/models/pipeline.pkl: src/models/train.py $(PROJECT_DIR)/data/processed/train.tsv
	$(PYTHON_INTERPRETER) src/models/train.py $(PROJECT_DIR)/data/processed/train.tsv $(PROJECT_DIR)/models/pipeline.pkl

$(PROJECT_DIR)/models/results.txt: src/models/evaluate.py $(PROJECT_DIR)/models/pipeline.pkl $(PROJECT_DIR)/data/processed/holdout.tsv
	$(PYTHON_INTERPRETER) src/models/evaluate.py $(PROJECT_DIR)/models/pipeline.pkl $(PROJECT_DIR)/data/processed/holdout.tsv $(PROJECT_DIR)/models/results.txt

$(PROJECT_DIR)/models/pipeline.pmml: src/models/export.py $(PROJECT_DIR)/models/pipeline.pkl
	$(PYTHON_INTERPRETER) src/models/export.py $(PROJECT_DIR)/models/pipeline.pkl $(PROJECT_DIR)/models/pipeline.pmml

$(PROJECT_DIR)/models/pipeline.manifest: $(PROJECT_DIR)/models/pipeline.pmml
	@echo "::: pmml md5 checksum:  " `$(MD5) $(PROJECT_DIR)/models/pipeline.pmml` > $(PROJECT_DIR)/models/pipeline.manifest
	@echo "::: timestamp:          " `date -u` >> $(PROJECT_DIR)/models/pipeline.manifest
	@echo "::: host:               " `hostname` >> $(PROJECT_DIR)/models/pipeline.manifest
	@echo "::: user:               " `whoami` >> $(PROJECT_DIR)/models/pipeline.manifest
	@echo "::: data md5 checksums:" >> $(PROJECT_DIR)/models/pipeline.manifest
	@$(MD5) $(PROJECT_DIR)/data/processed/* >> $(PROJECT_DIR)/models/pipeline.manifest
ifeq (True,$(IN_GIT_REPO))
	@echo "::: git remotes:" >> $(PROJECT_DIR)/models/pipeline.manifest
	@git remote -v  >> $(PROJECT_DIR)/models/pipeline.manifest
	@echo "::: git head:           " `git rev-parse HEAD` >> $(PROJECT_DIR)/models/pipeline.manifest
	@echo "::: git uncommitted:" >> $(PROJECT_DIR)/models/pipeline.manifest
	@git status -s  >> $(PROJECT_DIR)/models/pipeline.manifest
else
	@echo "::: not in a git repo!" >> $(PROJECT_DIR)/models/pipeline.manifest
endif
	@echo "::: python version:     " `$(PYTHON_INTERPRETER) --version 2>&1` >> $(PROJECT_DIR)/models/pipeline.manifest
	@echo "::: pip packages:" >> $(PROJECT_DIR)/models/pipeline.manifest
	@pip freeze >> $(PROJECT_DIR)/models/pipeline.manifest
ifeq (True,$(HAS_CONDA))
	@echo "::: conda version:      " `conda --version` >> $(PROJECT_DIR)/models/pipeline.manifest
	@echo "::: conda packages:"  >> $(PROJECT_DIR)/models/pipeline.manifest
	@conda list >> $(PROJECT_DIR)/models/pipeline.manifest
endif
	@echo "pipeline manifest written to $(PROJECT_DIR)/models/pipeline.manifest"

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := show-help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: show-help
show-help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
