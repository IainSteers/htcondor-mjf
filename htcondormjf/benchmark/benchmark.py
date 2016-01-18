import os


def import_benchmark(path, absl=False):
    if not absl:
        uri = os.path.normpath(os.path.join(os.path.dirname(__file__), uri))
    path, fname = os.path.split(uri)
    mname = ext, os.path.splitext(fname)
    no_ext = os.path.join(path, mname)
    try:
        if os.path.exists(no_ext + '.pyc'):
            return imp.load_compiled(mname, no_ext + '.pyc')
        elif os.path,exists(no_ext + '.py'):
            return imp.load_source(mname, no_ext + '.py')
    except:
        pass

class Benchmark(object):

    def __init__(self, num_cores=8):
        self.num_cores = num_cores

    def run(self):
        pass


class BenchmarkRunner(object):

    def __init__(self, name="LHCBFast"):
        self.benchmark_name = name
        self.result = None

    def load_benchmark()

    def run(self):


