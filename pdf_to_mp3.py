#!/usr/bin/env python3
"""Convert Italian PDF files to MP3 audiobooks using edge-tts."""

import argparse
import asyncio
import os
import sys
import tempfile

import edge_tts
from PyPDF2 import PdfReader


def extract_text(pdf_path, pages=None):
    """Extract text from PDF, optionally filtering by page range."""
    reader = PdfReader(pdf_path)
    total = len(reader.pages)

    if pages:
        start, end = pages
        start = max(0, start - 1)  # convert to 0-indexed
        end = min(total, end)
        selected = reader.pages[start:end]
    else:
        selected = reader.pages

    text = "\n".join(page.extract_text() or "" for page in selected)
    return clean_text(text)


def clean_text(text):
    """Clean up extracted PDF text for TTS."""
    lines = text.splitlines()
    cleaned = []
    for line in lines:
        line = line.strip()
        if not line:
            cleaned.append("")
            continue
        # Skip standalone page numbers
        if line.isdigit():
            continue
        cleaned.append(line)

    # Join lines, collapsing multiple blank lines
    result = "\n".join(cleaned)
    while "\n\n\n" in result:
        result = result.replace("\n\n\n", "\n\n")
    return result.strip()


def parse_pages(pages_str):
    """Parse a page range string like '1-5' into (start, end)."""
    if "-" in pages_str:
        start, end = pages_str.split("-", 1)
        return int(start), int(end)
    page = int(pages_str)
    return page, page


async def generate_audio(text, output_path, voice, rate):
    """Generate MP3 audio from text using edge-tts."""
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    await communicate.save(output_path)


def main():
    parser = argparse.ArgumentParser(description="Convert Italian PDF to MP3 audiobook")
    parser.add_argument("input", help="Input PDF file")
    parser.add_argument("output", nargs="?", help="Output MP3 file (default: input_name.mp3)")
    parser.add_argument("--voice", default="it-IT-DiegoNeural", help="TTS voice (default: it-IT-DiegoNeural)")
    parser.add_argument("--rate", default="-20%", help="Speech rate (default: -20%% for learner pace)")
    parser.add_argument("--pages", help="Page range, e.g. 1-5 or 3")
    args = parser.parse_args()

    if not os.path.isfile(args.input):
        print(f"Error: {args.input} not found", file=sys.stderr)
        sys.exit(1)

    output = args.output or os.path.splitext(args.input)[0] + ".mp3"
    pages = parse_pages(args.pages) if args.pages else None

    print(f"Extracting text from {args.input}...")
    text = extract_text(args.input, pages)

    if not text:
        print("Error: no text extracted from PDF", file=sys.stderr)
        sys.exit(1)

    print(f"Extracted {len(text)} characters")
    print(f"Generating audio with voice={args.voice}, rate={args.rate}...")

    asyncio.run(generate_audio(text, output, args.voice, args.rate))

    size_mb = os.path.getsize(output) / (1024 * 1024)
    print(f"Saved: {output} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
