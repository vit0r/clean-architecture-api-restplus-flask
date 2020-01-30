"""Setup app from setup.cfg
"""

from setuptools import find_packages, setup

setup(packages=find_packages(exclude="tests"), tests_require=["tox"])
