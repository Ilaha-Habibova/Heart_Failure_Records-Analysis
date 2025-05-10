from Orange.data import Table
import numpy as np

# Calculate IQR bounds
def iqr_outliers(data, feature):
    Q1 = np.percentile(data.X[:, feature], 25)
    Q3 = np.percentile(data.X[:, feature], 75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR
    return (data.X[:, feature] < lower) | (data.X[:, feature] > upper)

# Apply to features that contain outliers
outlier_mask = np.zeros(len(in_data), dtype=bool)
for i, var in enumerate(in_data.domain.attributes):
    if var.name in ['ejection_fraction', 'serum_creatinine', 'serum_sodium']:
        outlier_mask |= iqr_outliers(in_data, i)

out_data = in_data[~outlier_mask]