# Input Exploration

## Fingerprint_PCA.ipynb
### purpose: 
- generate different fingerprints using SMILES (RDkit, MACCS, Morgen, FCFP, Topological Torsion, Atom Pair)
- PCA and color the molecules by categories (Lysergamide, Phenethylamine, Tryptamine, Unknown)

### process
- input: 43_Psychedelic_drug_SMILES_Category.csv, psychedelics_all_fingerprints.csv (Name, SMILES, Category)
- output 1: different fingerprints
- output 2: PCA graphs using different fingerprints
- output 3: explained variance of different fingerprints 

### file explanation
- 43_Psychedelic_drug_SMILES_Category.csv: 43 psychedelic drugs with SMILES and Categories (Lysergamide, Phenethylamine, Tryptamine, Unknown)
- psychedelics_all_fingerprints.csv: ~250 psychoactive molecules with SMILES and Categories and other info


## Get_fingerprint.ipynb
- can output different combinations of fingerprints. Purely for fingerprints output.


## g protein correlation
### purpose:

