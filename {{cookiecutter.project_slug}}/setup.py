#!/usr/bin/env python

"""The setup script."""

import setuptools

with open("README.md") as f:
    LONG_DESCRIPTION, LONG_DESC_TYPE = f.read(), "text/markdown"

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open("requirements/base_requirements.txt") as f:
    REQUIREMENTS = f.read().splitlines()
	
setup_requirements = [{%- if cookiecutter.use_pytest == 'y' %}'pytest-runner',{%- endif %} ]

test_requirements = [{%- if cookiecutter.use_pytest == 'y' %}'pytest>=3',{%- endif %} ]

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setuptools.setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    python_requires='>=3.5',
	
	# For a complete list of classifiers, see https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
		'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    description="{{ cookiecutter.project_short_description }}",
    {%- if 'no' not in cookiecutter.command_line_interface|lower %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:main',
        ],
    },
    {%- endif %}
    install_requires=REQUIREMENTS,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    include_package_data=True,
    keywords='{{ cookiecutter.project_slug }}',
    name='{{ cookiecutter.project_slug }}',
    packages=setuptools.find_packages(include=['{{ cookiecutter.project_slug }}', '{{ cookiecutter.project_slug }}.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    version=0.1.0, # For a complete description of versioning, see https://www.python.org/dev/peps/pep-0440/
    zip_safe=False,
)
