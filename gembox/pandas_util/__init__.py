from .pd_utils import (
    merge_df,
    drop_finished,
)
'''
def merge_df(parent_dir: (str, pathlib.Path), file_regexp: str = None, on: (list, None) = None):
    """
    Merge all csv files in the parent_dir into a single dataframe.

    TODO: Now, the merging is rather slow, since we first concat all files and then drop duplicates. Address this on-the-fly may be better.

    :param parent_dir: (str, pathlib.Path) The parent directory of the csv files.
    :param file_regexp: (str) The regular expression for the file names. If None, all files will be merged.
    :param on: (list) The column names to drop duplicates on. If None, no duplicates will be dropped.
    :return: (pd.DataFrame) The merged dataframe.
    """
    pass
    
def drop_finished(tasks: pd.DataFrame, finished: pd.DataFrame, on: Collection[str]) -> pd.DataFrame:
    """
    Drop the finished tasks from the tasks dataframe.

    :param tasks: (pd.DataFrame) The tasks dataframe.
    :param finished: (pd.DataFrame) The finished tasks dataframe.
    :param on: (Collection[str]) The column names to drop duplicates on.
    :return: (pd.DataFrame) The remaining tasks dataframe.
    """
    pass
'''

