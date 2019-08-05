import matplotlib.pyplot as plt
import numpy as np
import xlrd

file_names = ['mnist_knn', 'nus_knn', 'trevi_knn', 'deep_knn']
file_save_name = {'mnist_knn': 'mnist', 'nus_knn': 'nus', 'trevi_knn': 'trevi', 'deep_knn': 'Deep1m'}
metrics = ['time', 'recall', 'ratio']

y_labels = {'recall': 'Recall', 'ratio': 'Ratio', 'time': 'Time'}
y_factors = {'mnist_knntime': 1.01, 'mnist_knnrecall': 1.001, 'mnist_knnratio': 1.0001,
             'nus_knntime': 1.001, 'nus_knnrecall': 1.01, 'nus_knnratio': 1.0005,
             'trevi_knntime': 1.01, 'trevi_knnrecall': 1.001, 'trevi_knnratio': 1.0001,
             'deep_knntime': 1.01, 'deep_knnrecall': 1.01, 'deep_knnratio': 1.0005}
xlims = {'fixed': [1, 100]}
ylims = {'mnist_knntime': [0.01, 0.0225], 'mnist_knnrecall': [0.75, 1], 'mnist_knnratio': [1, 1.02],
         'nus_knntime': [0.09, 0.115],
         'nus_knnrecall': [0, 1], 'nus_knnratio': [1, 1.05], 'trevi_knntime': [0, 0.3], 'trevi_knnrecall': [0.75, 1],
         'trevi_knnratio': [1, 1.008], 'deep_knntime': [0.1, 0.4], 'deep_knnrecall': [0.35, 1],
         'deep_knnratio': [1, 1.05]}

file_name = file_names[0]
metric = metrics[0]

mnist_knn_data = xlrd.open_workbook('data/0716/knn/' + file_name + '.xlsx')

sheet_time = mnist_knn_data.sheets()[0]
sheet_recall = mnist_knn_data.sheets()[1]
sheet_ratio = mnist_knn_data.sheets()[2]

# time data
time_SRS = sheet_time.col_values(0)
time_QALSH = sheet_time.col_values(1)
time_Multi = sheet_time.col_values(2)
time_PM = sheet_time.col_values(3)
# time_index = np.arange(len(time_SRS))
# time_x_label = [str(int(x)) for x in sheet_time.col_values(5)]
time_x_name = 'time'

# ratio data
ratio_SRS = [x for x in sheet_ratio.col_values(0)]
ratio_QALSH = [x for x in sheet_ratio.col_values(1)]
ratio_Multi = [x for x in sheet_ratio.col_values(2)]
ratio_PM = [x for x in sheet_ratio.col_values(3)]
# ratio_index = np.arange(len(ratio_SRS))
# ratio_x_label = [str(int(x)) for x in sheet_ratio.col_values(5)]
ratio_x_name = 'ratio'

# recall data
recall_SRS = [x for x in sheet_recall.col_values(0)]
recall_QALSH = [x for x in sheet_recall.col_values(1)]
recall_Multi = [x for x in sheet_recall.col_values(2)]
recall_PM = [x for x in sheet_recall.col_values(3)]
# recall_x_label = [str(int(x)) for x in sheet_recall.col_values(5)]
# recall_index = np.arange(len(recall_SRS))
recall_x_name = 'recall'

A = eval(metric + '_SRS')
B = eval(metric + '_QALSH')
C = eval(metric + '_Multi')
D = eval(metric + '_PM')

index = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# x_label = eval(metric + '_x_label')
y_lable = y_labels[metric]
y_factor = y_factors[file_name + metric]
xlim = xlims['fixed']
ylim = ylims[file_name + metric]
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
ax = plt.subplot(1, 1, 1)
ax.grid(axis='y', linestyle=':', alpha=0.4)
ax.grid(axis='x', alpha=0)
ax.grid(zorder=1)
plt.rc('font', family='ARIAL', size=25)

plt.plot(index, D, color='r', ls='-', linewidth=2, marker='o', label='PM-Tree', markersize=8)
plt.plot(index, A, color='darkblue', ls='-.', linewidth=2, marker='v', label='SRS', markersize=8)
plt.plot(index, C, color='g', ls='--', linewidth=2, marker='s', label='Multi-Probe', markersize=8)
plt.plot(index, B, color='black', ls=':', linewidth=2, marker='x', label='QALSH', markersize=8)

# plt.title('square Numbers', fontsize=24)
# !!!!!!!!!!!!!!!!
# plt.ylim(ylim[0], ylim[1])
# plt.yticks([1, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35], fontsize=14)
plt.yticks(fontsize=15)

plt.xticks(index, fontsize=15)
plt.ylim(bottom=ylim[0], top=ylim[1])
plt.xlim(left=1, right=100)
# plt.xlabel(x_name, fontsize=23)    recall_x_label
# !!!!!!!!!!!!!!!!
plt.text(1, ylim[1] * y_factor, y_lable, fontsize=25)

border_width = 1
plt.legend(ncol=4, fontsize=11, facecolor='none')

ax = plt.subplot(1, 1, 1)
ax.spines['top'].set_linewidth(border_width)
ax.spines['bottom'].set_linewidth(border_width)
ax.spines['left'].set_linewidth(border_width)
ax.spines['right'].set_linewidth(border_width)
plt.subplots_adjust(top=0.93, bottom=0.06, right=0.97, left=0.12, hspace=0, wspace=0)
plt.savefig('graph/knn/' + file_name + '_' + metric + '.pdf', format='pdf', dpi=300)
# plt.show()
