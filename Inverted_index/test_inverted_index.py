import os

import pytest

import inverted_index


def prepare_file():
    test_data = {1: "1 2 3 armavir", 7: "auf wykat auf 2", 325: "shah i mat myata"}
    test_file_name = "small_text_bundle"
    with open(test_file_name, "w") as f:
        for i, w in test_data.items():
            f.write(f"{i} {w}\n")
    return test_file_name


def test_load_documents():
    test_file_name = prepare_file()
    docs = inverted_index.load_documents(test_file_name)
    assert docs
    os.remove(test_file_name)
