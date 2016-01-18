import os
import logging


class Feature(object):

    def __init__(self, name, default, file_path):
        self.log = logging.getLogger(__name__)
        self.name = name
        self.default = default
        self.file_path = file_path

    def write(self, value):
        with open(self.file_path, 'w') as feature_file:
            feature_file.write(value)
        msg = "Written Feature {0} to {1}".format(self.name, self.file_path)
        self.log.info(msg)

    def discover(self):
        raise NotImplementedError("Feature should be subclassed and discover() overridden.")

