import argparse
import os
import logging

command_list = ['help', 'start', 'config', 'exit', 'logs', 'read']
global parser
parser = argparse.ArgumentParser(description='Example with subcommands')

# Creating subparsers
global subparsers
subparsers = parser.add_subparsers(dest='command', help='Subcommands')

global compressor
global LOG_DIRECTORY
global code_mapping


def read_logs(args):
    clear_console()
    try:
        with open(LOG_DIRECTORY, 'r') as file:
            file_contents = file.read()
            print(file_contents)
    except FileNotFoundError:
        print(f"File not found: {LOG_DIRECTORY}")
    except Exception as e:
        print(f"An error occurred: {e}")
    starter_screen()


def show_help(args):
    clear_console()
    print('Available commands:')
    for command in command_list:
        print(command)
    starter_screen()


def config(args):
    clear_console()
    starter_screen()


def start_compression(args):
    clear_console()
    global code_mapping
    code_mapping = compressor.compress()
    print('successfully compressed!')
    starter_screen()


def read_compressed_file(args):
    clear_console()
    try:
        with open(compressor.compressed_file_directory, 'r') as file:
            file_contents = file.read()
            print(file_contents)
    except FileNotFoundError:
        print(f"File not found: {compressor.compressed_file_directory}")
    except Exception as e:
        print(f"An error occurred: {e}")
    print(code_mapping)
    starter_screen()


def exit_program(args):
    exit()


def start_loop(compr, log_dir):
    global compressor
    compressor = compr
    global LOG_DIRECTORY
    LOG_DIRECTORY = log_dir
    starter_screen()


def starter_screen():
    print('-----------------------------------------------------------------')
    print("if you're lost type help")
    inp = input()
    # Subparser for command1
    parser_help = subparsers.add_parser('help', help='tells you what you can do')
    parser_help.set_defaults(func=show_help)

    parser_exit = subparsers.add_parser('exit', help='stops the app')
    parser_exit.set_defaults(func=exit_program)

    parser_config = subparsers.add_parser('config', help='change your app configuration')
    parser_config.add_argument('--input', help='put here new path for a file to compress', required=False)
    parser_config.add_argument('--output', help='put here new path where compressed file should be put in',
                               required=False)
    parser_config.add_argument('--logs', help='put here new path where logs should be logged (file should end with '
                                              '.log)', required=False)
    parser_config.set_defaults(func=config)

    parser_start_compression = subparsers.add_parser('start', help='starts the compression')
    parser_start_compression.set_defaults(func=start_compression)
    parser_read_logs = subparsers.add_parser('logs', help='reads all logs')
    parser_read_logs.set_defaults(func=read_logs)

    parser_read_compressed_file = subparsers.add_parser('read', help='writes out compressed file')
    parser_read_compressed_file.set_defaults(func=read_compressed_file)

    # Parsing the command-line arguments
    args = parser.parse_args(inp.split())

    # Calling the associated function for the selected subcommand
    if hasattr(args, 'func'):
        args.func(args)


def clear_console():
    os.system('cls')
