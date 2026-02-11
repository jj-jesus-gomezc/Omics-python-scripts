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
# Visualization of data distribution using boxplots, violin plots and heatmaps for
# exploratory analysis practice.


# -----------------------------------------------------------------------------------------------


# --------------------------
# #Import Packages 
# --------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------
# #Load Data
# --------------------------

df = pd.read_csv("Data1.csv")

# Quick look 
print(df.head())
print(df.tail())
print(df.info())

pd.set_option("display.expand_frame_repr", False)

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
print("Shape (raw):", df.shape)
print("Shape (no NaNs):", new_df.shape)


# --------------------------
# #Save as new File
# --------------------------

new_df.to_csv("new_Data1.csv", index=False)


# --------------------------
# #Visualize Data (basic plots)
# --------------------------

# Line plot (all numeric columns)
new_df.plot()
plt.title("Data1 (clean) - Line plot")
plt.tight_layout()
plt.show()

# Scatter plot example (raw df kept just like in course)
if {"Time0_1", "Time6_1"}.issubset(df.columns):
    df.plot(kind="scatter", x="Time0_1", y="Time6_1")
    plt.title("Scatter: Time0_1 vs Time6_1")
    plt.tight_layout()
    plt.show()


#---------------------------------------------------------

# --------------------------
# #Data Filtering
# --------------------------

if "Time0_1" in df.columns:
    filtered_df = df.query("Time0_1 > 80")
    print("Filtered (Time0_1 > 80):", filtered_df.shape)

if {"Time0_1", "Time6_1"}.issubset(df.columns):
    filtered_df1 = df.loc[(df["Time0_1"] > 80) & (df["Time6_1"] > 80)]
    print("Filtered (Time0_1 & Time6_1 > 80):", filtered_df1.shape)

#------------------------------------------------------

# --------------------------
# Boxplot Visualization (use clean data)
# --------------------------

ax = plt.figure(figsize=(12, 12))
plt.xlabel("time", fontsize=14)
plt.ylabel("intensity", fontsize=14)
new_df.boxplot(grid=False, rot=45, fontsize=15)
plt.title("Boxplots (Data1 clean)")
plt.tight_layout()
plt.savefig("boxplot_data1.png", dpi=300, bbox_inches="tight")
plt.show()

# --------------------------
# #Violin Plots
# --------------------------

plt.figure(figsize=(12, 12))
plt.xlabel("time", fontsize=14)
plt.ylabel("intensity", fontsize=14)
sns.violinplot(data=new_df)
plt.title("Violin plots (Data1 clean)")
plt.tight_layout()
plt.savefig("violinplot_data1.png", dpi=300, bbox_inches="tight")
plt.show()

#------------------------------------------------------
# --------------------------
# #Heatmaps (Data3)
# --------------------------

df3 = pd.read_csv("Data3.csv", index_col=0)
print(df3.head())

plt.figure(figsize=(6, 6))
sns.heatmap(df3, vmin=-2, vmax=6, cmap="Blues")
plt.title("Heatmap (Data3)")
plt.tight_layout()
plt.savefig("heatmap_data3.png", dpi=300, bbox_inches="tight")
plt.show()

# --------------------------Add annotation--------------------------
plt.figure(figsize=(6, 6))
sns.heatmap(df3, vmin=-2.0, vmax=6, cmap="viridis", annot=True)
plt.title("Heatmap annotated (Data3)")
plt.tight_layout()
plt.savefig("heatmap_annot_data3.png", dpi=300, bbox_inches="tight")
plt.show()


# --------------------------Clustering Heatmaps--------------------------

g = sns.clustermap(df3, cmap="viridis_r", vmin=-2.0, vmax=6, annot=True, linecolor="w")
g.savefig("clustermap_data3.png", dpi=300)
plt.show()


# --------------------------Standardize--------------------------

g = sns.clustermap(df3, standard_scale=1, cmap="viridis_r",
                   annot=True, linecolor="w", linewidths=1)

g.savefig("clustermap_standardized.png", dpi=300)
plt.show()


# --------------------------Normalize (z-score)--------------------------
g = sns.clustermap(df3, z_score=1, cmap="viridis_r", annot=True, linecolor="w")
g.savefig("clustermap_zscore.png", dpi=300)
plt.show()

# --------------------------Robust Normalization--------------------------
g = sns.clustermap(df3, cmap="viridis_r", robust=True, annot=True, linecolor="w")
g.savefig("clustermap_robust.png", dpi=300)
plt.show()

print("Done. Outputs saved as PNG/CSV in the current folder.")

