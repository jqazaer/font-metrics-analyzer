#!/usr/bin/env python3
"""
Font Metrological Analyzer
Extracts and compares vertical metrics, coordinate parameters, and typography flags
between Latin and Arabic font companions using FontTools.
"""

import os
import sys
from fontTools.ttLib import TTFont


def inspect_metrics(font_path: str):
    """
    Parses an OpenType/TrueType font file and extracts key vertical metrics,
    including OS/2, hhea, and head table values.
    """
    if not os.path.exists(font_path):
        print(f"[!] File not found: {font_path}")
        return None

    try:
        font = TTFont(font_path)
    except Exception as e:
        print(f"[!] Error loading font '{font_path}': {e}")
        return None

    # Retrieve core font tables
    os2 = font.get('OS/2')
    hhea = font.get('hhea')
    head = font.get('head')

    if not os2 or not hhea or not head:
        print(f"[!] Missing essential tables (OS/2, hhea, head) in '{font_path}'")
        return None

    # Check OpenType Typo Metrics flag: fsSelection bit 7 (USE_TYPO_METRICS)
    # When enabled, layout engines prioritize sTypo metrics over usWin ascent/descent
    bit_7_enabled = bool(os2.fsSelection & (1 << 7))
    fs_selection_str = "Enabled (1)" if bit_7_enabled else "Disabled (0)"

    # Compute Total Typo Budget: sTypoAscender - sTypoDescender + sTypoLineGap
    typo_total = os2.sTypoAscender - os2.sTypoDescender + os2.sTypoLineGap

    # Safe extraction of optional typographic heights
    x_height = getattr(os2, 'sxHeight', 'Undefined')
    cap_height = getattr(os2, 'sCapHeight', 'Undefined')

    # Display extracted values
    separator = "=" * 70
    print(separator)
    print(f"Font File: {os.path.basename(font_path)}")
    print(separator)
    print(f"  unitsPerEm:                 {head.unitsPerEm}")
    print(f"  hhea.ascender:              {hhea.ascender}")
    print(f"  hhea.descender:             {hhea.descender}")
    print(f"  hhea.lineGap:               {hhea.lineGap}")
    print(f"  fsSelection (bit 7):        {fs_selection_str}  [USE_TYPO_METRICS]")
    print(f"  sTypoAscender:              {os2.sTypoAscender}")
    print(f"  sTypoDescender:             {os2.sTypoDescender}")
    print(f"  sTypoLineGap:               {os2.sTypoLineGap}")
    print(f"  Typo Total (Line Budget):   {typo_total}")
    print(f"  usWinAscent (Clipping):     {os2.usWinAscent}")
    print(f"  usWinDescent (Clipping):    {os2.usWinDescent}")
    print(f"  sxHeight (x-Height):        {x_height}")
    print(f"  sCapHeight (Cap-Height):    {cap_height}")
    print(separator)
    print()

    return {
        "file": os.path.basename(font_path),
        "unitsPerEm": head.unitsPerEm,
        "hhea_ascender": hhea.ascender,
        "hhea_descender": hhea.descender,
        "hhea_lineGap": hhea.lineGap,
        "use_typo_metrics": bit_7_enabled,
        "sTypoAscender": os2.sTypoAscender,
        "sTypoDescender": os2.sTypoDescender,
        "sTypoLineGap": os2.sTypoLineGap,
        "typo_total": typo_total,
        "usWinAscent": os2.usWinAscent,
        "usWinDescent": os2.usWinDescent,
        "x_height": x_height,
        "cap_height": cap_height,
    }


def find_font(filename: str) -> str:
    """
    Search for font file in multiple standard paths:
    current directory, ./fonts/, and parent directories.
    """
    candidate_paths = [
        filename,
        os.path.join("fonts", filename),
        os.path.join(os.path.dirname(__file__), "fonts", filename),
        os.path.join(os.path.dirname(__file__), filename),
    ]
    for path in candidate_paths:
        if os.path.isfile(path):
            return path
    return filename


def main():
    """
    Main entry point. If font files are specified as CLI arguments, inspect them.
    Otherwise, default to inspecting the standard IBM Plex font companions.
    """
    if len(sys.argv) > 1:
        # Inspect fonts provided via command line arguments
        for font_arg in sys.argv[1:]:
            inspect_metrics(font_arg)
    else:
        # Default comparative inspection for IBM Plex Sans Latin & Arabic
        latin_font = find_font("IBMPlexSans-Regular.ttf")
        arabic_font = find_font("IBMPlexSansArabic-Regular.ttf")

        print("No font paths provided. Inspecting default font companions:\n")
        inspect_metrics(latin_font)
        inspect_metrics(arabic_font)


if __name__ == "__main__":
    main()