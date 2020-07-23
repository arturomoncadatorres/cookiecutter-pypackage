# {{ cookiecutter.project_name }}
######  {{ cookiecutter.project_short_description }}
{% if is_open_source %}
[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})
[![Build Status](https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg?branch=master)](https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
[![Documentation](https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest)](https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest)
{%- endif %}
{% if cookiecutter.add_pyup_badge == 'y' %}
[![PyUp](https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/shield.svg)](https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/)
{% endif %}

A long description of your package goes here.

## :tada: Features
* Features
* of
* your
* cool 
* package

{% if is_open_source %}
## :bookmark_tabs: Documentation
You can find the complete package's documentation [here](https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io).
{% endif %}

{% if is_open_source %}
## :page_with_curl: License
This package uses the {{ cookiecutter.open_source_license }}
{% endif %}

## :black_nib: References
If you are using {{ cookiecutter.project_name }}, please cite the current repository as follows:
> * {{ cookiecutter.full_name }}. {{ cookiecutter.project_name }}. Accessed on [MONTH, 20XX].

## :label: Credits
This package was created with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [`arturomoncadatorres/cookiecutter-pypackage` project template](https://github.com/arturomoncadatorres/cookiecutter-pypackage)
