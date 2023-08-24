import pathlib
import pandas as pd

from gembox.io import ensure_pathlib_path


def merge_df(parent_dir: (str, pathlib.Path), file_regexp: str = None, on: (list, None) = None):
    """
    Merge all csv files in the parent_dir into a single dataframe.

    TODO: Now, the merging is rather slow, since we first concat all files and then drop duplicates. Address this on-the-fly may be better.

    :param parent_dir: (str, pathlib.Path) The parent directory of the csv files.
    :param file_regexp: (str) The regular expression for the file names. If None, all files will be merged.
    :param on: (list) The column names to drop duplicates on. If None, no duplicates will be dropped.
    :return: (pd.DataFrame) The merged dataframe.
    """
    # 0. Parameter validation
    parent_dir = ensure_pathlib_path(parent_dir)
    if not parent_dir.is_dir() or not parent_dir.exists():
        raise ValueError(f"Invalid parent_dir {parent_dir}")

    if not isinstance(on, (type(None), list, set, tuple)):
        raise ValueError(f"Invalid on {on}, must be None or a list of column names.")

    # 1. Get all files
    file_list = list(parent_dir.glob(file_regexp)) if file_regexp else list(parent_dir.iterdir())
    if len(file_list) == 0:
        raise ValueError(f"No files found in {parent_dir} with regexp {file_regexp}")

    # 2. Merge all files
    df_list = []
    for file in file_list:
        df = pd.read_csv(file)
        df_list.append(df)

    merged_df = pd.concat(df_list, axis=0, ignore_index=True)

    # 3. Drop duplicates
    if on:
        merged_df.drop_duplicates(subset=on, keep='first', inplace=True)

    return merged_df
