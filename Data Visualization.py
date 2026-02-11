# -----------------------------------------------------------------------------------------------
# Script: Graphic Visualization of Omic Data
#
# Original author: Dr. Eliel Ruiz May
# Source: Omics Data Analysis Course Material
#
# Adapted and explored by:
# Juan José de Jesús Gómez Castro
#
# Description:
# Visualization of data distribution using boxplots, violoin plots and heatmaps for
# exploratory analysis practice.


# -----------------------------------------------------------------------------------------------


# --------------------------
# #Import Packages 
# --------------------------

import pandas as pd
import matplotlib.pyplot as plt

# --------------------------
# #Load Data
# --------------------------

df= pd.read_csv('Data1.csv')

df

df.head()
df.tail()

# --------------------------
# #Visualizing all Dataframe
# --------------------------

pd.set_option('display.expand_frame_repr', False)


df= pd.read_csv('Data1.csv')

df


print(df.info()) 


# --------------------------
# #Delete Empty Cells
# --------------------------


new_df = df.dropna()

new_df


# --------------------------
# #Save as new File
# --------------------------


new_df.to_csv('new_Data1.csv')

new_df.to_csv('new_Data1.csv', index=0)


# --------------------------
# #Visualize Data in Graphs
# --------------------------


new_df.plot()


df.plot(kind = 'scatter', x = 'Time0_1', y = 'Time6_1')


df["Time0_1"].plot(kind = 'hist')



#---------------------------------------------------------

# --------------------------
# #Data Filtering
# --------------------------


filtered_df = df.query('Time0_1 > 80') 


filtered_df


filtered_df1= df.loc[(df['Time0_1']> 80) & (df['Time6_1']> 80)]

filtered_df1


#------------------------------------------------------

# --------------------------
# #Load Data1
# --------------------------


df= pd.read_csv('Data1.csv')


df

# --------------------------
# #Boxplot Visualization
# --------------------------


ax = plt.figure(figsize=(12, 12))
plt.xlabel("time", fontsize=14)
plt.ylabel("intensity", fontsize=14)
df.boxplot(grid=False, rot=45, fontsize=15)  

# --------------------------
# #Violin Plots
# --------------------------


import seaborn as sns

ax = plt.figure(figsize=(12, 12))
plt.xlabel("time", fontsize=14)
plt.ylabel("intensity", fontsize=14)
sns.violinplot(data = df)


#------------------------------------------------------
# --------------------------
# #Heatmaps
# --------------------------


import pandas as pd
import seaborn as sns
import scipy
from pandas import read_csv
import matplotlib.pyplot as plt

df= read_csv('Data3.csv', index_col=0)


df



plt.figure(figsize=(6,6))

sns.heatmap(df, vmin = -2, vmax = 6, cmap="Blues")
plt.show()



# --------------------------
# #Add annotation
# --------------------------

plt.figure(figsize=(6,6))

sns.heatmap(df, vmin = -2.0, vmax = 6, cmap="viridis", annot = True)
plt.show()




# --------------------------
# #Clustering Heatmaps
# --------------------------

sns.clustermap(df, cmap="viridis_r",  vmin = -2.0, vmax = 6, annot = True, linecolor="w")

# --------------------------
# #Show the graph
# --------------------------


plt.show()


# --------------------------
# #Standarize
# --------------------------


sns.clustermap(df, standard_scale=1,cmap="viridis_r", annot = True,linecolor="w", linewidths=1)
plt.show()


# --------------------------
# #Normalize
# --------------------------


sns.clustermap(df, z_score=1, cmap="viridis_r", annot = True,linecolor="w")
plt.show()


# --------------------------
# #Robust Normalization
# --------------------------


sns.clustermap(df, cmap="viridis_r",  robust = True, annot = True, linecolor="w")
plt.show()





