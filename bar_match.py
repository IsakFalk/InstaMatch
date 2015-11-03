#bar plot for the online instamatch app

import plotly.plotly as py
import numpy as np
import matplotlib.pyplot as plt

def generate_bar_plot(x, y, name1, name2):

  N = 2
  ind = np.arange(N)

  feel_perc = 53
  interest_perc = 86

  heights = [feel_perc, interest_perc]
  width = 0.40

  fig = plt.figure()
  ax = fig.add_subplot(111)
  #plt.title('Compatibility')
  ax.set_xlim(0.0, 1.1)
  ax.set_ylim(0.0, 100.0)
  ax.set_xticks([0.2, 0.6])
  ax.set_xticklabels(('emotion', 'interests'))
  ax.get_xaxis().set_visible(False)
  ax.get_yaxis().set_visible(False)
  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)
  ax.spines['bottom'].set_visible(False)
  ax.spines['left'].set_visible(False)
  ax.text(0.1 + width*0.5, 1.05*heights[0], "emotional %d %%"%feel_perc, weight='bold', size='large', color='#FF9191', ha='center')
  ax.text(0.6 + width*0.5, 1.05*heights[1], "interests %d %%"%interest_perc, weight='bold', size='large', color='#FF9191', ha='center')

  bars1 = ax.bar([0.1, 0.6], [feel_perc, interest_perc], width, color='#FF9191', edgecolor='none')

  plt.savefig('%s_%s' % (str(name1), str(name2)), bbox_inches='tight')
