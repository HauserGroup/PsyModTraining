# Group Selfies

## group_selfie_psy_testIfSameMol
### purpose
make sure gsf can reconstruct the molecules

## group_selfie_psy_upsetPlot
show the fragments from auto fragmentation in psychedelic drugs

step:
- 1. Data Preparation
    - input: 
        - `For auto fragmentation`: SMILES_PsychLight&all_fingerprint.csv -> collect molecules both in PsycheLight and psychedelics_all_fingerprints file, to get as much psychoactive molecules as possible
        - `For showing fragments in psychedelic drugs`: Hallucinate.csv

- 2. Group Token extraction (auto fragementation)
    - methods: 
        - default: 
        - mmpa
        - fraggle

- 3. Upset Plot
    - show all results
    - reduce minor fragments
    show which fragments dominate

## gsf_model
Apply gsf on chembl data to predict whether molecules can active 5HT2A

steps:
- 1. Data Preparation
    - process pChEMBL_data.csv -> remove "not determined", remove duplicates
        - psy = 277
        - non-psy = 563 -> imbalanced?
    - autofragmentation on all chembl using mmpa
        - why use mmpa: 
    - fragment chembl
    - one-hot encoding for fragments of each molecules

- 2. Models
    - gsf-Single Label
        - autofragmentation on all chembl using mmpa
            - why use mmpa: 
        - fragment chembl
         - one-hot encoding for fragments of each molecules
        - binarize the target with Threshold = 0
        - StratifiedKFold, nested CV
    
    - MACCS-Single Label
        same model but change input




    


