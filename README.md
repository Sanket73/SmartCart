Customer Segmentation using Clustering

# Project Overview

This project performs Customer Segmentation using clustering techniques to group customers based on purchasing behavior, demographics, and engagement patterns. The segmentation helps businesses target customers effectively and improve marketing strategies.

# Project Structure

smartcart-clustering/
├── data
│   ├── raw                  # Original dataset
│   ├── processed            # Cleaned & engineered data
│   └── results              # Clustering outputs
│
├── notebooks
│   ├── 01_data_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_clustering.ipynb
│   └── 04_analysis.ipynb
│
├── src
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── clustering.py
│   ├── visualization.py
│   └── evaluation.py
│
├── results
    ├── figures              # Generated plots
    └── reports              # Analysis reports


# Objectives

Clean and preprocess customer data

Engineer useful features

Perform clustering to group customers

Evaluate optimal number of clusters

Analyze and characterize each customer segment

# Workflow

1. Data Preprocessing

Handled missing values

Removed irrelevant columns

Cleaned dataset

2. Feature Engineering

Created derived features

Dropped unnecessary attributes

3. Visualization & Analysis

Generated correlation heatmap

Explored distributions

Studied customer behavior

4. Encoding

Converted categorical data into numeric format.

5. Scaling

Normalized features to improve clustering performance.

6. Optimal K Selection

Used:

Elbow Method

Silhouette Score

7. Clustering

Applied K-Means clustering to segment customers.

8. Cluster Characterization

# Average characteristics of clusters:

| Feature              | Cluster 0 | Cluster 1 | Cluster 2 | Cluster 3 |
|----------------------|-----------|-----------|-----------|-----------|
| Income               | 39,680    | 72,808    | 36,960    | 70,722    |
| Recency              | 48.9      | 49.2      | 48.3      | 50.5      |
| Deals Purchases      | 2.59      | 1.95      | 2.59      | 1.86      |
| Web Purchases        | 3.15      | 5.69      | 2.71      | 5.79      |
| Catalog Purchases    | 0.97      | 5.49      | 0.84      | 5.01      |
| Store Purchases      | 4.14      | 8.66      | 3.62      | 8.43      |
| Web Visits/Month     | 6.30      | 3.58      | 6.65      | 3.73      |
| Complaint Rate       | Very Low  | Very Low  | Very Low  | Very Low  |
| Campaign Response    | 0.076     | 0.167     | 0.142     | 0.320     |
| Avg Age              | ~56       | ~59       | ~56       | ~59       |
| Tenure Days          | 343       | 370       | 339       | 376       |
| Total Spending       | 222       | 1237      | 166       | 1190      |


# Cluster Insights

## Cluster 0 — Low Income Regular Buyers

Moderate store purchases

Low total spending

Frequent web visits

Budget-conscious customers

## Cluster 1 — High Income Heavy Spenders

High store and catalog purchases

High total spending

Fewer web visits

Loyal premium customers

## Cluster 2 — Low Spending Occasional Buyers

Lowest spending group

Lower purchases overall

High browsing but low buying

## Cluster 3 — Premium Loyal Customers

Very high spending

High campaign response

Strong purchasing frequency

Best target for retention campaigns

# Technologies Used

* Python

* Pandas

* NumPy

* Scikit-learn

* Matplotlib

* Seaborn

# Conclusion

The project successfully segments customers into meaningful groups enabling data-driven marketing decisions.
