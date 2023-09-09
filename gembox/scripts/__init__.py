"""
- ls-py.py: list files in a directory. You can use `ls-py.exe -h` to see the help message. the source code is as follow:
    def main():
        parser = argparse.ArgumentParser(description="List contents of a directory.")
        parser.add_argument('path', type=pathlib.Path, nargs='?', default='.',
                            help='Path to the directory you want to list.')
        parser.add_argument('-e', '--expand-hidden', action='store_true', default=False,
                            help='Whether to expand hidden directories, i.e. directories starting with "__" or "."')
        parser.add_argument('-x', '--exclude', nargs='*', default=None,
                            help='List of directory or file names to exclude from the output.')
        args = parser.parse_args()

        print(list_directory(args.path, expand_hidden_dir=args.expand_hidden, excluded_list=args.exclude))
"""
