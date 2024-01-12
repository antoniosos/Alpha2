import logging
import os.path
import re
from collections import Counter


class Compressor:

    def __init__(self, file_directory, compressed_file_directory):
        self.file_directory = self.set_file_directory(file_directory)
        self.compressed_file_directory = self.set_directory(compressed_file_directory)

    def set_file_directory(self, file_directory):

        if not os.path.isfile(file_directory):
            logging.warning(f'{file_directory} path is not valid')
            raise FileNotFoundError()
        logging.info("valid path set")
        return file_directory

    def set_directory(self, directory):

        # add handling for non-valid arguments
        if not os.path.isdir(directory):
            logging.warning(f'{directory} directory is not valid')
            raise FileNotFoundError()
        logging.info("valid directory set")
        return directory + '\compressed_text.txt'

    def read_file_content(self):
        try:
            with open(self.file_directory, 'r') as file:
                content = file.read()
                logging.info(f'Read content from {self.file_directory}')
                return content
        except FileNotFoundError:
            logging.warning(f'File not found: {self.file_directory}')
            raise

    def to_pascal_case(self, text):
        # Pattern to match words
        pattern = r'\b\w+\b'

        # Function to capitalize the first letter of each word
        def capitalize(match):
            return match.group(0).capitalize()
        pascal_case_text = re.sub(pattern, capitalize, text)

        return pascal_case_text

    def replace_with_codes(self, text):

        words = re.findall(r'\b\w{6,}\b', text)
        word_counts = Counter(words)
        most_common_words = [word for word, _ in word_counts.most_common(5)]

        # Create a dictionary to map each most common word to a unique code
        code_mapping = {word: f"00{i}" for i, word in enumerate(most_common_words, 1)}

        # Replace the most common words with their codes
        replaced_text = re.sub(r'\b(' + '|'.join(re.escape(word) for word in most_common_words) + r')\b',
                               lambda match: code_mapping.get(match.group(0)),
                               text)

        return replaced_text, code_mapping
    def compress(self):
        logging.info('attempted compress file')
        content = self.read_file_content()
        pattern = r' '
        content = self.to_pascal_case(content)

        content, code_mapping = self.replace_with_codes(content)

        content = re.sub(pattern, '', content)
        try:
            with open(self.compressed_file_directory, 'w') as file:
                file.write(content)
                logging.info('file compressed successfully')
                logging.info(f'used file path: {self.compressed_file_directory}')
        except FileNotFoundError:
            logging.warning(f'file not found {self.compressed_file_directory}')

        return code_mapping

