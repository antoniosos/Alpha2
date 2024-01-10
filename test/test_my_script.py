# test_my_script.py

import unittest
from unittest.mock import patch
from io import StringIO
import my_script

class TestMyScriptCLI(unittest.TestCase):

    @patch('sys.argv', ['my_script.py', '--input', 'input.txt', '--output', 'output.txt'])
    def test_command_line_arguments(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            my_script.main()
            output = mock_stdout.getvalue().strip()

        self.assertEqual(output, 'Input file: input.txt\nOutput file: output.txt')

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
