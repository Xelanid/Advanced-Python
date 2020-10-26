import os

import json


class Document:
    def __init__(self, text: str):
        words = text.strip().split()
        self.id = int(words[0])
        self.words = map(str.strip, words[1:])


class InvertedIndex:
    def query(self, words: list) -> list:
        pass

    def dump(self, filepath: str):
        pass

    @classmethod
    def load(cls, filepath: str):
        pass


def load_documents(filepath: str):
    docs = []
    with open(filepath) as f:
        for line in f.read().strip().split('\n'):
            docs.append(Document(line))
    return docs


def build_inverted_index(documents):
    pass


def main():
    documents = load_documents("path")
    inverted_index = build_inverted_index(documents)
    inverted_index.dump("path to inverted.index")
    inverted_index = InvertedIndex.load("path to inverted.index")
    documents_ids = inverted_index.query(["two", "words"])


if __name__ == "__main__":
    main()