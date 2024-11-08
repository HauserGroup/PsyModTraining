# %%
import pandas as pd

# %%
# TODO: Don't hardcode paths
substances = pd.read_csv("../data/IsomerDesigns/output/substances2.csv")
names = pd.read_csv("../data/IsomerDesigns/output/names2.csv")
# Read the JSON file
pihkal = pd.read_json("../data/reports/Pihkal_ascii_cleaned_cleaned.json").transpose()
tihkal = pd.read_json("../data/reports/Tihkal_djvu_clean_cleaned.json").transpose()

# %%
merged_df = substances.join(
    names.set_index("substance_id"),
    on="substance_id",
    lsuffix="_substances",
    rsuffix="_names",
)

# %%
pihkal_merged = pihkal.merge(
    merged_df,
    left_on="NAME",
    right_on="name",
    how="left",
    indicator=True,
)

merged_df.loc[:, "substance_id_tihkal"] = merged_df["substance_id"] - 5000

tihkal_merged = tihkal.merge(
    merged_df,
    left_index=True,
    right_on="substance_id_tihkal",
    # left_on="NAME",
    # right_on="name",
    how="left",
    indicator=True,
)

len(tihkal.NAME.value_counts())
len(tihkal_merged.NAME.value_counts())
len(pihkal.NAME.value_counts())
len(pihkal_merged.NAME.value_counts())

# %%
# Careful multiple rows due to name_class
final_merged = pd.concat([pihkal_merged, tihkal_merged], axis=0)

# %%
# Save
final_merged.to_csv("../data/reports/final_merged.tsv", index=False, sep="\t")
