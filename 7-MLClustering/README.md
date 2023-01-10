# Hyperion-Capstone 7 PCA_Clustering

A demonstration on using PCA to simplify a dataset, then comparing the [K-mean](https://en.wikipedia.org/wiki/K-means_clustering) and [Hierarchical](https://en.wikipedia.org/wiki/Hierarchical_clustering) clustering algorithms. The [dataset](https://www.kaggle.com/datasets/kurohana/usarrets) used contains crime statistics for each US state. [Scikit-learn](https://scikit-learn.org/stable/) was used for the clustering algorithms.

## Description

This exploration follows a simple structure. First, there is a small EDA on the dataset in order to understand what data we're dealing with and find any interesting insights that may be useful.

After this a PCA is investigated and the optimal number of column reductions are found using the explained variance metric. An analysis of the new principle axes is also carried out. Trying to explain that these new axes actually mean and how we can interpret them.

 Once this is completed, the K-mean model is trained, after finding what number of clusters gives the best silhouette score. After the training, the clustering is analysed further to find the reasons why the cluster formed the way it did and how that is linked to the original data.

 A hierarchical model is them generated on the same set of data, and once again, the interpretations of the clustering is given. Finally, both models are compared to each other.
