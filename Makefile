#
# MIT License
#
# (C) Copyright 2019-2022, 2024 Hewlett Packard Enterprise Development LP
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# If you wish to perform a local build, you will need to clone or copy the contents of the
# cms-meta-tools repo to ./cms_meta_tools

NAME ?= cray-k8s-liveness

all : runbuildprep lint pymod
pymod: pymod_prepare pymod_build pymod_test

runbuildprep:
		./cms_meta_tools/scripts/runBuildPrep.sh

lint:
		./cms_meta_tools/scripts/runLint.sh

pymod_prepare:
		python3 --version
		python3 -m pip install --upgrade pip --user -c constraints.txt
		python3 -m pip install --upgrade setuptools build wheel --user -c constraints.txt

pymod_build:
		python3 -m build --sdist
		python3 -m build --wheel

pymod_test:
		python3 -m pip install -r requirements.txt --user --no-warn-script-location
		python3 -m pip install -r requirements-test.txt --user --no-warn-script-location
		python3 -m pip install dist/*.whl --user -c constraints.txt
		python3 tests/test_liveness.py
		python3 -m pycodestyle --config=.pycodestyle ./src/liveness || true
		python3 -m pylint ./src/liveness || true
