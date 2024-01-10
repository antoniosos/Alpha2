import argparse

parser = argparse.ArgumentParser(description='My command-line tool')
parser.add_argument('input_file', help='Path to the input file')
args = parser.parse_args()

print(f'Input file: {args.input_file}')