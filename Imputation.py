## 
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

# 1. ---- Load Data ----
data = pd.read_csv('Data.csv', index_col=0)
data.replace(0, np.nan, inplace=True)

# 2. ---- Imputation Methods ----

## ---- Mean Imputation ----
mean_imputer = SimpleImputer(strategy='mean')
imputed_mean_array = mean_imputer.fit_transform(dataset)
imputed_data_mean = pd.DataFrame(imputed_mean_array, columns=dataset.columns, index=dataset.index)

  ## ---- Iterative Imputer (Linear Regression) ----
iter_lr_imputer = IterativeImputer(estimator=LinearRegression(), max_iter=40, tol=0.001, initial_strategy='mean', random_state=42)
imputed_lr_array = iter_lr_imputer.fit_transform(dataset)
imputed_data_lr = pd.DataFrame(mputed_lr_array, columns=dataset.columns, index=dataset.index)

  ## ---- Iterative Imputer (Random Forest) ----
iter_rf_imputer = IterativeImputer(estimator=RandomForestRegressor(n_estimators=40, random_state=42, n_jobs=-1), max_iter=10, initial_strategy='mean', random_state=42)
imputed_rf_array = iter_rf_imputer.fit_transform(dataset)
imputed_data_rf = pd.DataFrame(imputed_rf_array, columns=dataset.columns, index=dataset.index)

  ## ---- KNN Imputer (scaled data) ----
scaler = StandardScaler()
dataset_scaled = pd.DataFrame(scaler.fit_transform(dataset), columns=dataset.columns, index=dataset.index)
knn_imputer = KNNImputer(n_neighbors=4)
imputed_knn_scaled_array = knn_imputer.fit_transform(dataset_scaled)
imputed_knn_array = scaler.inverse_transform(imputed_knn_scaled_array)
imputed_data_knn = pd.DataFrame(imputed_knn_array, columns=dataset.columns, index=dataset.index)

print("\nAll imputed datasets saved.")

# ---- 3. Save all results ----
imputed_data_mean.to_csv('imputed_mean_Data1.csv')
imputed_data_lr.to_csv('imputed_LR_Data1.csv')
imputed_data_rf.to_csv('imputed_RF_Data1.csv')
imputed_data_knn.to_csv('imputed_KNN_Data1.csv')

# ---- 4. Create Dictionary ----
imputed_results = {
    "mean": imputed_data_mean,
    "lr": imputed_data_lr,
    "rf": imputed_data_rf,
    "knn": imputed_data_knn
}

# ---- 5. Plotting ----

  ## ---- Plotting: Boxplots ----
plt.rcParams['svg.fonttype'] = 'none'

plot_datasets = {"raw": dataset, **imputed_results}
plot_titles = {
    "raw": "Original Data (after zero→NaN)",
    "mean": "Imputed Data (Mean)",
    "lr": "Imputed Data (Iterative Linear Regression)",
    "rf": "Imputed Data (Iterative Random Forest)",
    "knn": "Imputed Data (KNN)"
}
plot_colors = { "raw": "skyblue", "mean": "orange", "lr": "pink", "rf": "green", "knn": "red"}
fig, axes = plt.subplots(nrows=len(plot_datasets), figsize=(10, 26), sharex=True)

for ax, (method, data) in zip(axes, plot_datasets.items()):
    sns.boxplot(ax=ax, data=data, color=plot_colors[method])
    ax.set_title(plot_titles[method])
    ax.tick_params(axis='x', labelrotation=60)

plt.tight_layout()
plt.show()


  ## ----KDE plot of column sums (first 6 columns) ----
columns_to_compare = dataset.columns[:6]
plt.figure(figsize=(12, 7))
columns_sum_raw = dataset[columns_to_compare].sum()
sns.kdeplot(columns_sum_raw, label='Raw (with NaN)', color='blue', fill=True)

kde_colors = {"mean": "orange", "lr": "pink", "rf": "green", "knn": "red"}
kde_labels = {"mean": "Mean","lr": "Iterative LR","rf": "Iterative RF","knn": "KNN"}
kde_linestyles = {"mean": "-","lr": "--","rf": "-.","knn": ":"}

for method, data in imputed_results.items():
    columns_sum = data[columns_to_compare].sum()
    sns.kdeplot(columns_sum, label=kde_labels[method], color=kde_colors[method], linestyle=kde_linestyles[method], fill=True)

plt.title("Sum across first 6 columns: Raw vs Imputed")
plt.legend()
plt.show()


# ---- 6. Results comparisson: Side-by-side Heatmaps ----
fig, axes = plt.subplots(ncols=5, figsize=(23, 6), sharey=True)

sns.heatmap(dataset.isnull(), ax=axes[0], cbar=False, cmap='viridis')
axes[0].set_title('Raw (zero→NaN)')

heatmap_titles = {"mean": "Imputed (Mean)","lr": "Imputed (Iterative LR)", "rf": "Imputed (Iterative RF)","knn": "Imputed (KNN)"}

for i, (method, data) in enumerate(imputed_results.items(), start=1):
    sns.heatmap(data.isnull(), ax=axes[i], cbar=False, cmap='viridis')
    axes[i].set_title(heatmap_titles[method])

for ax in axes:
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

plt.tight_layout()
plt.show()


# ---- 7. Summary statistics ----
print("\nOriginal data summary (with NaN):\n", dataset.describe())

summary_titles = {
    "mean": "Mean",
    "lr": "Iterative Linear Regression",
    "rf": "Iterative Random Forest",
    "knn": "KNN"
}

for method, data in imputed_results.items():
    print(f"\nImputed data ({summary_titles[method]}):\n", data.describe())





