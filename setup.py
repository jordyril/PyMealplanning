"""
Created on Sun Mar 14 15:30:00 2021

@author: Jordy Rillaerts
"""

"""PyMealPlanning package setup script

   To create a source distribution of the PyMealPlanning
   package run

   python PyMealPlanning.py sdist

   which will create an archive file in the 'dist' subdirectory.
   The archive file will be  called 'PyMealPlanning-1.0.zip' and will
   unpack into a directory 'PyMealPlanning-1.0'.

   An end-user wishing to install the PyMealPlanning package can simply
   unpack 'PyMealPlanning-1.0.zip' and from the 'PyMealPlanning-1.0' directory and
   run

   python setup.py install

   which will ultimately copy the PyMealPlanning package to the appropriate
   directory for 3rd party modules in their Python installation
   (somewhere like 'c:\python27\libs\site-packages').

   To create an executable installer use the bdist_wininst command

   python setup.py bdist_wininst

   which will create an executable installer, 'PyMealPlanning-1.0.win32.exe',
   in the current directory.

"""

from setuptools import setup

# package naming
DISTNAME = "PyMealPlanning"

# descriptions
DESCRIPTION = "'PyMealPlanning' package version"
LONG_DESCRIPTION = "'PyMealPlanning' package and extensions\n"

# developer(s)
AUTHOR = "Jordy Rillaerts"
EMAIL = "jordy_rillaerts13@hotmail.com"

# versioning
MAJOR = 0
MINOR = 1
MICRO = 0
ISRELEASED = False
VERSION = "%d.%d.%d" % (MAJOR, MINOR, MICRO)
QUALIFIER = ""

FULLVERSION = VERSION
write_version = True

# if not ISRELEASED:
# FULLVERSION += '.dev'

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Operating System :: OS Independent",
    "Intended Audience :: Jordy Rillaerts",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Topic :: Support",
]

DEPENDENCIES = ["pandas", "pylatex"]

setup(
    name=DISTNAME,
    version=FULLVERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    maintainer=AUTHOR,
    maintainer_email=EMAIL,
    # setup_requires=DEPENDENCIES,
    install_requires=DEPENDENCIES,
    long_description=LONG_DESCRIPTION,
    packages=["PyMealPlanning"],
)
