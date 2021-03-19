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
    author="Cray/HPE Inc",
    author_email="cray-oss@hpe.com",
    description="Library for simplifying liveness checks for python based infrastructure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cray-HPE/k8s-liveness",
    download_url="https://github.com/user/reponame/archive/v_1.1.2.tar.gz",
    keywords="Cray/HPE IMS",
    classifiers=(
          'Development Status :: 5 - Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
      'Programming Language :: Python :: 3.6',
    ),
)
