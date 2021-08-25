#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("requirements.txt") as f:
    requirements = f.read().split("\n")

setup_requirements = ["pytest-runner"]
test_requirements = ["pytest"]

setup(
    name="slackmsg",
    description="A Slack Library to simplifiy sending a slack message from a python app.",
    version="1.0",
    license="Apache license",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords="slackmsg slack",
    author="Steven George",
    author_email="steven.blog@hardtechnology.net",
    url="https://github.com/steven_geo/slackmsg",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7"
    ],
    install_requires=requirements,
    include_package_data=True,
    packages=find_packages(include=["slackmsg"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    zip_safe=False,
        entry_points={
        'console_scripts': [
            'slackmsg = slackmsg.cli:main'
        ]
    }
)
