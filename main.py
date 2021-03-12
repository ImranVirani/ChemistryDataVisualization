import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
fig, ax = plt.subplots()
data1 = np.array([230,202, 270])
data1 = np.roll(data1, 1)
data2 = np.array([138, 101, 189])
data2 = np.roll(data2, 1)
width = 0.3
plt.bar(np.arange(len(data1)), data1, width=width, label = 'control')
plt.bar(np.arange(len(data2))+ width, data2, width=width,label = 'experimental')
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
for axis in [ax.xaxis, ax.yaxis]:
    axis.set_major_locator(ticker.MaxNLocator(integer=True))
plt.xticks(np.arange(len(data1)), np.arange(1, len(data1)+1))
ax.set_xlabel('Trial Number')
ax.set_ylabel('Number of folds per cm$^2$')
ax.set_title('Number of Folds After Control and Experimental Trials')
ax.legend()
plt.show()

