# %%
import json
import re

# %%
# txt_file = "../data/reports/Tihkal_djvu_clean_example.txt"
txt_file = "Shulgin/data/reports/Tihkal_djvu_clean_cleaned.txt"
with open(txt_file, "r") as f:
    tihkal = f.readlines()  # [:5000]

compound_dict = {
    "SYNTHESIS": "",
    "DOSAGE": "",
    "DURATION": "",
    "QUALITATIVE COMMENTS": "",
    "EXTENSIONS AND COMMENTARY": "",
}

entries = {}
skipped = 0
COMPOUND_NUMBER = None
STATE = None
VERBOSE = False

for i, line in enumerate(tihkal):
    line = line.strip()
    if not line.startswith("#") and (line == "" or len(line) < 10):
        skipped += 1
        continue

    # if line starts with #
    title = re.match(r"^#(\d+)\.\s+([\w\s\-,]+)", line)
    if title:
        COMPOUND_NUMBER = int(title.group(1))
        compound_name = title.group(2)
        entries[COMPOUND_NUMBER] = {
            "NAME": compound_name,
            "SYNTHESIS": "",
            "DOSAGE": "",
            "DURATION": "",
            "QUALITATIVE COMMENTS": "",
            "EXTENSIONS AND COMMENTARY": "",
        }
        STATE = None
        continue

    url = re.match(
        r"^http://www.erowid.org/library/books_online/tihkal/tihkal(\d+)\.shtml", line
    )

    if url:
        assert (
            int(url.group(1)) == COMPOUND_NUMBER
        ), f"URL number mismatch: {COMPOUND_NUMBER} != {url.group(1)} at line {i}"
        continue

    online_text = re.match(r"Erowid Online.+TiHKAL #(\d+)", line)
    if online_text:
        continue

    # Check for section headers and update state
    if line.startswith("SYNTHESIS"):
        STATE = "SYNTHESIS"
    elif line.startswith("DOSAGE"):
        STATE = "DOSAGE"
        line = re.sub(r"DOSAGE\s*:\s*", " ", line).strip()
        entries[COMPOUND_NUMBER][STATE] += line + " "
        continue
    elif line.startswith("DURATION"):
        STATE = "DURATION"
        line = re.sub(r"DURATION\s*:\s*", " ", line).strip()
        entries[COMPOUND_NUMBER][STATE] += line + " "
        continue
    elif line.startswith("QUALITATIVE COMMENTS"):
        STATE = "QUALITATIVE COMMENTS"
    elif line.startswith("EXTENSIONS AND COMMENTARY"):
        STATE = "EXTENSIONS AND COMMENTARY"
    elif STATE:
        # Append line to the current state section
        entries[COMPOUND_NUMBER][STATE] += line + " "

# Final check to ensure all entries have been found
required_sections = [
    "SYNTHESIS",
    "DOSAGE",
    "DURATION",
    "QUALITATIVE COMMENTS",
    "EXTENSIONS AND COMMENTARY",
]
for compound_number, compound_data in entries.items():
    for section in required_sections:
        if not compound_data[section] and VERBOSE:
            print(f"Warning: Compound {compound_number} is missing section {section}")

# Check that all compounds from 1 to 55 are found
for compound_number in range(1, 56):
    if compound_number not in entries:
        print(f"Warning: Compound {compound_number} is missing")

# %%
# Save to JSON
# TODO: Don't hardcode the file path
json_file = "Shulgin/data/reports/Tihkal_djvu_clean_cleaned.json"
with open(json_file, "w") as f:
    json.dump(entries, f, indent=4)

# %%
