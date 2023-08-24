import pathlib

import pandas as pd

from gembox.io import ensure_pathlib_path


class PandasIO:
    @staticmethod
    def read(filepath: (str, pathlib.Path), **kwargs):
        filepath = ensure_pathlib_path(filepath)
        if not filepath.exists():
            raise ValueError(f"File {filepath} does not exist.")
        suffix = filepath.suffix
        if suffix == ".csv":
            return pd.read_csv(filepath, **kwargs)
        elif suffix == ".xlsx":
            return pd.read_excel(filepath, **kwargs)
        elif suffix == ".json":
            return pd.read_json(filepath, **kwargs)
        else:
            raise ValueError(f"Unsupported file type {suffix} for {filepath}")

    @staticmethod
    def write(df: pd.DataFrame, filepath: (str, pathlib.Path), **kwargs):
        filepath = ensure_pathlib_path(filepath)
        suffix = filepath.suffix
        if suffix == ".csv":
            df.to_csv(filepath, **kwargs)
        elif suffix == ".xlsx":
            df.to_excel(filepath, **kwargs)
        elif suffix == ".json":
            df.to_json(filepath, **kwargs)
        else:
            raise ValueError(f"Unsupported file type {suffix} for {filepath}")


__all__ = ["PandasIO"]
