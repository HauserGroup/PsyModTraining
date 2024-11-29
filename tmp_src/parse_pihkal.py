# %%
import json
import re


def parse_pihkal(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    entries = {}
    COMPOUND_NUMBER = None
    STATE = None

    for line in lines:
        line = line.strip()

        # Match compound number and name
        title = re.match(r"^#(\d+)\s+([\w\s\-,;]+)", line)
        if title:
            COMPOUND_NUMBER = int(title.group(1))
            compound_name = title.group(2).strip()
            compound_names = [name.strip() for name in compound_name.split(";")]
            entries[COMPOUND_NUMBER] = {
                "NAME": compound_names[0],
                "ALTERNATIVE NAMES": compound_names[1:],
                "SYNTHESIS": "",
                "DOSAGE": "",
                "DURATION": "",
                "QUALITATIVE COMMENTS": "",
                "EXTENSIONS AND COMMENTARY": "",
            }
            STATE = None
            continue

        # Check for section headers and update state
        if line.startswith("SYNTHESIS"):
            STATE = "SYNTHESIS"
        elif line.startswith("DOSAGE"):
            STATE = "DOSAGE"
            entries[COMPOUND_NUMBER][STATE] = re.sub(
                r"DOSAGE\s*:\s*", " ", line
            ).strip()
        elif line.startswith("DURATION"):
            STATE = "DURATION"
            entries[COMPOUND_NUMBER][STATE] = re.sub(
                r"DURATION\s*:\s*", " ", line
            ).strip()
        elif line.startswith("QUALITATIVE COMMENTS"):
            STATE = "QUALITATIVE COMMENTS"
        elif line.startswith("EXTENSIONS AND COMMENTARY"):
            STATE = "EXTENSIONS AND COMMENTARY"
        elif STATE:
            # Append line to the current state section
            entries[COMPOUND_NUMBER][STATE] += line.strip() + " "

    return entries


def save_to_json(data, file_path):
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)


def main():
    # TODO: Don't hardcode paths
    input_file = "Shulgin/data/reports/Pihkal_ascii.txt"
    output_file = "Shulgin/data/reports/Pihkal_ascii_cleaned_cleaned.json"
    compounds = parse_pihkal(input_file)
    save_to_json(compounds, output_file)


if __name__ == "__main__":
    main()

# %%
