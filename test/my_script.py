# my_script.py

import argparse

def main():
    parser = argparse.ArgumentParser(description='A sample script with argparse')
    parser.add_argument('--input', help='Input file path', required=True)
    parser.add_argument('--output', help='Output file path', required=True)
    args = parser.parse_args()

    # Your script logic goes here
    print(f'Input file: {args.input}')
    print(f'Output file: {args.output}')

if __name__ == '__main__':
    main()
