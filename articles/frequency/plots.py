"""
My Gold Mine: Card Frequencies

The following Python code plots the card frequencies in **My Gold Mine**.
"""
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# create data
s = pd.Series([29, 15, 5, 9], index=list("one gold,two gold,one gold/back,dragon".split(",")))

# vertical bar plot
s.plot.bar(figsize=(5, 5), color=["#4444cc", "#8888ff", "#bbbbff", "firebrick"])
plt.ylabel("card count")
plt.savefig("bar_vert.png", dpi=100)

# horizontal bar plot
s.plot.barh(figsize=(5, 5), color=["#4444cc", "#8888ff", "#bbbbff", "firebrick"])
plt.xlabel("card count")
plt.savefig("bar_horiz.png", dpi=100)

# pie chart
s.plot.pie(explode=[0, 0, 0, 0.2], autopct="%4.1f%%", figsize=(5, 5), colors=["#4444cc", "#8888ff", "#bbbbff", "firebrick"])
plt.savefig("pie.png", dpi=100)
