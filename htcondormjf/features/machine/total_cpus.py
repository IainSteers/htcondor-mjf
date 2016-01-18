import os
import htcondor
from htcondormjf.features.base import Feature


class TotalCpusFeature(Feature):

    def discover(self):
        total_cpus = htcondor.param.get('NUM_CPUS', self.default)
        self.write_feature(total_cpus)
        return total_cpus
