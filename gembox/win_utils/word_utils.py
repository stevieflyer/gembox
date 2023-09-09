"""
This file contains some utility functions for working with Word documents.
"""
import pathlib
from typing import Optional, Union

import win32com.client as win32
from win32com.client import constants

from gembox.io import ensure_pathlib_path


def convert_doc_to_docx(file_path: (str, pathlib.Path), output_dir: Optional[Union[str, pathlib.Path]] = None) -> pathlib.Path:
    """
    Convert a .doc file to .docx file.

    Since the .doc file is not supported by the openpyxl package, we often need to convert it to .docx file first.

    :param file_path: (str | pathlib.Path) path to the .doc file
    :param output_dir: (str | pathlib.Path) path to the output directory
    :return: (None)
    """
    # 0. parameter validation
    if output_dir is None:
        output_dir = "."
    file_path = ensure_pathlib_path(file_path)
    output_dir = ensure_pathlib_path(output_dir)

    # If the file is not a .doc file, raise an error
    if not file_path.suffix == '.doc':
        raise ValueError("The provided file is not a .doc file.")

    # make sure the file exists
    word = win32.gencache.EnsureDispatch('Word.Application')
    word.Visible = False

    # open the .doc file
    doc = word.Documents.Open(str(file_path))
    doc.Activate()

    # get the path to the .docx file
    new_file_path = output_dir / file_path.with_suffix('.docx')

    # save the .docx file
    wd_format_xml_document = constants.wdFormatXMLDocument
    doc.SaveAs2(str(new_file_path), FileFormat=wd_format_xml_document)

    doc.Close(False)
    word.Quit()

    return new_file_path
