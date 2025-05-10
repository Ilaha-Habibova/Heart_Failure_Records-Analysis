# Heart Failure Clinical Records Analysis

> What is <a href="https://github.com/Ilaha-Habibova/Heart_Failure_Records-Analysis/blob/main/heart_failure_clinical_records_dataset.csv">the dataset</a> about?

This dataset contains the medical records of 299 patients who had heart failure, collected during their follow-up period, where each patient profile has 13 clinical attributes (7 continuous,5 categorical features + categorical target). Machine learning, in particular, can predict patients’ survival from their data and can identify the most important features among those included in their medical records.
<br>
## All 13 attributes' meanings:

![image](https://github.com/user-attachments/assets/28ec1f37-415f-455b-959c-1178a26057a1)

## Used software:🍊<a href="https://orangedatamining.com/">Orange</a>
Orange is an open-source data visualization, machine learning and data mining toolkit. It features a visual programming front-end for exploratory qualitative data analysis and interactive data visualization.
<br>
To download and watch its tutorials, use:
<a href="https://orangedatamining.com/">Orange website</a> and <a href="https://www.youtube.com/channel/UClKKWBe2SCAEyv7ZNGhIe4g">Orange Youtube Tutorials</a>

## Example workflow view on Orange for the dataset:

![image](https://github.com/user-attachments/assets/58d6d15f-9853-4b3e-992a-81b133af584e)
<br>
### To explore more,download the Orange file: <a href="https://github.com/Ilaha-Habibova/Heart_Failure_Records-Analysis/blob/main/Heart_Failure_Analysis.ows">Heart Failure Analysis</a>
<br>

## 🔄Data Preprocessing:
The data has no missing or duplicate data, but has outliers.<br>
After experimenting with different outlier methods, we concluded IQR method is the best for our dataset and easy to implement. We used simple python script to remove outliers from selected features which contains outliers:ejection_fraction, serum_creatinine and serum_sodium. (we removed outliers for unselected numerical features also by simply adding creatinine phosphokinase and platelets to list and then rank all 12 features to choose which features to continue with. After that we updated code for only selected features which have outliers). <br>
Note that other selected features-age has no outliers (normal range – [40,95]) and follow-up time for each patient can vary. 
<br><br>
See the final version of Python script: <a href="https://github.com/Ilaha-Habibova/Heart_Failure_Records-Analysis/blob/main/outlier_detection.py">Outlier Detection</a>

> Why were only 5 features selected 😕 ?
<br>

Because other features, especially categorical features are not important according to ranking.
<br><br>
![image](https://github.com/user-attachments/assets/83a4787b-27f2-4ab2-b49c-c5e8bff49be1)


## Unsupervised machine learning algorithms
As you can see from the Orange file, we applied 2 unsupervised machine learning algorithms:<br>
### 1. Hierarchical clustering:<br>
More we move cut off line toward right (less height ratio), more clusters are created. The main disadvantages of hierarchical clustering is that the dendrogram of clusters is hard to draw meaningful conclusions  and it requires manual intervention for selecting the appropriate number of clusters. However, we observe that perfect separation is not achieved, suggesting overlapping clusters.
<br><br>
### 2. K-means:
We have low Silhouette Score which is about 0.2. This means the classes are not well-separated. One of the factors for this result can be follow-up time dispersion. For example, when we skip time, we get higher Silhouette score. But skipping time decreases supervised ML performance, because time is an important influencing factor. Another cause may be class imbalance.

### Final Conclusion:
The two algorithms (hierarchical clustering and k-means) show the classes are poorly separable.
The Silhouette scores confirm weak separability. 
Furthermore, from Silhouette plot we can see in cluster 1, some data objects are misclassified.

## Supervised machine learning algorithms
I used `Neural network`, `Random forest` and  `XGboost` because they performed well during initial testing. For training 80 % of the data, for testing the rest-20% of the data was used. Firstly, cross validation is used for hyperparameters tuning and estimate how well our model has been trained. Then we tested our algorithms and received results of:

| Model            | AUC   | CA    | F1    | Prec  | Recall |
|------------------|-------|-------|-------|-------|--------|
| Neural Network   | 0.926 | 0.943 | 0.942 | 0.948 | 0.943  |
| Random Forest    | 0.900 | 0.849 | 0.846 | 0.846 | 0.849  |
| Gradient Boosting| 0.888 | 0.811 | 0.803 | 0.805 | 0.811  |

In medical data, mostly recall is most important performance measure. Recall in our dataset measures what percentage of patients identified correctly as having risk of death from heart failure. Therefore, we ranked algorithms according to recall. <br><br>

Neural Network performed obviously better than the others.Therefore, according to test data we conclude that Neural network is top choice due to its 94.3% recall score which minimizes missed diagnoses.<br>
From confusion matrix, we can observe all the algorithms obtained better prediction scores on the true negative rate, rather than on the true positive rate because the dataset has imbalance (67.89% negative elements and 32.11% positive elements).
<br><br><br>

## Author: [@Ilaha_Habibova](https://github.com/Ilaha-Habibova)
<br>
Unauthorized use, reproduction, modification, or distribution of this project, in whole or in part is strictly prohibited. <br>
Proper reference must be given if any part of this project is used:<br> 
Heart Failure Records Analysis by Orange: Ilaha Habibova - https://github.com/Ilaha-Habibova/Heart_Failure_Records-Analysis

### Cite of the dataset:
Heart Failure Clinical Records [Dataset]. (2020). UCI Machine Learning Repository. https://doi.org/10.24432/C5Z89R.
<br>
> Great thanks to UC Irvine Machine Learning Repository,the researchers Davide Chicco and Giuseppe Jurman.
