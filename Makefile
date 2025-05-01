# Detect OS and set proper activate & pip paths
ifeq ($(OS),Windows_NT)
	PY ?= python
	ENV_DIR ?= .venv
	ACTIVATE = $(ENV_DIR)\Scripts\activate
	PIP = $(ENV_DIR)\Scripts\pip.exe
else
	PY ?= python3
	ENV_DIR ?= .venv
	ACTIVATE = source $(ENV_DIR)/bin/activate
	PIP = $(ENV_DIR)/bin/pip
endif

# Setup virtual environment and install dependencies
.PHONY: setup
setup:
	$(PY) -m venv $(ENV_DIR)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	$(PIP) install jupyter pytest nbconvert

# Run all Jupyter Notebooks
.PHONY: run
run:
	$(ACTIVATE) && \
	jupyter nbconvert --to notebook --execute notebooks/week1-2.ipynb --inplace && \
	jupyter nbconvert --to notebook --execute notebooks/week3-4.ipynb --inplace && \
	jupyter nbconvert --to notebook --execute notebooks/week5-6.ipynb --inplace && \
	jupyter nbconvert --to notebook --execute notebooks/week7-8.ipynb --inplace

# Install dependencies only
.PHONY: install
install:
	$(PIP) install -r requirements.txt

# Run tests
.PHONY: test
test:
	$(ACTIVATE) && pytest tests/

# Clean the environment and temp files
.PHONY: clean
clean:
	rm -rf $(ENV_DIR)
	rm -rf __pycache__ .ipynb_checkpoints
	rm -rf notebooks/__pycache__
