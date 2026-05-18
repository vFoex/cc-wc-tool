# ccwc - Coding Challenge wc Tool

## Overview

This project is an implementation of the `wc` (word count) command-line tool from Unix/Linux, created as a solution to the **Coding Challenges wc Tool** challenge.

The goal was to build a Python-based tool that replicates the functionality of the standard `wc` command, starting with basic byte counting and gradually expanding to support multiple options.

## Features

- **Byte counting** (`-c`): Count the number of bytes in a file or from stdin
- **Character counting** (`-m`): Count Unicode characters
- **Line counting** (`-l`): Count the number of lines
- **Word counting** (`-w`): Count the number of words
- **Default behavior**: When no option is specified, displays lines, words, and bytes (like standard `wc`)
- **Multiple file support**: Process multiple files and display totals
- **stdin support**: Read from standard input when no files are provided

## Installation

No external dependencies required. Just ensure you have Python 3.9+ installed.

```bash
# Clone or download the repository
cd cc-wc-tool

# Make the script executable (optional)
chmod +x ccwc.py
```

## Usage

### Basic usage (displays lines, words, bytes)

```bash
python3 ccwc.py file.txt
```

Output:
```
       3       10      45 file.txt
```

### Count only bytes

```bash
python3 ccwc.py -c file.txt
```

### Count only lines

```bash
python3 ccwc.py -l file.txt
```

### Count only words

```bash
python3 ccwc.py -w file.txt
```

### Count only characters

```bash
python3 ccwc.py -m file.txt
```

### Process multiple files

```bash
python3 ccwc.py -c file1.txt file2.txt file3.txt
```

Output includes a total line:
```
      45 file1.txt
      78 file2.txt
      32 file3.txt
     155 total
```

### Read from stdin

```bash
cat file.txt | python3 ccwc.py -c
```

Or:

```bash
echo "Hello, World!" | python3 ccwc.py
```

## Examples

### Using test files

The `test/` directory contains several test files for development and testing:

- `test/empty.txt` - Empty file (edge case)
- `test/single_line.txt` - Single line of text
- `test/multiple_lines.txt` - Multiple lines
- `test/with_numbers.txt` - Lines with numbers
- `test/special_chars.txt` - Special characters, accents, and emojis
- `test/long_line.txt` - Long single line

```bash
# Test byte counting
python3 ccwc.py -c test/single_line.txt

# Test with multiple files
python3 ccwc.py test/*.txt

# Compare with system wc
wc test/single_line.txt
python3 ccwc.py test/single_line.txt
```

## Output Format

The tool follows the standard `wc` output format:

```
[count1] [count2] [count3] [filename]
```

- Each count is right-aligned in an 8-character field
- Multiple counts are separated by spaces
- When no filename is provided (stdin), only counts are shown
- When processing multiple files, a "total" line is added

## Implementation Details

### Architecture

The tool is built with:

- **argparse**: For command-line argument parsing
- **Multiple counter functions**: Separate functions for each counting type
- **Binary file reading**: Files are read in binary mode for accurate byte counting
- **UTF-8 encoding support**: Proper handling of Unicode characters and special characters

### Functions

- `count_bytes(content)` - Count bytes in content
- `count_chars(content)` - Count Unicode characters
- `count_lines(content)` - Count newline characters
- `count_words(content)` - Count whitespace-separated words
- `read_file(filepath)` - Safe file reading with error handling
- `format_output(counts, filename)` - Format results for display
- `main()` - Main entry point with argument parsing and orchestration

## Error Handling

The tool handles common error cases:

- **File not found**: Displays error message and continues with other files
- **Permission denied**: Displays error message and continues with other files
- **Invalid UTF-8**: Uses error replacement character (U+FFFD) for malformed sequences

## Testing

You can verify the implementation by comparing output with the system `wc`:

```bash
# Compare byte counting
wc -c test/single_line.txt
python3 ccwc.py -c test/single_line.txt

# Compare word counting
wc -w test/multiple_lines.txt
python3 ccwc.py -w test/multiple_lines.txt

# Compare default output
wc test/single_line.txt
python3 ccwc.py test/single_line.txt
```

## Development

This is a progressive implementation that started with `-c` support and was gradually expanded to include `-m`, `-l`, and `-w` options.

## Future Enhancements

Potential improvements could include:
- Combined options support (`-lw` to show both lines and words)
- File globbing patterns
- Performance optimizations for very large files
- Additional statistical information

## License

This project is created for educational purposes as part of a coding challenge.
