import plotly.plotly as py
import numpy as np
import matplotlib.pyplot as plt

py.sign_in('isak.falk', 'c5db1lskr9')

mpl_fig = plt.figure()

x = np.random.randn(20)
y = np.random.randn(20)

plt.scatter(x, y)

py.plot_mpl(mpl_fig, filename="plotly_figure")
