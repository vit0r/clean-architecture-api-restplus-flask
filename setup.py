"""Setup app from setup.cfg
"""

from setuptools import setup, find_packages

setup(
    packages=find_packages(exclude='tests'),
    tests_require=['tox']
)
