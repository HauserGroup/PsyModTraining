# Hallucinate Paper Repeat

## Random Forest Classification - 5-HT6
steps:
- 1. Data preparation
    - read precreated fingerprints file and PsychLight data

- 2. Training
    - Methods introduction:
        - Random Forest Classification
        - Nested CV
        - StratifiedKFold CV -> keep the same proportion
        - Optuna


    -  Random Forest Classification  + Nested CV
        - StratifiedKFold 5-fold for both inner and outer cv
        - optuna optimization is based on accuracy


- 3. Evaluation
    Accuracy (ACC)、F1-score、AUC、Cohen's Kappa、MCC、Precision、Recall、Specificity、True Negative (TN)、False Positive (FP)、False Negative (FN)、True Positive (TP)

