# Experimental Data 

## Multilabel Random Forest
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
            - rf hyperparameter range: 
                - "n_estimators", 10, 100
                - "max_depth", 5, 20
                - "min_samples_split", 2, 5
                - "min_samples_leaf", 1, 4
                - "bootstrap", [True, False]
        - Optuna + cv 
            - 5-fold cv only for outer cv (evaluation part)
            - optuna search 50 trials without inner cv, but once for each outer cv
            - rf hyperparameter range: -> the same as Optuna + nested cv
                - "n_estimators", 10, 100
                - "max_depth", 5, 20
                - "min_samples_split", 2, 5
                - "min_samples_leaf", 1, 4
                - "bootstrap", [True, False]

- 3. Evaluation
    - hamming loss: measures the fraction of labels that are incorrectly predicted. when predicting for single label, the same as accuracy
    - accuracy: Measures the proportion of correctly predicted labels.
    - f1 micro: Calculates the F1 score by aggregating the contributions of all classes.
    - jaccard samples: Measures the similarity between the predicted and true labels.


- 4. Questions
    - is the parameter range correct? -> since the input features have 166 and predicted labels have 25
    - how to describe the figure? possible explanations
        - imbalanced dataset: some labels have only 1 and some only 0
    - further improvement?
    - why i choose hamming loss to do the optimization?
    - what do those metrics mean and do i need other metrics?


## Real Value Random Forest

