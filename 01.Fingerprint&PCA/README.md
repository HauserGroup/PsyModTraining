# Fingerprint & PCA
## purpose: 
- generate different fingerprints using SMILES (RDkit, MACCS, Morgen, FCFP, Topological Torsion, Atom Pair)
- PCA and color the molecules by categories (Lysergamide, Phenethylamine, Tryptamine, Unknown)

## process
- input: 40_Psychedelic_drug.csv, psychedelics_all_fingerprints.csv (Name, SMILES, Category)
- output 1: different fingerprints
- output 2: PCA graphs using different fingerprints
- output 3: explained variance of different fingerprints 

## file explanation
- 40_Psychedelic_drug.csv: 40 psychedelic drugs with SMILES and Categories (Lysergamide, Phenethylamine, Tryptamine, Unknown)
- psychedelics_all_fingerprints.csv: ~250 psychoactive molecules with SMILES and Categories and other info