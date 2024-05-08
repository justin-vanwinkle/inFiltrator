# importing pandas as pd
import pandas as pd

chunksize = 10**6
inputFile = "input.txt"
outputFile = "output.txt"
total_lines_removed = 0

# add numbers here that you want to potentially remove.
# if a line contains one number from each of these three arrays, the line will be removed.
col1_filter_values = [2, 1]
col2_filter_values = [2, 3]
col3_filter_values = [2]


# function to process the chunk
def process(chunk):
    global total_lines_removed

    filtered_chunk = chunk[
        # filter criteria 1 (first column)
        (chunk[0].isin(col1_filter_values))
        &
        # filter criteria 2 (second column)
        (chunk[1].isin(col2_filter_values))
        &
        # filter criteria 3 (third column)
        (chunk[2].isin(col3_filter_values))
    ]

    # append the filtered chunk to the output file
    with open(outputFile, "a") as f:
        filtered_chunk.to_csv(f, sep="|", header=False, index=False)

    # calculate the number of removed lines
    lines_removed = chunk.shape[0] - filtered_chunk.shape[0]
    total_lines_removed += lines_removed
    print("A chunk removed", lines_removed, "lines.")


# ensure the output file is empty before we start processing input
open(outputFile, "w").close()

# read the input file in chunks and process each chunk
with pd.read_csv(inputFile, chunksize=chunksize, sep="|", header=None) as reader:
    for chunk in reader:
        process(chunk)

print("Total lines removed:", total_lines_removed)
