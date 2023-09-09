import pathlib
import argparse
from typing import Union, Optional

from gembox.io import ensure_pathlib_path, list_dir


def is_hidden_dir(d: Union[str, pathlib.Path]) -> bool:
    """
    Check whether the directory is hidden, i.e. starting with '__' or '.'.

    :param d: (str | pathlib.Path) the directory
    :return: (bool) whether the directory is hidden
    """
    d = ensure_pathlib_path(d)
    return d.name.startswith("__") or d.name.startswith(".")


def list_directory(d: Union[str, pathlib.Path],
                   indent_level: int = 0,
                   expand_hidden_dir: bool = False,
                   recursive: bool = False,
                   excluded_list: Optional[list[str]] = None) -> str:
    """
    Print all items under the directory `d`.

    :param d: (str | pathlib.Path) the directory
    :param indent_level: (int) the indent level
    :param expand_hidden_dir: (bool) whether to expand hidden directories, i.e. directories starting with '__' or '.'
    :param recursive: (bool) whether to list recursively
    :param excluded_list: (list[str]) a list of excluded items
    :return: (str) the string representation of the items under the directory
    """
    # 0. Parameter validation
    ret = ""
    d = ensure_pathlib_path(d)
    if not d.is_dir():
        raise ValueError(f"{d} is not a directory.")
    if not d.exists():
        return ret
    assert isinstance(indent_level,
                      int) and indent_level >= 0, f"indent_level should be a non-negative integer, got {indent_level}."

    # 1. Get all items under the directory
    child_paths = list_dir(d)
    for child_path in child_paths:
        if child_path.is_dir():
            if excluded_list is not None and child_path.name in excluded_list:
                continue
            ret += f"{'    ' * indent_level}- {child_path.name}/\n"
            # recursive for 非隐藏文件夹
            if recursive and (not is_hidden_dir(child_path) or (expand_hidden_dir and is_hidden_dir(child_path))):
                ret += list_directory(child_path, indent_level + 1, expand_hidden_dir=expand_hidden_dir, excluded_list=excluded_list, recursive=recursive)
        else:
            ret += f"{'    ' * indent_level}- {child_path.name}\n"
    return ret


def main():
    parser = argparse.ArgumentParser(description="List contents of a directory.")
    parser.add_argument('path', type=pathlib.Path, nargs='?', default='.',
                        help='Path to the directory you want to list.')
    parser.add_argument('-e', '--expand-hidden', action='store_true', default=False,
                        help='Whether to expand hidden directories, i.e. directories starting with "__" or "."')
    parser.add_argument('-x', '--exclude', nargs='*', default=None,
                        help='List of directory or file names to exclude from the output.')
    parser.add_argument('-r', '--recursive', action='store_true', default=False, help='Whether to list recursively.')
    args = parser.parse_args()

    print(list_directory(args.path, expand_hidden_dir=args.expand_hidden, excluded_list=args.exclude, recursive=args.recursive))
