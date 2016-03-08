#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#Ivana Chingovska <ivana.chingovska@idiap.ch>
#Tue 10 Mar 16:07:27 CET 2015

from setuptools import setup, find_packages

# Define package version
version = open("version.txt").read().rstrip()

# The only thing we do in this file is to call the setup(
    namespace_packages=['bob'],
) function with all
# parameters that define our package.
setup(
    namespace_packages=['bob'],


    name='bob.db.msu_mfsd_mod',
    version=version,
    description='MSU Mobile Face Spoofing Database Access API for Bob, with modified protocol',
    url='http://github.com/bioidiap/bob.db.msu_mfsd_mod',
    license='GPLv3',
    author='Ivana Chingovska',
    author_email='ivana.chingovska@idiap.ch',
    long_description=open('README.rst').read(),

    # This line is required for any distutils based packaging.
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,



    install_requires=[
      'setuptools',
      'six',
      'bob.db.base',
      'antispoofing.utils',
    ],

    entry_points={

      # declare the database to bob
      'bob.db': [
        'msu_mfsd_mod = bob.db.msu_mfsd_mod.driver:Interface',
      ],

      # antispoofing database declaration
      'antispoofing.utils.db': [
        'msu_mfsd_mod = bob.db.msu_mfsd_mod.spoofing:Database',
      ],

      'console_scripts': [
        'testme.py = bob.db.msu_mfsd_mod.testme:main',
      ],
    },

    classifiers = [
      'Framework :: Bob',
      'Development Status :: 4 - Beta',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'Topic :: Database :: Front-Ends',
    ],

)
