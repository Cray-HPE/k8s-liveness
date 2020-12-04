# setup.py for ims-python-helper
# Copyright 2020 Hewlett Packard Enterprise Development LP
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('.version', 'r') as fh:
    version = fh.read().strip()

setuptools.setup(
    name="liveness",
    version=version,
    package_dir = {'liveness': 'src/liveness'},
    packages=['liveness'],
    install_requires=[
      'liveness',
    ],
    author="Cray Inc.",
    author_email="sps@cray.com",
    description="Library for simplifying liveness checks for python based infrastructure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://stash.us.cray.com/projects/SCMS/repos/k8s-liveness/browse",
    keywords="Cray IMS",
    classifiers=(
      "Programming Language :: Python :: 3.6",
    ),
)
