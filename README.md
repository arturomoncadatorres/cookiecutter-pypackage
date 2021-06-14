# Cookiecutter PyPackage
######  A Cookiecutter template for Python (Data Science) packages

This repository contains a [Cookiecutter template](https://github.com/cookiecutter/cookiecutter) for creating Python packges. It is originally based on [audreyr's fantastic original `cookiecutter-pypackage`](https://github.com/audreyr/cookiecutter-pypackage/). I took the liberty of updating it using more recent tools. More importantly, I added a few quality-of-life improvements. Many of these were done with a Data Science mindset. However, this Cookiecutter can very well be used as a base for other types of projects.

<p align="center">
  <a href="#tada-features">Features</a> •
  <a href="#bulb-quickstart">Quickstart</a> •
  <a href="#man_teacher-tutorial">Tutorial</a> •
  <a href="#memo-release-checklist">Release checklist</a> •
  <a href="#card_index_dividers-package-organization">Package organization</a> •
  <a href="#bomb-troubleshooting">Troubleshooting</a> •
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
* Added a `datasets` directory, together with its corresponding `data` subdirectory (with a README) <br>
Data Science projects often require at least some basic sample data to get users started. You can put all your data files here. Moreover, you can (and should) describe them in the accompanying README.
* Added an `examples` directory <br>
This is the perfect place to include use cases (e.g., Jupyter notebooks) where you show how your package works.
* Improved requirements definition by separating them into different files (`base`, `dev`, `doc`).
* [Updated the generated project's README from .rst to .md](https://github.com/arturomoncadatorres/cookiecutter-pypackage/issues/2)
* [Changed the generated project's default documentation style from Alabaster to Sphinx-rtd-theme](https://github.com/arturomoncadatorres/cookiecutter-pypackage/issues/1)
* Added issue templates for bugs reports, documentation improvements, feature suggestions, and others.
* Updated upload instructions to PyPI

## :bulb: Quickstart
For a detailed description, see the <a href="#man_teacher-tutorial">Tutorial</a>.
* Create a new environment and [install Cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html)
* Generate the package files:
```
cookiecutter https://github.com/arturomoncadatorres/cookiecutter-pypackage.git
```
* Put files under version control in GitHub
* Install the project's local development requirements
```
pip install -r ./requirements/dev_requirements.txt
```
* [Configure Travis CI](https://docs.travis-ci.com/user/tutorial/#to-get-started-with-travis-ci-using-github). Make sure to encrypt your password:
```
travis encrypt password --add deploy.password
```
* Go to [Read the Docs](https://readthedocs.org/) and [import your documentation](https://docs.readthedocs.io/en/stable/intro/import-guide.html)
* Configure [PyUp](https://pyup.io/docs/bot/installation-and-usage/)
* Actually develop your package (commit and push the files to GitHub)
* Release on [(Test)PyPI](https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives)

## :man_teacher: Tutorial

### 0. Pre-requisites
* Have a [GitHub account](https://github.com/). For this tutorial, we will use `github_username` as an example.
* Have a [ReadTheDocs account](https://readthedocs.org/)
* Have a [PyPI (Python Package Index) account](https://pypi.org/)
* Have a [PyUp account](https://pyup.io/) (which will be linked to your GitHub account)

### 1. Setup your environment
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

### 2. Generate package files
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


### 3. Put files under version control in GitHub
Next, we need to put our newly-created files under version control using GitHub. Go to GitHub and create a new repository. Make sure that the repository's name matches that defined `project_slug`.

Make sure that you have [configured your SSH key properly](https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account). Now, in your project's directory (that is in `project_slug` and *not* in `project_slug`/`project_slug`), open a Git Bash and type:

```
git init
git remote add origin git@github.com/github_username/cool-package.git
git add .
git commit -m "Initial commit"
git push -u origin master
```

### 4. Install requirements
Now, we need to install the new project's local development requirements. We can do so by typing:

```bash
pip install -r ./requirements/dev_requirements.txt
```

> If you get the error `ERROR: Could not install packages due to an OSError: [WinError 5] Access is denied`, try doing the install with the `--user` option. That is:
> 
> ```bash
> pip install -r ./requirements/dev_requirements.txt --user
> ```

### 5. Configure Travis CI
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

### 6. Configure Read the Docs
Login to [ReadTheDocs](https://readthedocs.org/). Click on your profile picture, which will bring you to your dashboard. Here, you can choose to import a project. Select your package repository and follow the instructions.

One important thing. Do notice that the package documentation uses [Sphinx](https://www.sphinx-doc.org/en/master/), which relies on `.rst` (reStructureText) files. This format is different from (your probably familiar) `.md` (Markdown) files. While you might be tempted to switch to Markdown, [it is not advisable](https://www.ericholscher.com/blog/2016/mar/15/dont-use-markdown-for-technical-docs/). For technical documentation, it is well worth investing some time in learning how to work with `.rst` files.

By default, your documentation will have the lovely [`sphinx-rtd-theme`](https://sphinx-rtd-theme.readthedocs.io/en/stable/). Note that you can also very easily change several [configuration options](https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html). However, we will stick to the defaults for now.

If you want to test how your documents render, you don't necessarily need to commit, push, and build your files for every change (which is a bit cumbersome). You can also do so locally. Just go to `project_slug/docs` and type
```bash
make html
```
You can see the local documentation files in `project_slug/docs/_build/html`. If you want to examine the landing page, take a look at `index.html`.


### 7. Configure PyUp
PyUp is a handy tool that takes care of updating your dependencies automatically. To configure it, login to [PyUp](https://pyup.io/) using your GitHub credentials. Then, click on the button `+ Add Repo` and select your `cool-package` repository. Confirm the dialogue. After that, your PyUp badge in your `README` will be updated automatically.

If you originally chose not to have a PyUp badge (Step 2) and you changed your mind, you can add it very easily. Just add the following lines in your `README.md` wherever you want the badge to show (probably at the top):

```
[![PyUp](https://pyup.io/repos/github/github_username/cool-package/shield.svg)](https://pyup.io/repos/github/github_username/cool-package/)
```

### 8. First release on PyPI
As you might have guessed, the last step is to actually release your package to PyPI. We will do so [the proper way](https://stackoverflow.com/a/58673788/948768) in two different ways, first on TestPyPI and then on PyPI. For both cases, you will need:

* A [TestPyPI](https://test.pypi.org/account/register/) or a [PyPI account](https://pypi.org/account/register/), respectively.
* `twine` (>= 2.0). If you don't have it, you can install it using pip:
```bash
pip install twine
```

#### Releasing on TestPyPI
If this is the first time you are publishing a package, I strongly suggest you first do so on TestPyPI. In this case and for didactic reasons, we will perform all steps one by one:

* Create the source distribution and wheels for your package:
```bash
python setup.py sdist bdist_wheel
```
* Check your distribution files for potential errors
```bash
twine check dist/*
```
* Upload to TestPyPI <br>
```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
You will be asked your TestPyPI username and password.

#### Releasing on PyPI
If you have some experience with publishing packages, you can publish your package directly to PyPI. Fortunately, the included `Makefile` makes this process very simple:

```bash
make release
```
You will be asked your PyPI username and password.


### 9. Subsequent releases on PyPI
After the first version of your package (`0.1.0` if you stuck to the defaults) is up, you will probably want to keep working on it, improving it, and adding more features. At some point, you will want to update its PyPI release. To do so, follow these steps:

* Go through the :memo: Release Checklist. This helps you make sure you don't miss anything.

  :ballot_box_with_check: Update all your package files with the new functionality. If you were working on a branch, merge it to `master`.

  :ballot_box_with_check: Update `HISTORY.rst` with the proper change log (and maybe your `README`, if you want to feature the new changes).

  :ballot_box_with_check: Commit and push the changes (i.e., make sure your tracked files have no uncommitted changes)

  ```bash
  git commit -m "Changelog for upcoming release 0.1.1."
  git push -u origin master
  ```

* Use `bump2version` to increase the version of your package. I recommend you follow the semantic versioning described in the [PEP 440](https://www.python.org/dev/peps/pep-0440/). In (very) short:

  * 0.1.0 --> 0.1.1 is a `patch`
  * 0.1.0 --> 0.2.0 is a `minor`
  * 0.1.0 --> 1.0.0 is a `major`

  For this example, we will suppose a `patch`

  ```bash
  bump2version patch ./project_slug/version.py
  ```

  This command will update the version number in all necessary files (e.g., `setup.py`, `setup.cfg`, `__init.py__`) plus in all additional files we wish (e.g., `version.py`). If you want to be more specific on the version you are replacing and the new version you are releasing, you can do:

  ```bash
  bump2version --current-version 0.1.0 --new-version 0.1.1 patch ./project_slug/version.py
  ```  

* Push to GitHub

  ```bash
  git push -u origin master
  ```

  This will update the change of version in the different files done by `bump2version`. You will see this in GitHub as `Bump version: 0.1.0 → 0.1.1`.

* From here, you can update your PyPI release in two different ways:

  * **By "hand"**

    * Upload the distribution files to PyPI, similarly to step 8. Again, using the included `Makefile`:

      ```bash
      make release
      ```
      You will be asked your PyPI username and password.

    This method is very simple and straightforward. However, it has the disadvantage that you won't see the release in GitHub's `project_slug/releases`. If you wish to do so, you will have to add it by hand.

  * **Using Travis**

      * `bump2version` creates a tag in its commit which corresponds to the desired version. We can push it to GitHub:

      ```bash
      git push --tags
      ```

     Once pushed, Travis will run its build and if successful, will show the information in GitHub's tags/releases and release it to PyPI.

     This method sounds very convenient. However, it depends on Travis running properly. Of course, this is always desired, but even the smallest error will stop the deployment to PyPI.

 Choose whichever method works better for you. If you choose Travis, don't underestimate the errors that might pop up there! These might actually affect the proper functioning of your package.


## :card_index_dividers: Package organization
The generated package will have the following structure

    ├── .github            <- Useful files for GitHub
    │   └── ISSUE_TEMPLATE <- Issue templates
    │                         Templates include bug, documentation, feature, and other.
    │
    ├── docs               <- A default Sphinx project. See sphinx-doc.org for details.
    │
    ├── examples           <- Example use cases of your packages.
    │                         Perfect place for Jupyter notebooks with demos.
    │
    ├── project_dir        <- Contains the actual files of your package. Uses `project_slug`.
    │   └── datasets       <- Nice to have for creating demos of your package.
    │      └── data        <- Data files go here.
    │          └── README.md
    │
    ├── requirements       <- Contains the different requirement files.
    │   └── base_requirements <- Base requirements for your package. Starts empty.
    │   └── dev_requirements  <- Development requirements. Includes `base_requirements`.
    │   └── doc_requirements  <- Document requirements. Includes `dev_requirements`.
    │
    ├── tests              <- Tests
    │
    ├── .editorconfig
    │
    ├── .gitignore
    │
    ├── .readthedocs.yml   <- YML for better requirement handling in Read the Docs.
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
    ├── setup.cfg
    │
    ├── setup.py
    │
    └── tox.ini            <- tox file with settings for running tox. See tox.testrun.org

## :bomb: Troubleshooting
* I am on Windows and my `Makefile` commands don't work <br>
This is probably because Windows doesn't recognize many of the commands (e.g., `rm`, `find`). This can be solved by [adding Git's bin directory (e.g., `C:\Program Files\Git\usr\bin`) to your `PATH` variable](https://stackoverflow.com/a/46816749/948768). Moreover, make sure that you have [Cygwin installed](https://cygwin.com/install.html) (including the `findutils` package, usually installed by default), that [its directory (e.g., `C:\cygwin64\bin`) is also part of your `PATH` variable](https://stackoverflow.com/a/10840077/948768), and that it is high on the environment variable list to that it is given higher priority that the Windows's.

* I updated my package on PyPI. However, its badge on the `README` still shows the older version. <br>
PyPI badges take some time to update. It will do so automatically in a few minutes. If you want to be absolutely sure of which version is being distributed, go directly to your project's PyPI page.

## :page_with_curl: License
Open source under the [BSD license](./LICENSE)

## :gift_heart: Contributing
If this template doesn't match your use case, feel free to check these other [Cookiecutters for Python packages](https://github.com/audreyr/cookiecutter-pypackage#not-exactly-what-you-want). Moreover, feel free to fork the current one to create your own version. [Feedback](https://github.com/arturomoncadatorres/cookiecutter-pypackage/issues) and [pull requests](https://github.com/arturomoncadatorres/cookiecutter-pypackage/pulls) for improving this Cookiecutter are always welcome!

I would love to know if you found this Cookiecutter useful or if you used it in one of your projects. [Drop me a line on Twitter (@amoncadatorres)](http://www.twitter.com/amoncadatorres)!
