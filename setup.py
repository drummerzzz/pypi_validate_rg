#!/usr/bin/env python

from setuptools import setup, find_packages  # type: ignore

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="Joao Filho Drummer",
    author_email="devdrummerzzz@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    description="Faz a validação de RG (SSP SP) Brasileiro",
    entry_points={"console_scripts": ["validate_rg=validate_rg.cli:main",],},
    install_requires=[],
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    package_data={"validate_rg": ["py.typed"]},
    include_package_data=True,
    keywords="validate_rg",
    name="validate_rg",
    package_dir={"": "src"},
    packages=find_packages(include=["src/validate_rg", "src/validate_rg.*"]),
    setup_requires=[],
    url="https://github.com/drummerzzz/pypi_validate_rg",
    version="0.0.1",
    zip_safe=False,
)
