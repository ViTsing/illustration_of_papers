import matplotlib.pyplot as plt
import xlrd

data = xlrd.open_workbook('data/0716/pn_m1.xlsx')
sheets = ['pn', 'm']
metrics = ['recall', 'time']
sheet = sheets[1]
metric = metrics[1]

sheet_pn = data.sheets()[0]
sheet_m = data.sheets()[1]

# pn
pn = sheet_pn.col_values(0)
pn_recall = sheet_pn.col_values(1)
pn_time = sheet_pn.col_values(2)

# m
m = sheet_m.col_values(0)
m_recall = sheet_m.col_values(1)
m_time = sheet_m.col_values(2)

lines = {'pnrecall': pn_recall, 'pntime': pn_time, 'mrecall': m_recall, 'mtime': m_time}
ylims = {'pnrecall': [0.7, 0.8], 'pntime': [0.02, 0.06], 'mrecall': [0, 1], 'mtime': [0, 0.05]}
y_factors = {'pnrecall': 1.001, 'pntime': 1.005, 'mrecall': 1.01, 'mtime': 1.01}
y_labels = {'recall': 'Recall', 'time': 'Time'}
y_ticks = {'pnrecall': [0.7, 0.72, 0.74, 0.76, 0.78, 0.8], 'pntime': [0.02, 0.03, 0.04, 0.05, 0.06],
           'mrecall': [0, 0.2, 0.4, 0.6, 0.8, 1],
           'mtime': [0, 0.01, 0.02, 0.03, 0.04, 0.05]}
line = lines[sheet + metric]
index = eval(sheet)
xlim = [index[0], index[-1]]
ylim = ylims[sheet + metric]
y_factor = y_factors[sheet + metric]
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['figure.figsize'] = (10, 8)

ax = plt.subplot(1, 1, 1)
ax.grid(axis='y', linestyle=':', alpha=0.4)
ax.grid(axis='x', alpha=0)
ax.grid(zorder=1)
plt.rc('font', family='ARIAL', size=25)

plt.plot(index, line, color='red', ls='-', linewidth=2, marker='o', markersize=8)

plt.yticks(y_ticks[sheet + metric], fontsize=27)
plt.xticks(index, fontsize=27)
plt.ylim(ymin=ylim[0], ymax=ylim[1])
plt.xlim(xmin=xlim[0], xmax=xlim[1])
plt.text(xlim[0], ylim[1] * y_factor, y_labels[metric], fontsize=34)

border_width = 1
# plt.legend(loc='upper right', ncol=4, fontsize=14, facecolor='none')

ax = plt.subplot(1, 1, 1)
ax.spines['top'].set_linewidth(border_width)
ax.spines['bottom'].set_linewidth(border_width)
ax.spines['left'].set_linewidth(border_width)
ax.spines['right'].set_linewidth(border_width)
plt.subplots_adjust(top=0.92, bottom=0.06, right=0.96, left=0.10, hspace=0, wspace=0)
plt.savefig('graph/pn_m/' + metric + '_' + sheet + '.pdf', format='pdf', dpi=300)
# plt.show()
