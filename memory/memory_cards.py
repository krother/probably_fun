"""
Generate plots for the Probably Fun memory cards.

This script was extracted from the Jupyter notebook using
the program ipynb-py-convert. It should work but requires cleanup.

Instructions:

Step 1: Code Review

- run the code and see if it works (you may need to install some libraries)
- write all libraries you 
- read the code and mark what is ugly, hard to understand or what you are curious about
- stop after 1 hour
- commit the changes

Step 2: Basic cleanup

- move all imports to the top of the script
- remove the '# %%' comments
- commit the changes

Step 3: Refactor

- identify redundant code
- move it to a function (ChatGPT can help with this!)
- create one function for each plot
- if you think it is a good idea, split the code into 3-4 modules
- commit

Step 4: Polishing

- check if it still works
- run the 'black' program over the code
- add yourself to the contributors in the README
- commit
"""

# %%
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# %%
pingus = sns.load_dataset("penguins")

# %%
plt.figure(figsize=(5, 5))
plt.axes((0.0, 0.0, 1.0, 1.0))

s = pd.Series([12, 6, 4, 2], index=list("    "))
s.plot.pie(explode=[0, 0, 0, 0.2])
plt.savefig("piechart.png")

# %%
plt.figure(figsize=(5, 5))
plt.axes((0.0, 0.0, 1.0, 1.0))

pingus.groupby("species")["sex"].count().plot.bar()
plt.xlabel("")
plt.ylabel("")
plt.xticks([])
plt.yticks([])
plt.savefig("barchart.png")

# %%
flights = sns.load_dataset("flights")
plt.figure(figsize=(5, 5))
plt.axes((0.0, 0.0, 1.0, 1.0))

flights["passengers"][36:68].plot(linewidth=7)
plt.xlabel("")
plt.ylabel("")
plt.xticks([])
plt.yticks([])
plt.savefig("timeseries.png")

# %%
plt.figure(figsize=(5, 5))
plt.axes((0.0, 0.0, 1.0, 1.0))

sample = pingus.sample(100)
sns.scatterplot(data=sample, x="bill_length_mm", y="bill_depth_mm", hue="species", s=300, legend=False)
plt.xlabel("")
plt.ylabel("")
plt.xticks([])
plt.yticks([])
plt.savefig("scatter.png")

# %%
ti = sns.load_dataset("titanic")["age"].dropna()
#g = np.random.normal(loc=0.0, scale=1.0, size=1_000)
#s = pd.Series(g)
#s = s[(s > -4) & (s < 4)]
plt.figure(figsize=(5, 5))
plt.axes((0.0, 0.0, 1.0, 1.0))

sns.histplot(data=ti, bins=12)
plt.xlabel("")
plt.ylabel("")
plt.xticks([])
plt.yticks([])
plt.savefig("histo.png")

# %%
plt.figure(figsize=(5, 5))
plt.axes((0.0, 0.0, 1.0, 1.0))

p = pingus.iloc[-125:].copy()
p.loc[219, "body_mass_g"] = 4400
p.loc[219, "bill_depth_mm"] = 16.5
sns.scatterplot(data=p, x="body_mass_g", y="bill_depth_mm", hue="species", s=400, legend=False)
plt.xlabel("")
plt.ylabel("")
plt.xticks([])
plt.yticks([])
plt.savefig("outlier.png")

# %%
num = pingus.iloc[:,2:].copy().dropna()
num ["sex"] = (num["sex"] == "Male").astype(int)
cm = num.corr().abs()
plt.figure(figsize=(5, 5))
plt.axes((0.0, 0.0, 1.0, 1.0))

sns.heatmap(cm, cbar=False, cmap="viridis")
plt.xlabel("")
plt.ylabel("")
plt.xticks([])
plt.yticks([])
plt.savefig("heatmap.png")

# %%
plt.figure(figsize=(5, 5))
plt.axes((0.0, 0.0, 1.0, 1.0))

sns.boxplot(data=pingus, y="flipper_length_mm", hue="species", gap=0.1, showfliers=False, legend=False, linewidth=3)
plt.xlabel("")
plt.ylabel("")
plt.xticks([])
plt.yticks([])
plt.savefig("boxplot.png")

# %%
plt.figure(figsize=(5, 5))
plt.axes((0.0, 0.0, 1.0, 1.0))

p = pingus.iloc[:100].copy()
p["sample"] = "a"
sample = p.sample(10)
p.loc[sample.index.values, "sample"] = "b"
p.sort_values(by="sample", inplace=True)
sns.scatterplot(data=p, x="body_mass_g", y="bill_depth_mm", hue="sample", s=400, legend=False)
plt.xlabel("")
plt.ylabel("")
plt.xticks([])
plt.yticks([])
plt.savefig("sample.png")

# %%


# %%
n=5.0
x = np.linspace(-n, n, 1000, np.float32)
y = 1 / (1 + np.exp(-x))
x = list(x) + [n, -n]
y = list(y) + [0.0, 0.0]

plt.figure(figsize=(5, 5))
plt.axes((0.0, 0.0, 1.0, 1.0))

plt.plot(x, y, "k")
plt.fill(x, y, "g")
plt.plot([0.0],  [0.5], "ko", markersize=10)
plt.plot([-n, n], [1.0, 1.0], "k-")

plt.xlabel("")
plt.ylabel("")
plt.xticks([])
plt.yticks([])
plt.axis([-n, n, 0.0, 1.0])
plt.savefig("logreg.png")

# %%
x = np.linspace(0, 4, 1000, np.float32)
y = np.exp(x)
x = [0.0] + list(x) + [4, 0]
y = [0.0] + list(y) + [0.0, 0.0]

plt.figure(figsize=(5, 5))
plt.axes((0.0, 0.0, 1.0, 1.0))

plt.plot(x, y, "k")
plt.fill(x, y, "g")

plt.xlabel("")
plt.ylabel("")
plt.xticks([])
plt.yticks([])
plt.axis([0.7, 4.0, 0.0, max(y)-10])
plt.savefig("expo.png")

# %%
xmin, xmax = -4, 4
x = np.linspace(xmin, xmax, 1000, np.float32)

y = 2 / np.sqrt((2 * np.pi)) * np.exp(-x**2/2)

x = [xmin] + list(x) + [xmax, xmin]
y = [0.0] + list(y) + [0.0, 0.0]

plt.figure(figsize=(5, 5))
plt.axes((0.0, 0.0, 1.0, 1.0))

plt.plot(x, y, "k")
plt.fill(x, y, "red")

plt.xlabel("")
plt.ylabel("")
plt.xticks([])
plt.yticks([])
plt.axis([xmin, xmax, 0.0, 1.1])
plt.savefig("normal.png")

# %%
from scipy.stats import skewnorm

# %%
xmin, xmax = -4, 1
alpha = -2.5
x = np.linspace(xmin, xmax, 1000, np.float32)

y = skewnorm.pdf(x, alpha)

x = [xmin] + list(x) + [xmax, xmin]
y = [0.0] + list(y) + [0.0, 0.0]

plt.figure(figsize=(5, 5))
plt.axes((0.0, 0.0, 1.0, 1.0))

plt.plot(x, y, "k")
plt.fill(x, y, "red")

plt.xlabel("")
plt.ylabel("")
plt.xticks([])
plt.yticks([])
plt.axis([xmin, xmax, 0.0, 1.1])
plt.savefig("skew.png")

# %%
xmin, xmax = -4, 4
x = np.linspace(xmin, xmax, 1000, np.float32)

y = 2 / np.sqrt((2 * np.pi)) * np.exp(-x**2/2)

xcut = [xmin] + list(x)[:600] + [x[600]]
ycut = [0.0] + list(y)[:600] + [0.0]

plt.figure(figsize=(5, 5))
plt.axes((0.0, 0.0, 1.0, 1.0))

plt.plot(list(x) + [-4], list(y) + [0.0], "k")
plt.fill(xcut, ycut, "red")

plt.xlabel("")
plt.ylabel("")
plt.xticks([])
plt.yticks([])
plt.axis([xmin, xmax, 0.0, 1.1])
plt.savefig("normal_interval.png")

# %%
rolls = np.random.randint(1, 7, size=(2, 100000)).sum(axis=0)
s = pd.Series(rolls)
plt.figure(figsize=(5, 5))
plt.axes((0.0, 0.0, 1.0, 1.0))

sns.histplot(data=s, bins=11, color="blueviolet")
plt.xlabel("")
plt.ylabel("")
plt.xticks([])
plt.yticks([])
plt.savefig("triangular.png")

# %%
from sklearn.linear_model import LinearRegression

# %%
adechin = pingus[pingus["species"]!="Gentoo"].dropna().sample(20)
X = adechin[["bill_depth_mm"]]
y = adechin["body_mass_g"]
m = LinearRegression().fit(X, y)
slope, intercept = m.coef_[0], m.intercept_

plt.figure(figsize=(5, 5))
plt.axes((0.0, 0.0, 1.0, 1.0))

sns.scatterplot(data=adechin, x="bill_depth_mm", y="body_mass_g", color="blueviolet", legend=False, s=400)
xmin,  xmax = X.min()[0] - 1, X.max()[0] + 1
plt.plot([xmin, xmax], [slope * xmin + intercept, slope * xmax + intercept], "k-", linewidth=3)
plt.xlabel("")
plt.ylabel("")
plt.xticks([])
plt.yticks([])
plt.savefig("linreg.png")

# %%
