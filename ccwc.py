#!/usr/bin/env python3
import argparse
import sys


def count_bytes(content) -> int:
    """Count the number of bytes in content."""
    if isinstance(content, str):
        return len(content.encode('utf-8'))
    return len(content)


def count_chars(content) -> int:
    """Count the number of Unicode characters in content."""
    if isinstance(content, bytes):
        return len(content.decode('utf-8', errors='replace'))
    return len(content)


def count_lines(content) -> int:
    """Count the number of lines in content."""
    if isinstance(content, bytes):
        content = content.decode('utf-8', errors='replace')
    return content.count('\n')


def count_words(content) -> int:
    """Count the number of words in content."""
    if isinstance(content, bytes):
        content = content.decode('utf-8', errors='replace')
    return len(content.split())


def read_file(filepath) -> bytes | None:
    """Read file in binary mode to count bytes accurately."""
    try:
        with open(filepath, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        print(f"ccwc: {filepath}: No such file or directory", file=sys.stderr)
        return None
    except PermissionError:
        print(f"ccwc: {filepath}: Permission denied", file=sys.stderr)
        return None


def format_output(counts, filename=None) -> str:
    """Format output like wc: 'count1 count2 count3 filename' or just 'count'."""
    if isinstance(counts, int):
        # Single count
        if filename:
            return f"{counts:8d} {filename}"
        return f"{counts:8d}"
    else:
        # Multiple counts (list/tuple)
        count_str = "".join(f"{c:8d}" for c in counts)
        if filename:
            return f"{count_str} {filename}"
        return count_str


def main() -> None:
    parser = argparse.ArgumentParser(
        prog='ccwc',
        description='Count bytes, words, and lines in files'
    )
    parser.add_argument('-c', action='store_true', help='Count bytes')
    parser.add_argument('-m', action='store_true', help='Count characters')
    parser.add_argument('-l', action='store_true', help='Count lines')
    parser.add_argument('-w', action='store_true', help='Count words')
    parser.add_argument('files', nargs='*', help='Files to process')

    args = parser.parse_args()

    # Determine which counters to use
    has_option = args.c or args.m or args.l or args.w

    if args.l:
        count_fns = [count_lines]
    elif args.m:
        count_fns = [count_chars]
    elif args.w:
        count_fns = [count_words]
    elif args.c:
        count_fns = [count_bytes]
    else:
        # No option specified: show lines, words, bytes (like wc)
        count_fns = [count_lines, count_words, count_bytes]

    results = []
    total_counts = [0] * len(count_fns)

    if not args.files:
        # Read from stdin
        content = sys.stdin.buffer.read()
        counts = tuple(fn(content) for fn in count_fns)
        results.append((counts, None))
        for i, c in enumerate(counts):
            total_counts[i] = c
    else:
        # Process each file
        for filepath in args.files:
            content = read_file(filepath)
            if content is not None:
                counts = tuple(fn(content) for fn in count_fns)
                results.append((counts, filepath))
                for i, c in enumerate(counts):
                    total_counts[i] += c

    # Display results
    for counts, filepath in results:
        print(format_output(counts, filepath))

    # Display total if multiple files
    if len(results) > 1:
        print(format_output(tuple(total_counts), 'total'))


if __name__ == '__main__':
    main()
