import re
import pathlib
from typing import List, Union


def ensure_pathlib_path(path: Union[pathlib.Path, str]) -> pathlib.Path:
    """
    Ensure the path is a pathlib.Path object

    :param path: (str or pathlib.Path) the path
    :return: (pathlib.Path) the path
    """
    if not isinstance(path, pathlib.Path):
        path = pathlib.Path(path)
    return path


def check_and_make_dir(dir_path: Union[str, pathlib.Path]) -> pathlib.Path:
    """
    Check if the directory exists, if not, create it

    :param dir_path: (str or pathlib.Path) the path to the directory
    :return: (pathlib.Path) the path to the directory
    """
    dir_path = ensure_pathlib_path(dir_path)
    # check whether the path is a directory
    if not dir_path.exists():
        dir_path.mkdir(parents=True, exist_ok=True)
    else:
        # already exists, check whether it is a directory
        if not dir_path.is_dir():
            raise ValueError(f"Path {dir_path} is not a directory")
    return dir_path


def list_dir(dir_path: Union[str, pathlib.Path], file_only: bool = False, dir_only: bool = False, regexp: str = None) -> List[pathlib.Path]:
    """
    List out all filepath under a directory

    :param dir_path: (str | pathlib.Path) the path to the directory
    :param file_only: (bool) whether to list out only files
    :param dir_only: (bool) whether to list out only directories
    :param regexp: (str) the regular expression to filter the file/directory name
    :return: (List[pathlib.Path]) the list of filepaths
    """
    if file_only and dir_only:
        raise ValueError("file_only and dir_only cannot be both True")
    dir_path = ensure_pathlib_path(dir_path)
    if not dir_path.is_dir():
        raise ValueError(f"Path {dir_path} is not a directory")
    if regexp is not None:
        regexp = re.compile(regexp)
    if file_only:
        return [x for x in dir_path.iterdir() if x.is_file() and (regexp is None or regexp.search(x.name))]
    elif dir_only:
        return [x for x in dir_path.iterdir() if x.is_dir() and (regexp is None or regexp.search(x.name))]
    else:
        return [x for x in dir_path.iterdir() if (regexp is None or regexp.search(x.name))]


__all__ = ["ensure_pathlib_path", "check_and_make_dir", "list_dir"]
