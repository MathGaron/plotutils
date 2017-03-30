import pandas as pd
from pandas.tools import plotting
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

if __name__ == '__main__':
    filename = "template.csv"

    df = pd.read_csv(filename)
    column_tags = df.columns.values
    df.plot(x=column_tags[0], y=[column_tags[1], column_tags[2]])
    plt.show()