import os


class HTCondorMachineFeatures(object):

    def __init__(self):
        self.machine_features = {}

    def discover_features(self):
        return htcondor.params.get('NUM_CPUS')

    def output_classad(self, 
