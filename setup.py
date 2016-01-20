#!/usr/bin/env python

from distutils.core import setup

setup(name='htcondor-mjf',
      version='0.1',
      description='HTCondor MachineJobFeatures Discovery Implementation',
      author='Iain Steers',
      author_email='iain.steers@cern.ch',
      url='https://github.com/IainSteers/htcondor-mjf',
      package_dir= {'': 'htcondormjf'},
      packages=['htcondormjf'],
     )


