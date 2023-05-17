import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def millions_and_thousands_formatter(x, pos):
    if x >= 1_000_000:
        return f'{x/1_000_000:.1f} MM'
    elif x >= 1_000:
        return f'{x/1_000:.0f} K'
    else:
        return f'{x:.0f}'

df = pd.read_csv('C:/Users/danie/Desktop/PROYECTO DATA/dataset.csv')
datasets = {
    'Male': df['Male'],
    'Female': df['Female']
}
age_labels = df['Age Group']

bar_width = 0.9
colors = {'Male': '#3f7ad8', 'Female': '#b715b8'}
insert_location = np.zeros(len(age_labels))

fig, ax = plt.subplots(figsize=(10, 7))
ax.yaxis.set_major_formatter(ticker.FuncFormatter(millions_and_thousands_formatter))

for label, data_points in datasets.items():
    chart = ax.bar(age_labels, data_points, width=bar_width, color=colors[label], label=label, bottom=insert_location)
    ax.bar_label(chart, label_type='center', color='white', labels=[f"{millions_and_thousands_formatter(val, None)}" for val in data_points], fontsize='small')
    insert_location += data_points

ax.legend(loc='upper right')
plt.title('Population estimate (2021)', fontsize=20)

plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()
