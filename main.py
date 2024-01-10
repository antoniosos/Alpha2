import configparser
import os.path
from src.compressor import Compressor
import logging

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('spousteni z konzole')
    MAIN_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
    CONFIG_DIRECTORY = MAIN_DIRECTORY + '\config\Alpha2.ini'

    parser = configparser.ConfigParser()
    parser.read(CONFIG_DIRECTORY)

    LOG_DIRECTORY = parser['Paths']['log_file']
    logging.basicConfig(filename=LOG_DIRECTORY, level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    compressor = Compressor(parser['Paths']['not_compressed_text'])





