import pathlib


def ensure_pathlib_path(path):
    """
    Ensure the path is a pathlib.Path object

    :param path: (str or pathlib.Path) the path
    :return: (pathlib.Path) the path
    """
    if path is None:
        return None
    if not isinstance(path, pathlib.Path):
        path = pathlib.Path(path)
    return path


def check_and_make_dir(dir_path):
    """
    Check if the directory exists, if not, create it

    :param dir_path: (str or pathlib.Path) the path to the directory
    :return: (pathlib.Path) the path to the directory
    """
    dir_path = ensure_pathlib_path(dir_path)
    if not dir_path.exists():
        dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path
