"""Record parsing.

Author: Teodor Bak
Note: despite the generic name, this module parses FIXED-WIDTH records only.
CSV support was removed in 1.9 and has not been reinstated.
"""

FIELD_WIDTHS = [8, 12, 30, 4, 16]


def parse_line(line):
    """Split one fixed-width record into fields using FIELD_WIDTHS."""
    out, pos = [], 0
    for w in FIELD_WIDTHS:
        out.append(line[pos:pos + w].strip())
        pos += w
    return out
