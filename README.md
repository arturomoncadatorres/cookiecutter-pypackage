# Cookiecutter PyPackage
######  A Cookiecutter template for a Python (Data Science) package

This repository contains a [Cookiecutter template](https://github.com/cookiecutter/cookiecutter) for creating Python packges. It is originally based on [audreyr's fantastic original `cookiecutter-pypackage`](https://github.com/audreyr/cookiecutter-pypackage/). I took the liberty of updating it using more recent tools. More importantly, I added a few quality-of-life improvements. Many of these were done with a Data Science mindset. However, this Cookiecutter can very well be used as a base for other types of projects.

<p align="center">
  <a href="#tada-features">Features</a> •
  <a href="#bulb-quickstart">Quickstart</a> •
  <a href="#man_teacher-tutorial">Tutorial</a> •
  <a href="#memo-release-checklist">Release checklist</a> •
  <a href="#card_index_dividers-package-organization">Package organization</a> •
  <a href="#page_with_curl-license">License</a> •
  <a href="#gift_heart-contributing">Contributing</a>
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
I wanted to keep things simple. I think that having separate documentation for such a small project was a bit of an overkill. Thus I decided to have all the repository's documentation in this README.
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

#### 0. Pre-requisites
* Have a [GitHub account](https://github.com/). For this tutorial, we will use `github_username` as an example.
* Have a [ReadTheDocs account](https://readthedocs.org/)
* Have a [PyPI (Python Package Index) account](https://pypi.org/)
* Have a [PyUp account](https://pyup.io/) (which will be linked to your GitHub account)

#### 1. Setup your environment
First, we need to create a virtual environment in which we will be working on the package development. You can do so using your preferred tool. Personally, I like [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands). Be sure to activate your created environment.

###### Enter Cookiecutter
As you have probably seen in other projects, creating a package requires configuring a lot of files to be in a very specific structure. This can be prone to errors, specially if this is your first time.

Enter [Cookiecutter](https://github.com/cookiecutter/cookiecutter). Cookiecutter is the key tool that will make this process much easier. In short, it allows you to easily create a project based on pre-existing cookiecutters (i.e., templates).

You need to install Cookiecutter in your environment, which you can do using conda:

```bash
conda config --add channels conda-forge
conda install cookiecutter
```

or using pip:

```bash
pip install cookiecutter
```

#### 2. Generate package files
Now, we will actually generate the files. In your prompt, move to the directory where your project will live. Once there, type:

```bash
cookiecutter https://github.com/arturomoncadatorres/cookiecutter-pypackage.git
```

A series of prompts will ask you about the characteristics of your project. At the time of writing, these are:

* `full_name` <br>
Your full name.

* `email` <br>
Your email address.

* `github_username` <br>
Your GitHub username (`github_username` in our example).

* `project_name` <br>
The name of the package. This is used in documentation, so spaces and special characters are ok. For now, we will use `Cool Package` as an example.

* `project_slug` <br>
This is the *namespace* of your Python package. This should be Python import-friendly. Typically, it is the [slugified](https://stackoverflow.com/questions/427102/what-is-a-slug-in-django) version (i.e., human-readable, unique identifier) of `project_name`. Therefore, in our case this would be `cool-package`.

* `project_short_description` <br>
A short description (preferably one sentence) of your package's purpose.

* `pypi_username` <br>
Your PyPI username.

* `version` <br>
The starting version number of the package. If this is the package's first iteration, I recommend sticking to `0.1.0`.

* `use_pytest` <br>
Whether to use [`pytest`](https://docs.pytest.org/en/latest/) (a framework for code testing).

* `use_pypi_deployment_with_travis` <br>
Whether to use PyPI deployment with [Travis CI (continuous integration](https://travis-ci.org/), a framework for automatically building and testing code changes, providing you with feedback almost immediately).

* `add_pyup_badge` <br>
Whether to include a [`PyUp` badge](https://github.com/pyupio/pyup) (a service for tracking and updating your dependencies). We will assume you chose so as well for the rest of the tutorial (step 7).

* `command_line_interface` <br>
Whether to create a console script using Click. Console script entry point will match the `project_slug`. Possible options are `Click`, `Argparse`, and `No command-line interface` <br>
(*TODO: I'm still figuring what these are used for*).

* `create_author_file` <br>
Whether to create an authors file. I recommend you do.

* `open_source_license`
Choosing a license for your project is important. Possible options are
  * 1. MIT License
  * 2. BSD license
  * 3. ISC license
  * 4. Apache Software License 2.0
  * 5. GNU General Public License v3
  * 6. Not open source

  If you are unsure of which license would be better for your project, take a look at [`choosealicense.com`](https://choosealicense.com/)


#### 3. Put files under version control in GitHub
Next, we need to put our newly-created files under version control using GitHub. Go to GitHub and create a new repository. Make sure that the repository's name matches that defined `project_slug`.

Make sure that you have [configured your SSH key properly](https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account). Now, in your project's directory, open a Git Bash and type:

```
git init
git remote add origin git@github.com/github_username/cool-package.git
git add .
git commit -m "Initial commit"
git push -u origin master
```

#### 4. Install requirements
Now, we need to install the new project's local development requirements. We can do so by typing:

```bash
pip install -r requirements_dev.txt
```

*TODO: I will probably change this configuration later. I would prefer having requirement files organized a little bit more neatly.*

#### 5. Configure Travis CI
Afterwards, we will configure [Travis CI](https://travis-ci.org/). First, we need to do so online. Just login with your GitHub credentials, click on your profile picture and go to settings. In the section "Legacy Services Integration", you will see all your (public) repositories (the first time it might take a few minutes, be patient). Simply turn on the switch of your repository of interest.

Next, we need to configure Travis locally. To do so, we need Ruby. Check if you have it installed already by typing in the console

```
ruby -v
```

If you have it already, you will see the current version of Ruby. If not, follow the [instructions here](https://www.ruby-lang.org/en/documentation/installation/). Afterwards, install Travis by typing

```
gem install travis
```

Check if the installation was successful by typing

```
travis version
```

Finally, we need to encrypt our PyPI password in the Travis configuration. Moreover, we also need to automate deployment on PyPI when pushing a new tag to the master branch. To do this, we need to type in the console

```
travis encrypt password --add deploy.password
```

You will get asked if you want to rewrite the contents of `.travis.yml`. Say yes. After that, commit and push this change to GitHub

```
git add .travis.yml
git commit -m "Updated .travis.yml"
git push -u origin master
```

#### 6. Configure ReadTheDocs
Login to [ReadTheDocs](https://readthedocs.org/). Click on your profile picture, which will bring you to your dashboard. Here, you can choose to import a project. Select your package repository and follow the instructions.

One important thing. Do notice that the package documentation uses [Sphinx](https://www.sphinx-doc.org/en/master/), which relies on `.rst` (reStructureText) files. This format is different from (your probably familiar) `.md` (Markdown) files. While you might be tempted to switch to Markdown, [it is not advisable](https://www.ericholscher.com/blog/2016/mar/15/dont-use-markdown-for-technical-docs/). For technical documentation, it is well worth investing some time in learning how to work with `.rst` files.

By default, your documentation will have the lovely [`sphinx-rtd-theme`](https://sphinx-rtd-theme.readthedocs.io/en/stable/). Note that you can also very easily change several [configuration options](https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html). However, we will stick to the defaults for now.


#### 7. Configure PyUp
PyUp is a handy tool that takes care of updating your dependencies automatically. To configure it, login to [PyUp](https://pyup.io/) using your GitHub credentials. Then, click on the button `+ Add Repo` and select your `cool-package` repository. Confirm the dialogue. After that, your PyUp badge in your `README` will be updated automatically.

If you originally chose not to have a PyUp badge (Step 2) and you changed your mind, you can add it very easily. Just add the following lines in your `README.md` wherever you want the badge to show (probably at the top):

```
[![PyUp](https://pyup.io/repos/github/github_username/cool-package/shield.svg)](https://pyup.io/repos/github/github_username/cool-package/)
```

#### 8. Release on (Test)PyPI
As you might have guessed, the last step is to actually release your package to PyPI. If you are unsure, you can always try releasing it first on [TestPyPI](https://test.pypi.org/). This is a good place to use as a sandbox.

*TODO: I will update this section once I have some hands on experience with the actual release. On the meantime, you can check some other [tutorials online](https://dev.to/wangonya/publishing-your-python-packages-on-testpypi-before-publishing-on-pypi-2gb2).*

<!--
To create releases, type in Console

```bash
bump2version patch
git push --tags
```

This will result in:
cool-package 0.1.1 showing up in your GitHub tags/releases page
cool-package 0.1.1 getting released on PyPI
You can also replace patch with minor or major.
-->

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
