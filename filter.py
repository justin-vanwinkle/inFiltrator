import sys
import os
from time import sleep
import re

# check if the user provided an input file
if len(sys.argv) < 2:
    print("Usage: python3 filter.py <input file>")
    sys.exit(1)

# ensure output dir exists
if not os.path.exists("output"):
    os.mkdir("output")

# set some variables
inputFileName = sys.argv[1]
outputFileName = "output/filtered-" + inputFileName
removedLinesFileName = "output/removed_lines-" + inputFileName
inputLinesCount = 0
outputLinesCount = 0
removedLinesCount = 0

# add numbers here that you want to filter for
# if (and only if) a line matches a number in all three arrays, it will be removed
BA_filter_values = [2, 1]
GL_filter_values = [2, 3]
CC_filter_values = [2]

# Open the input file (read only) and output file (write only)
inputFile = open(inputFileName, "r")
outputFile = open(outputFileName, "w")
removedLinesFile = open(removedLinesFileName, "w")

print("Beginning to filter", inputFileName, "...")


# with open(inputFileName, "r") as fp:
#     for count, line in enumerate(fp):
#         pass
def blocks(files, size=65536):
    while True:
        b = files.read(size)
        if not b:
            break
        yield b


with open(inputFileName, "r", encoding="utf-8", errors="ignore") as f:
    count = sum(bl.count("\n") for bl in blocks(f)) + 1
    print("Number of lines to process:", count)

print()

# for each line in input, check if it should be removed
for line in inputFile:

    sys.stdout.write("\r")
    sys.stdout.write(
        "[%-100s] %d%%"
        % (
            "=" * int(100 * inputLinesCount / (count - 1)),
            100 * inputLinesCount / (count - 1),
        )
    )
    sys.stdout.flush()

    inputLinesCount += 1

    # split the line into columns
    columns = line.split("|")

    # ensure the columns are digits
    if columns[0].isdigit():
        columns[0] = re.sub("\D", "", columns[0])
    if columns[1].isdigit():
        columns[1] = re.sub("\D", "", columns[1])
    if columns[2].isdigit():
        columns[2] = re.sub("\D", "", columns[2])

    # check if the line should be removed
    if (
        int(columns[0]) in BA_filter_values
        and int(columns[1]) in GL_filter_values
        and int(columns[2]) in CC_filter_values
    ):
        # track the removed line
        removedLinesFile.write(line)
        removedLinesCount += 1
    else:
        # append the line to the output file
        outputFile.write(line)
        outputLinesCount += 1

# close the files
inputFile.close()
outputFile.close()
removedLinesFile.close()

# output a summary
print()
print()
print("------------------")
print("Summary")
print("------------------")
print("Input file:", inputFileName)
print("Output file:", outputFileName)
print("Removed lines file:", removedLinesFileName)
print("---")
print("Lines input:", inputLinesCount)
print("Lines output:", outputLinesCount)
print("Lines removed:", removedLinesCount)
print("---")
print("Filters Used:")
print("BA:", BA_filter_values)
print("GL:", GL_filter_values)
print("CC:", CC_filter_values)
print("------------------")
print("Done!")
print("------------------")
print()
