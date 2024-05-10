import sys

# check if the user provided an input file
if len(sys.argv) < 2:
    print("Usage: python3 filter.py <input file>")
    sys.exit(1)
inputFile = sys.argv[1]
outputFile = "filtered-" + inputFile
inputLines = 0
removedLines = []
outputLines = 0

# add numbers here that you want to potentially remove.
# if a line contains one number from each of these three arrays, the line will be removed.
BA_filter_values = [2, 1]
GL_filter_values = [2, 3]
CC_filter_values = [2]

# Open the input file (read only) and output file (write only)
input = open(inputFile, "r")
output = open(outputFile, "w")

# for each line in input, check if it should be removed
for line in input:
    inputLines += 1

    # split the line into columns
    columns = line.split("|")
    # check if the line should be removed
    if (
        int(columns[0]) in BA_filter_values
        and int(columns[1]) in GL_filter_values
        and int(columns[2]) in CC_filter_values
    ):
        # track the removed line
        removedLines.append(line.replace("\n", ""))
    else:
        # append the line to the output file
        output.write(line)
        outputLines += 1

# close the files
input.close()
output.close()

# output a summary
print()
print("------------------")
print("Summary")
print("------------------")
print("Input file:", inputFile)
print("Output file:", outputFile)
print("---")
print("Lines input:", inputLines)
print("Lines output:", outputLines)
print("Lines removed:", len(removedLines))
print("---")
print("Filtered lines with the following values:")
print("BA:", BA_filter_values)
print("GL:", GL_filter_values)
print("CC:", CC_filter_values)
print("---")
print("Removed Lines:")
for line in removedLines:
    print(line)
print("------------------")
print("Done!")
print("------------------")
print()
