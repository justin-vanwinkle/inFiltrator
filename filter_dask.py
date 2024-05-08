import dask.dataframe as dd

inputFile = "input.txt"
outputFile = "output.txt"

# ensure the output file is empty before we start processing input

# read the input file with dask
df = dd.read_csv(inputFile, sep="|", header=None, blocksize="256MB")
input_lines = df.shape[0].compute()

# add numbers here that you want to potentially remove.
# if a line contains one number from each of these three arrays, the line will be removed.
col1_filter_values = [2, 1]
col2_filter_values = [2, 3]
col3_filter_values = [2]


# filter
df = df[
    (df[0].isin(col1_filter_values))
    & (df[0].isin(col2_filter_values))
    & (df[0].isin(col3_filter_values))
]

output_lines = df.shape[0].compute()

print("Lines removed:", input_lines - output_lines)

df.to_csv(outputFile, sep="|", header=False, index=False, single_file=True)
