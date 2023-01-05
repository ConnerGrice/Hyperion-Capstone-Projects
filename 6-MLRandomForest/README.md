# Hyperion Capstone 6 RandomForest

A demonstration on using [SciKit-Learn](https://scikit-learn.org/stable/) to train and tune a [Random Forest](https://en.wikipedia.org/wiki/Random_forest) machine learning model. The model was trained using the [MNIST handwritten digit](http://yann.lecun.com/exdb/mnist/) data-set to recognise written numbers.

## Description

This notebook is split into easy to follow sections outlining the theory behind some aspects of tuning and testing a Random Forest model.

The first step is to load in the MNIST data-set. Once loaded, the data is split into 3 subsets. Training, validation, and testing.

The model is then trained using the training data in order to generate a benchmark model performance without any parameter tuning.

After this, the parameter called `max_depth` was chosen to tuning. The model was trained multiple times using different `max_depth` values. The results were plotted and the best parameter value was found.

These findings were then used to train the final model. This model was then used on the testing subset and the results were analysed using a confusion matrix. The accuracy, precision, recall and f1-score are then explained and calculated to get some final performance metrics.

## Installation

Libraries used:

Library|Version
---|---
[NumPy](https://numpy.org/install/)|`1.23.4`
[Pandas](https://pandas.pydata.org/docs/getting_started/install.html)|`1.5.1`
[SciKit-Learn](https://scikit-learn.org/stable/install.html)|`1.1.2`
[mlxtend](http://rasbt.github.io/mlxtend/installation/)|`0.21.0`

The Jupyter notebook can be cloned into the desired directory using:

```shell
git clone https://github.com/ConnerGrice/Hyperion-Capstone-6-RandomForest.git
```

The dataset must also be downloaded and placed in the repository location. It is available [here](http://yann.lecun.com/exdb/mnist/).
