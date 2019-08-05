import matplotlib.pyplot as plt
import numpy as np
import xlrd

ratio_time = xlrd.open_workbook('data/0716/ratiotime2.xlsx')
recall_time = xlrd.open_workbook('data/0716/recalltime2.xlsx')

plt.rcParams['figure.figsize'] = (8, 4)

# str_book = 'ratio_time'
str_book = 'recall_time'
str_sheet = 'trevi'

ylabel = {'ratio_time': 'Ratio', 'recall_time': 'Recall'}
legend_loc = {'ratio_time': 'upper right', 'recall_time': 'bottom right'}
ylabel_factors = {'ratio_timemnist': 1.001, 'ratio_timenus': 1.0001, 'ratio_timetrevi': 1.0001,
                  'ratio_timeDeep1m': 1.0001, 'recall_timeDeep1m': 1.01, 'recall_timenus': 1.01,
                  'recall_timetrevi': 1.01,
                  'recall_timemnist': 1.01}
legend_loc
ylim = {'ratio_timemnist': [1, 1.06], 'ratio_timenus': [1, 1.01], 'ratio_timetrevi': [1, 1.015],
        'ratio_timeDeep1m': [1, 1.025], 'recall_timeDeep1m': [0.5, 1], 'recall_timenus': [0.7, 1],
        'recall_timetrevi': [0.55, 1],
        'recall_timemnist': [0.6, 1]}
xlim = {'ratio_timemnist': [0.01, 0.031], 'ratio_timenus': [0.08796, 0.214], 'ratio_timetrevi': [0.031, 0.30],
        'ratio_timeDeep1m': [0.065, 0.53], 'recall_timeDeep1m': [0.065, 0.53], 'recall_timenus': [0.087, 0.22],
        'recall_timetrevi': [0.024, 0.41],
        'recall_timemnist': [0.009, 0.031]}

# file name
book = eval(str_book)

sheet_mnist = book.sheets()[0]
sheet_nus = book.sheets()[1]
sheet_trevi = book.sheets()[2]
sheet_Deep1m = book.sheets()[3]

# sheet name
sheet = eval('sheet_' + str_sheet)

SRS = [x for x in sheet.col_values(0) if x != ""]
SRS_index = [x for x in sheet.col_values(1) if x != ""]
QALSH = [x for x in sheet.col_values(2) if x != ""]
QALSH_index = [x for x in sheet.col_values(3) if x != ""]
MUL_LSH = [x for x in sheet.col_values(4) if x != ""]
MUL_LSH_index = [x for x in sheet.col_values(5) if x != ""]
PM_LSH = [x for x in sheet.col_values(6) if x != ""]
PM_LSH_index = [x for x in sheet.col_values(7) if x != ""]

A_name = SRS.pop(0)
B_name = QALSH.pop(0)
C_name = MUL_LSH.pop(0)
D_name = PM_LSH.pop(0)

SRS_index.pop(0)
QALSH_index.pop(0)
MUL_LSH_index.pop(0)
PM_LSH_index.pop(0)

A = SRS
B = QALSH
C = MUL_LSH
D = PM_LSH

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

plt.plot(PM_LSH_index, D, color='r', ls='-', linewidth=2, marker='o', label='PM-LSH', markersize=6, zorder=10)
plt.plot(SRS_index, A, color='darkblue', ls='-.', linewidth=2, marker='v', label='SRS', markersize=6)
plt.plot(QALSH_index, B, color='g', ls='--', linewidth=2, marker='s', label='QALSH', markersize=6)
plt.plot(MUL_LSH_index, C, color='black', ls=':', linewidth=2, marker='x', label='Multi-Probe', markersize=6)

# plt.title('square Numbers', fontsize=24)
# !!!!!!!!!!!!!!!!
# plt.ylim(ylim[0], ylim[1])
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)

plt.ylim(bottom=ylim[str_book + str_sheet][0], top=ylim[str_book + str_sheet][1])
plt.xlim(left=xlim[str_book + str_sheet][0], right=xlim[str_book + str_sheet][1])
plt.xlabel('Time', fontsize=20)
# !!!!!!!!!!!!!!!!
plt.text(xlim[str_book + str_sheet][0], ylim[str_book + str_sheet][1] * ylabel_factors[str_book + str_sheet],
         ylabel[str_book], fontsize=20)

border_width = 1
# plt.legend(loc=legend_loc[str_book], ncol=4, fontsize=12, facecolor='none')
plt.legend(ncol=4, fontsize=12, facecolor='none')

ax = plt.subplot(1, 1, 1)
ax.spines['top'].set_linewidth(border_width)
ax.spines['bottom'].set_linewidth(border_width)
ax.spines['left'].set_linewidth(border_width)
ax.spines['right'].set_linewidth(border_width)
plt.subplots_adjust(top=0.90, bottom=0.15, right=0.97, left=0.12, hspace=0, wspace=0)
fname = str_sheet + '_' + str_book
plt.savefig('graph/' + fname + '.pdf', format='pdf', dpi=300)
# plt.show()
