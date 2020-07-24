# Cookiecutter PyPackage
######  A Cookiecutter template for a Python (Data Science) package

This repository contains a [Cookiecutter template](https://github.com/cookiecutter/cookiecutter) for creating Python packges. It is originally based on [audreyr's fantastic original `cookiecutter-pypackage`](https://github.com/audreyr/cookiecutter-pypackage/). I took the liberty of updating it using more recent tools. More importantly, I added a few quality-of-life improvements. Many of these were done with a Data Science mindset. However, this Cookiecutter can very well be used as a base for other types of projects.

<p align="center">
  <a href="#tada-features">Features</a> •
  <a href="#bulb-quickstart">Quickstart</a> •
  <a href="#man_teacher-tutorial">Tutorial</a> •
  <a href="#memo-release-checklist">Release checklist</a> •
  <a href="#card_index_dividers-package-organization">Package organization</a> •
  <a href="#page_with_curl-how-to-use">License</a> •
  <a href="#gift_heart-how-to-use">Contributing</a>
</p>

---------------------------------------------------------------------------
## :tada: Features
**Original features**
* Testing setup with `unittest` and `python setup.py test` or `pytest`
* [Travis-CI](https://travis-ci.org/): ready for Travis CI (Continuous Integration) testing
* [Tox testing](http://testrun.org/tox/): setup to easily test for Python 3.6, 3.7, 3.8
* [Sphinx docs](https://www.sphinx-doc.org/en/master/): documentation ready for generation with [Read the Docs](https://readthedocs.org/)
* [`bump2version`](https://github.com/c4urself/bump2version): pre-configured version bumping with a single command
* Auto-release to [PyPI](https://pypi.org/) when you push a new tag to master (optional)
* Command line interface using Click (optional)

**Quality-of-life improvements:**
* Updated requirements to more recent versions
* Concentrated original documentation into this README <br>
I think that having separate documentation for such a small project was a bit of an overkill. Thus I decided to have all the repository's documentation in this README.
* Added a `data` directory, together with its corresponding README <br>
Data Science projects often require at least some basic sample data to get users started. You can put all your data files here. Moreover, you can (and should) describe them in the accompanying README.
* Added an `examples` directory <br>
This is the perfect place to include use cases (e.g., Jupyter notebooks) where you show how your package works.
* [Updated the generated project's README from .rst to .md](https://github.com/arturomoncadatorres/cookiecutter-pypackage/issues/2)
* [Changed the generated project's default documentation style from Alabaster to Sphinx-rtd-theme](https://github.com/arturomoncadatorres/cookiecutter-pypackage/issues/1)
* Added issue templates for bugs reports, documentation improvements, feature suggestions, and others.

## :bulb: Quickstart
TODO

## :man_teacher: Tutorial
TODO

## :memo: Release checklist
TODO:

## :card_index_dividers: Package organization
The generated package will have the following structure

    ├── .github            <- Useful files for GitHub
    │   └── ISSUE_TEMPLATE <- Issue templates
    │                         Templates include bug, documentation, feature, and other.
    │
    ├── data               <- Sample data.
    │                         Nice to have for creating demos of your package.
    │
    ├── docs               <- A default Sphinx project. See sphinx-doc.org for details.
    │
    ├── examples           <- Example use cases of your packages.
    │                         Perfect place for Jupyter notebooks with demos.
    │
    ├── tests              <- Tests
    │
    ├── project_dir        <- Contains the actual files of your package.
    │                         Uses the `project_slug`
    │
    ├── .editorconfig
    │
    ├── .gitignore
    │
    ├── .travis.yml        <- Travis configuration
    │
    ├── AUTHORS.rst        <- Credits
    │
    ├── CONTRIBUTING.rst   <- Contribution guidelines
    │
    ├── HISTORY.rst        <- Version history
    │
    ├── LICENSE            <- See https://choosealicense.com/
    │
    ├── MANIFEST.in
    │
    ├── Makefile
    │
    ├── README.md          <- The top-level README for users of the package.
    │
    ├── requirements_dev.txt
    │
    ├── setup.cfg
    │
    ├── setup.py
    │
    └── tox.ini            <- tox file with settings for running tox. See tox.testrun.org


## :page_with_curl: License
Open source under the [BSD license](./LICENSE)

## :gift_heart: Contributing
If this template doesn't match your use case, feel free to check these other [Cookiecutters for Python packages](https://github.com/audreyr/cookiecutter-pypackage#not-exactly-what-you-want). Moreover, feel free to fork the current one to create your own version. [Feedback](https://github.com/arturomoncadatorres/cookiecutter-pypackage/issues) and [pull requests](https://github.com/arturomoncadatorres/cookiecutter-pypackage/pulls) for improving this Cookiecutter are always welcome!
