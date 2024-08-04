# import important libraries
import pandas as pd
import matplotlib.pyplot as plt

# set the (csv/txt) file directory
file_path = 'Gene_Data.csv'

# read the file with '\t' delimiter
df = pd.read_csv(file_path, delimiter='\t')

### ADDITIONAL THINGS TO DO [REF-1] ###
# in-case the file contains a lot of gene and you want to work only specific genes
# comment out the following line of code if you need it
#genes_to_keep = ['Gene1', 'Gene2', 'Gene3']
# filtering the dataframe to keep only the rows with specified genes
#df_filtered = df[df['gene'].isin(genes_to_keep)].copy()


### ADDITIONAL THINGS TO DO [REF-2] ###
# in-case the specific columns (oe_lof, oe_lof_lower, oe_lof_upper) contains string value and decimal points separated by ','
# comment out the following lines of code if you need it
#df_filtered['oe_lof'] = df_filtered['oe_lof'].str.replace(',', '.').astype(float)
#df_filtered['oe_lof_lower'] = df_filtered['oe_lof_lower'].str.replace(',', '.').astype(float)
#df_filtered['oe_lof_upper'] = df_filtered['oe_lof_upper'].str.replace(',', '.').astype(float)


### FOR REF-1 and REF-2 in the following lines of code use df_filtered instead of df    

# sort the dataframe by oe_lof
df = df.sort_values(by='oe_lof')

# plotting the data
fig, ax = plt.subplots(figsize=(14, 7))

# plot the dots for oe_lof
ax.scatter(df['gene'], df['oe_lof'], color='black', zorder=2)

# plot the bars for oe_lof_lower and oe_lof_upper
for idx in df.index:
    ax.plot([df['gene'][idx], df['gene'][idx]], [df['oe_lof_lower'][idx], df['oe_lof_upper'][idx]], color='gray', zorder=1)

# formatting the plot
ax.set_xlabel('Genes')
ax.set_ylabel('Observed/expected LoF ratio')
ax.set_xticks(range(len(df['gene'])))
ax.set_xticklabels(df['gene'], rotation=90)
ax.set_ylim(0.0, 2.0)

plt.title('A set of 25 Genes (Sorted by oe_lof)')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

# Save the plot as a file
plt.savefig('oe_lof_plot_sorted.png')

# Display the plot
plt.show()