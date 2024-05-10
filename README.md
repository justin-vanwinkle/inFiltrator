# The inFiltrator

- This application filters line out of a text file.
- The input file will remain untouched.
- A new file will be created with the filtered results.

## Get Started

To get started, download this repository and follow the instructions below.

## Configure

Open `filter.py` and update the `BA_filter_values`, `GL_filter_values`, `CC_filter_values`. If (and only if) a line in the input file contains a number from all three of these lists, that line will be removed.

## Input

Place the file you wish to filter in this directory.

## Run

Install [python3](https://www.python.org/downloads/)

Run this command:
`python3 filter.py <name of input file>`

Example Command:
`python3 filter.py example.txt`

## Output

All outputs will appear in the `output` folder.

The file named `filtered-<input filename>.txt` will contain your filtered result.

The file named `removed_lines-<input filename>.txt` will contain all deleted lines.
