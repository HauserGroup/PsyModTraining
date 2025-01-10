# Experimental Data 

## a.Multilabel Random Forest
steps:
- 1. Data preparation
    - read fingerprint file and experiment data file
    - binarize the experiment data file -> create multilabel for receptors
    - merge features and labels -> to ensure the features and labels match based on drugs

- 2. Training
    - Methods introduction:
        - Optuna -> hyperparameter selection
        - Random Forest -> can trace back to find important features 
        - Nested cross validation -> reduce overfitting for small dataset (use cross validation for both training and evaluation), 
            - "Choosing the parameters that maximize non-nested CV biases the model to the dataset, yielding an overly-optimistic score" -- sklearn.
            - inner cv for hyperparameter search, outer cv for evaluation

        - Optuna optimization based on average minimized hamming loss of each cv

    - Methods:
        - Optuna + nested cv
            - 5-fold cv for both inner and outer cv
            - optuna search 50 trials for each inner cv
            - optuna optimization is based on hamming loss
            - rf hyperparameter range: 
                - "n_estimators", 10, 100
                - "max_depth", 5, 20
                - "min_samples_split", 2, 5
                - "min_samples_leaf", 1, 4
                - "bootstrap", [True, False]
        - Optuna + cv 
            - 5-fold cv only for outer cv (evaluation part)
            - optuna search 50 trials without inner cv, but once for each outer cv
            - optuna optimization is based on hamming loss
            - rf hyperparameter range: -> the same as Optuna + nested cv
                - "n_estimators", 10, 100
                - "max_depth", 5, 20
                - "min_samples_split", 2, 5
                - "min_samples_leaf", 1, 4
                - "bootstrap", [True, False]

- 3. Evaluation
    - hamming loss: smaller the better
        - measures the fraction of labels that are incorrectly predicted. when predicting for single label, the same as accuracy
    - accuracy: closer to one the better
        - Measures the proportion of correctly predicted labels.
    - f1 micro: closer to one the better
        - Calculates the F1 score by aggregating the contributions of all classes.
    - jaccard samples: closer to one the better
        - Measures the similarity between the predicted and true labels.


- 4. Questions
    - is the parameter range correct? -> since the input features have 166 and predicted labels have 25
    - how to describe the figure? possible explanations
        - imbalanced dataset: some labels have only 1 and some only 0
        - too many features: features vs samples = 166 vs 43
    - further improvement?
        - feature dimentionality reduction -> lasso regression
    - why do i choose hamming loss to do the optimization?
    - what do those metrics mean and do i need other metrics?


## b.Real Value Random Forest
steps:
- 1. Data preparation
    - read fingerprint file and experiment data file
    - wash data and choose largest Emax among all gprotein as target 
        - why choose largest Emax: for convenience and can best separate binding and not binding
    - merge features and targets -> to ensure the features and labels match based on drugs

- 2. Training
    - Methods introduction:
        - Multioutput Random Forest Regression 
        - Nested CV
        - Optuna

    - Multioutput Random Forest Regression  + Nested CV
        - 5-fold for both inner and outer cv
        - optuna optimization is based on mean squared error


- 3. Evaluation
    - mean square error: lower the better
         measure the difference between predicted value and ground truth
    - r2: closer to 1 the better
    - explained variance score: [0,1], closer to 1 the better
        - how much of the variance in the target is captured by the model
    - mean absolute error

- 4. Questions
    - how to compare which one is better, a or b?
    - why those metrics, what information can i get?
    - Since I use optuna to choose hyperparameters, when optimizing, it considers the mean value of all receptors. Different receptors may have different the best hyperparameters. Therefore, I choose to build the model only for 5-HT6 (c). 

## b'. Real Value Random Forest Threshold
Almost the same as b
- 2. Training
    - Methods introduction:
        - Multioutput Random Forest Regression 
        - Nested CV
        - Optuna

    - Multioutput Random Forest Regression  + Nested CV
        - 5-fold for both inner and outer cv
        - model train on real value but evaluation is based on the accuracy of predicting labels. Transform the predicted values to bits based on threshold
        - optuna optimization is based on hamming loss of each cv fold
        - optimize threshold 

- 3. Evaluation
    - hamming loss but transformed the values to labels based on threshold

- 4. Questions  
    - how to set the range of threshold?
    - compare results to multilabel



## c.Random Forest Classification - 5-HT6
steps:
- 1. Data preparation
    - read fingerprint file and experiment data file
    - binarize the experiment data file
    - merge features and targets -> to ensure the features and labels match based on drugs
    - only leave 5HT6 as target -> because 5HT6 is less imbalanced

- 2. Training
    - Methods introduction:
        - Random Forest Classification
        - Nested CV
        - Optuna


    -  Random Forest Classification  + Nested CV
        - 5-fold for both inner and outer cv
        - optuna optimization is based on accuracy


- 3. Evaluation
    - accuracy
    - f1
    - roc

