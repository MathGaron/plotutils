import pandas as pd
import os

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def file2pandas(path):
    with open(path) as file:
        # remove all spaces and enter from the first file line
        header = [x.replace("\n", "") for x in file.readline().split(" ") if x != ""]
        all_lines = []
        for line in file:
            # for each line, remove spaces and convert to float
            line = [float(x) for x in line.split(" ") if is_number(x)]
            all_lines.append(line)

    # convert the list of lines to list of columns
    data = list(zip(*all_lines))
    # convert list of columns to dict with header as tags
    data_dict = {}
    for i, title in enumerate(header):
        data_dict[title] = data[i]

    return pd.DataFrame(data_dict)

if __name__ == '__main__':

    filename = "Sensor AH44020-2016-12-07-14-00-23-992.txt"
    filepath = os.path.join("files", filename)
    dataframe = file2pandas(filepath)
    dataframe.to_csv(filepath.split(".")[0] + ".csv")
