import logging
import os.path
from pathlib import Path


class Compressor:

    def __init__(self, file_directory):
        self.file_directory = self.set_file_directory(file_directory)


    def set_file_directory(self, file_directory):

        # add handling for non-valid arguments
        if not os.path.isfile(file_directory):
            logging.warning('text to be compressed directory is not valid')
            raise Exception("non valid path")
        logging.info("valid directory set")
        return file_directory

    def compress(self):
        pass

