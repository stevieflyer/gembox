import pathlib
import traceback
from typing import Union, Optional

import PyPDF2
from docx import Document

from gembox.io._io import ensure_pathlib_path
from gembox.win_utils import convert_doc_to_docx


class TextReader:
    """
    TextReader is a class to read text content from any files.

    e.g.

    - .pdf (using PyPDF2)

    - .docx (using docx)

    - .doc (convert to .docx and then using docx)

    - others (just using built-in python modules)
    """

    @classmethod
    def read(cls, filepath: Union[str, pathlib.Path], max_words: Optional[int] = None) -> str:
        """
        Read text content from a file.

        :param filepath: (str | pathlib.Path) the path to the file
        :param max_words: (int) the maximum number of words to read, None for no limit
        :return: (str) the text content
        """
        # 0. parameter checks
        filepath = ensure_pathlib_path(filepath)
        if not filepath.exists():
            raise ValueError(f"File {filepath} does not exist.")
        assert max_words is None or max_words > 0, f"max_words must be None or > 0, but got {max_words}"

        # 1. analyze the file type and read the content
        suffix = filepath.suffix
        try:
            if suffix == ".pdf":
                return cls._read_pdf(filepath, max_words)
            elif suffix == ".docx":
                return cls._read_docx(filepath, max_words)
            elif suffix == ".doc":
                return cls.read_doc(convert_doc_to_docx(filepath), max_words)
            else:
                return cls.read_txt(filepath, max_words)
        except Exception as e:
            raise RuntimeError(f"Error when reading file {filepath} with suffix: {suffix}, error: {e}, "
                               f"traceback: {traceback.format_exc()}")

    @classmethod
    def _read_pdf(cls, filepath: pathlib.Path, max_words: Optional[int] = None) -> str:
        with open(filepath, "rb") as f:
            reader = PyPDF2.PdfFileReader(f)
            text = ""
            for page in range(reader.numPages):
                page_text = reader.getPage(page).extractText()
                text += page_text
                if max_words and len(text.split()) > max_words:
                    text = " ".join(text.split()[:max_words])
                    break
            return text

    @classmethod
    def _read_docx(cls, filepath: pathlib.Path, max_words: Optional[int] = None) -> str:
        doc = Document(filepath)
        full_text = []
        word_count = 0
        for para in doc.paragraphs:
            full_text.append(para.text)
            word_count += len(para.text.split())

            if max_words and word_count > max_words:
                words = " ".join(full_text).split()[:max_words]
                return " ".join(words)

        return "\n".join(full_text)

    @classmethod
    def read_doc(cls, filepath: pathlib.Path, max_words: Optional[int] = None) -> str:
        converted_path = convert_doc_to_docx(filepath)
        return cls._read_docx(converted_path, max_words)

    @classmethod
    def read_txt(cls, filepath: pathlib.Path, max_words: Optional[int] = None) -> str:
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
            if max_words:
                text = " ".join(text.split()[:max_words])
            return text


__all__ = ["TextReader"]
