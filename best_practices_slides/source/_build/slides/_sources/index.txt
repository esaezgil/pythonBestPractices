===============================
Python projects' Best Practices
===============================


.. image:: /_static/download.jpeg
    :align: center

========
Who am I
========

    Enrique Saez

    Software engineer working for Skyscanner Hotels: http://skyscanner.net/hotels


Motivation
==========

* Started in a mature Python project
* CI & CD already set up

.. image:: /_static/Picture1.png
   :scale: 50

Goal
====

* Help advanced beginners understand project structure
* Make clear to intermediate devs


Best Practices for a Python project
===================================

* Project structure
* Modules
* Packages
* PEP8
* Environment setup (virtualenv)
* Testing
* Distributing your project

Project structure
=================
+-----------------+----------+-----------------+-------------+------------------+
| project folder  | Flask    | Requests        | boto3       | pandas           |
+=================+==========+=================+=============+==================+
| docs/           | docs/    |                 |             |                  |
+-----------------+----------+-----------------+-------------+------------------+
| examples        |examples/ |                 |             |                  |
+-----------------+----------+-----------------+-------------+------------------+
| sample/core.py  | flask/   | requests/       |  boto3/     | pandas/          |
+-----------------+----------+-----------------+-------------+------------------+
| scripts/        | scripts/ |                 | scripts/    | scripts/         |
+-----------------+----------+-----------------+-------------+------------------+
| tests/          | tests/   | tests/          | tests/      |                  |
+-----------------+----------+-----------------+-------------+------------------+
| Makefile        | Makefile | Makefile        | Makefile    |   Makefile       |
+-----------------+----------+-----------------+-------------+------------------+
| setup.py        | setup.py | setup.py        | setup.py    |setup.py          |
+-----------------+----------+-----------------+-------------+------------------+
|requirements.txt | setup.cfg|requirements.txt | setup.cfg   |requirements.txt  |
+-----------------+----------+-----------------+-------------+------------------+
| tox.ini         | tox.ini  |                 |  tox.ini    |   tox.ini        |
+-----------------+----------+-----------------+-------------+------------------+

Modules
=======

- split code in different files for related data and functionality
- lowercase, _separated names for module and function names: ~~compute-area~~ compute_area

.. sourcecode:: python

  def create_square(start, stop):
      print i**2
      square(0, 10)

- square(0,10) will get run on import!

.. sourcecode:: python

  def create_square(start, stop):
      print i**2
      square(0, 10)
      if __name__ == '__main__':
          square(0, 10)

What does python do to import a module?
========================================

* Check the module registry (sys.modules)
* If the module is already imported:

    * Python uses the existing module object as is

* Otherwise:

    1. Create a new, empty module object (essentially a dictionary)
    2. Insert that module object in the sys.modules dictionary
    3. Load the module code object (if necessary, compile the module first)
    4. Execute the module code object in the new module’s namespace (isolated scope)
    5. Top-level statements in modu.py will be executed, including other imports

* It’s fairly cheap to import an already imported module: look the module name up in a dictionary.

Importing a module (II)
=======================
* Function and class definitions are stored in the module’s dictionary
* Functions, and classes will be available to the caller through the module’s namespace
* The included code is isolated in a module namespace:

    - Generally don’t have to worry about the included code having unwanted effects (overriding functions with the same name)

Packages
========

* Directory with python modules:
    - installed into ``/dist-packages/``      ``(python setup.py install)``

.. sourcecode:: python

    pack/
    pack/__init__.py
    pack/modu.py

Don't have to worry about configuring PYTHONPATH to include the source


Packages (II)
=============

.. sourcecode:: python

    pack/
    pack/__init__.py
    pack/modu.py

.. sourcecode:: python

    from pack import modu     import very.deep.module as mod

* Execute all top-level statements from __init__.py
* Execute all top-level statements from modu.py
* Any variable, function, class defined in modu.py is available in pack.modu

PEP8
====

* Four spaces (NOT a tab) for each indentation level
* Limit all lines to 80/120 characters
* Separate:
    * top level functions and class definitions with 2 blank lines
    * methods inside a class by a single blank line
    * sparingly: blank lines in functions to separate logical sections

.. sourcecode:: python

    from figures.figures.figure_patterns import FigurePatterns


    class CircleCreator(FigurePatterns, object):

        LINE_WIDTH = 5

        def __init__(self, name, area=7):
            super(CircleCreator, self).__init__(name)
            self.area = area

PEP8 (II)
=========
* Lowercase, _-separated names for module and function names: my_module
* CamelCase to name classes
* ‘_’ prefix to indicate a “private” variable/method not to be used outside the module
* blank spaces, CONSTANTS

.. sourcecode:: python

    from figures.figures.figure_patterns import FigurePatterns


    class CircleCreator(FigurePatterns, object):

        LINE_WIDTH = 5

        def _compute_area(self):
            return random.random()*10

PEP8 (III)
==========

* imports:
    * standard
    * third-party
    * local library

.. sourcecode:: python

    from collections import defaultdict
    from requests import
    from figures import figure_patterns

Testing: environment setup (virtualenv)
=======================================

- Allow Python packages to be installed in an isolated location for a particular application, rather than globally.
- Keep dependencies separated
- Isolated environments with different python versions

virtualenv
==========

.. sourcecode:: bash

    $ virtualenv venv
    $ virtualenv -p /usr/bin/python2.7 venv
    $ source venv/bin/activate
    $ deactivate
    $ pip freeze > requirements.txt (list packages and version in venv)
    $ pip install -r requirements.txt

- Creates:
    - a folder containing the necessary executables to use the packages needed by the Python project
    - a copy of pip to install other packages

testing: (unittest package)
===========================

- Mirror hierarchy:

.. sourcecode:: python

    mylib/foo/bar.py
    mylib/tests/foo/test_bar.py

.. sourcecode:: python

    from unittest import TestCase


    class TestFigures(TestCase):

        def setUp(self):
            self.circle = CircleCreator('Circle')

        def tearDown(self):
            self.circle = None

        def test_name_ok(self):
            self.assertEqual(self.circle.get_name(), 'Circle')

* assert method provided by unittest


testing: Fixtures
=================

Resources/initial conditions that a test needs to operate correctly and independently from other tests.

Functions and methods that run before and after a test

.. sourcecode:: python

    from unittest import TestCase


    class TestFigures(TestCase):

        def setUp(self):
            self.circle = CircleCreator('Circle')

        def tearDown(self):
            self.circle = None

        def test_name_ok(self):
            self.assertEqual(self.circle.get_name(), 'Circle')

testing: (nose package)
=======================

* Provides automatic test discovery
* Loads every file that starts with \test_
* Executes all functions within that start with \test_
* In maintenance mode for the past several years: use Nose2, py.test

.. sourcecode:: bash

    $ nosetest

test selection:

.. sourcecode:: bash

    $ path.to.your.module:ClassOfYourTest.test_method
    $ path.to.your.module:ClassOfYourTest
    $ path.to.your.module

py.test
=======

* Auto-discovery of test modules and functions
* Modular fixtures for managing small or parametrized long-lived test resources
* Can run unittest (including trial) and nose test suites

.. sourcecode:: bash

    $ py.test tests/

* Parametrize

http://docs.pytest.org/en/latest/fixture.html#fixture

tox
---

* Clean environment for running unit tests:
* Create virtual environment, using pip to install dependencies
* Use setup.py to install package inside virtualenv
* Automate and standardize how tests are run in Python for each environment

.. sourcecode:: yaml

    [tox]
    envlist = {py27}

    [testenv]
    deps =
        -rrequirements.txt

    commands =
        nosetests

Jargon
======

* Built Distribution
    * A Distribution format containing files and metadata
    * Only need to be moved to the correct location to be installed

* Wheel
    - A Built Distribution format supported by pip.

* setuptools
    - Collection of enhancements to the Python distutils, (includes easy_install)
    - Easily build and distribute Python distributions, especially ones that have dependencies on other packages.

Jargon (II)
===========

* Source Distribution (or “sdist”)
    * requires a build step when installed by pip
    * provides metadata and the essential source files needed for installing by a tool like pip, or for generating a Built Distribution.
    * usually generated with :code:`setup.py sdist`
    * see the bdist_wheel setuptools extension available from the wheel project to create wheels

* egg
    * a zip file with different extension

* setup.cfg
    * ini file that contains option defaults for setup.py commands.

Console scripts
===============

* Installs a tiny program in the system path to call a module’s specific function
* Launchable programs need to be installed inside a directory in the systempath

setup.py
========

.. sourcecode:: python

    from setuptools import setup, find_packages

    setup(
        name="figures",
        version="1",
        packages=find_packages(),
        entry_points={
            'console_scripts': [
                "figure_creator = figures.example_figures:main"
            ],
        },
    )

setup.py (II)
=============
.. sourcecode:: bash

    python setup.py install

will create a script like this in /bin/:

.. sourcecode:: python

    __requires__ = 'figures==1'
    import sys
    from pkg_resources import load_entry_point

    if __name__ == '__main__':
        sys.exit(
            load_entry_point('figures==1', 'console_scripts', 'figure_creator')()
        )

* scans the entry points of the figures package
* retrieves the figures key from the console_scripts category, to locate and run the corresponding function
* entry points: package.subpackage:function

entry points
============

- Part of setuptools
- Used by other python programs to dynamically discover features that a package provides
- entry_point_inspector package: lists the entry points available in a package

Requirements for Installing Packages
====================================

- pip, setuptools (for advanced installations) and wheel
- distutils for simple package installations
- Create a virtual environment
- pip

.. sourcecode:: bash

    $ pip install –r requirements.txt
    $ pip install ‘botocore=0.6.8’

Wheel
=====
* pre-built distribution format
* faster installation compared to Source Distributions (sdist), especially when a project contains compiled extensions.

* creates a .whl file in the dist directory

.. sourcecode:: bash

    python your_code.whl/wheel

Wheel (II)
==========

* supported by pip

- offers the bdist_wheel setuptools extension for creating wheel distributions.
- Additionally, it offers its own command line utility for creating and installing wheels.

- Wheel files do not require installation

.. sourcecode:: bash

	run $ python wheel-0.21.0-py2.py3-none-any.whl/wheel –h

.. sourcecode:: bash

    python setup.py bdist_wheel

Mocking
=======

* Replace parts of the project with mock objects (fake, behaviour controlled)
* Make assertions about how they have been used

Mock
====

Mock objects
Simulated objets that mimic the behaviour of real objects

References
==========

The Hitchhiker’s Guide to Python: http://docs.python-guide.org/en/latest/

Python Packaging User Guide: https://packaging.python.org/

Writing idiomatic Python: https://jeffknupp.com/

Mouse vs Python: http://www.blog.pythonlibrary.org/

Python for you and me: http://pymbook.readthedocs.io/en/latest/

BogoToBogo: http://www.bogotobogo.com/python

Python testing: http://www.pythontesting.net/


Questions:
==========



http://github.com/esaezgil/pythonbestpractices


