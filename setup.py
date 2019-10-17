# coding=utf-8
from setuptools import setup, find_packages
from os.path import realpath, dirname
from os import listdir


root_dir = dirname(realpath(__file__))
# data_path = '/countryinfo/data'
data_dir = root_dir+'/countryinfo/data'
# read readme file
with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()
# package data file
data_files = ['countryinfo/data/'+file for file in listdir(data_dir) if file.endswith(".json")]


setup(
    name='countryinfo',
    version='0.1.0',
    python_requires='>3.0.0',
    packages = find_packages(
        include=['countryinfo'],
        exclude='tests'
    ),
    include_package_data=True,
    test_suite="tests.Tests",
    data_files=[("data", data_files)],  # package data files
    url='https://github.com/porimol/countryinfo',
    license='MIT License',
    classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5'
    ],
    author=['Porimol Chandro'],
    author_email=['porimolchandroroy@gmail.com'],
    description='countryinfo is a python module for returning data about countries, ISO info and states/provinces within them.',
    long_description=long_description,
    keywords = ['countryinfo'],
    install_requires=[],
)
