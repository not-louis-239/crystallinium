from enum import StrEnum

class MarkdownTokenClassification(StrEnum):
    TEXT = "TEXT"
    HEADER = "HEADER"
    LIST_ITEM = "LIST_ITEM"
    CODE_INLINE = "CODE_INLINE"
    CODE_BLOCK = "CODE_BLOCK"
    LINK = "LINK"
    IMAGE = "IMAGE"
    QUOTE = "QUOTE"
    BOLD = "BOLD"
    ITALIC = "ITALIC"

class MarkdownToken:
    def __init__(self, typ: str, val: str):
        self.typ = typ
        self.val = val

def parse_markdown(text: str) -> list[MarkdownToken]:
    """Parse a markdown string into tokens and return them as a list"""
    ...
