import os
import json
import re
import argparse

#  WORKING NOTES # header features (modeled on Mahāsaṅghika Vinaya) (eg pj1)
# - "摩訶僧祇律卷第" (fascicle indicator)
# - appears at at beginning AND end of each fascicle)
#  "東晉天竺三藏佛陀跋陀羅共法顯譯" - (Translated by info - ALWAYS THE SAME)
# fascicle end eg. ss11

# "明" - (AT START OF LINE ONLY) marker for "beginning of explanation" (eg pd1-8)

# subheadings "Story", "Ruling", "Explanation", "Verse"

# Rule beginning marker "Origin Story" (*reasonably* reliable)
# note marker "(<note:.*?>)" -(reliable)
# is chinese "。" (reliable)

# pc1-70
# custom handling

# notes
# - po files for pm seperate handling
# specific handling for gd, pn
# `\p{Han}` This assumes that your regex compiler meets requirement RL1.2 Properties from UTS#18 Unicode Regular Expressions. Perl and Java 7 both meet that spec, but many others do not.
# `\p{script=Han}`
# "verses:"


parser = argparse.ArgumentParser(description="Process text files to JSON.")
parser.add_argument(
    "--input_dir", type=str, help="The input directory containing the text files."
)
parser.add_argument(
    "--output_dir",
    type=str,
    help="The output directory where the JSON files will be saved.",
)
parser.add_argument(
    "--school", type=str, help="The name of the school the vinaya texts are from."
)
parser.add_argument(
    "--book", type=str, help="The name of the vinaya book the texts are from."
)

args = parser.parse_args()


rule_classes = {
    "pj": "Expulsion",
    "ss": "Suspension",
    "np": "Relinquishment With Confession",
    "pc": "Confession",
    "pd": "Acknowledgment",
    "sk": "Rules for Training",
    "as": "Settling Legal Issues",
}


def is_fascicle_start_lzh_start_line(line):
    if line is None:
        return False
    heading_regex = re.compile(r"<lzh>摩訶僧祇律卷第.*(?!</lzh>$)")
    return re.match(heading_regex, line)


def is_fascicle_start_lzh_end_line(line):
    if line is None:
        return False
    heading_regex = re.compile(r"</lzh>")
    return re.match(heading_regex, line)


def is_fascicle_end_lzh_line(line):
    if line is None:
        return False
    heading_regex = re.compile(r"<lzh>摩訶僧祇律卷第.*</lzh>")
    return re.match(heading_regex, line)


def is_h2_line(line):
    if line is None:
        return False
    heading_regex = re.compile(r"<beginh2>")
    return re.match(heading_regex, line)


def is_lzh_start_line(line):
    if line is None:
        return False
    is_lzh_start_regex = re.compile(r"<lzh>")
    return re.match(is_lzh_start_regex, line)


def is_lzh_end_line(line):
    if line is None:
        return False
    is_lzh_end_regex = re.compile(r"</lzh>")
    return re.match(is_lzh_end_regex, line)


def coerce_paragraphs(lines):
    split_lines = []
    previous_line_has_note = False

    for line in lines:
        if line.startswith("<"):
            split_lines[len(split_lines) - 1] = (
                split_lines[len(split_lines) - 1] + " " + line
            )
            previous_line_has_note = True
        elif previous_line_has_note:
            split_lines[len(split_lines) - 1] = (
                split_lines[len(split_lines) - 1] + " " + line
            )
            previous_line_has_note = False
        else:
            # TODO: REMOVE LINE SPLITTING
            separated_lines = re.split(r"(\s*—?“.+?”)", line.strip())
            split_lines.extend(separated_lines)

    split_lines = [line.strip() for line in split_lines if line]
    return split_lines


def parse_txt_content(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Extract the file ID from the first line
    id = lines[0].strip()

    # Initialize data structure
    data = {
        "id": id,
        "school": args.school,
        "book": args.book,
        "rule_class": rule_classes[id[5:7]],
        "rule_no": id[7:],
        "body": [],
    }

    section_model = {
        "division_start_lzh": [],
        "division_start_en": [],
        "h2": "",
        "lzh": [],
        "en": [],
        "division_end_lzh": [],
        "division_end_en": [],
    }

    current_section = None
    chinese_buffer = []
    english_buffer = []

    def add_translation():
        if chinese_buffer and english_buffer:
            en = []

            for line in english_buffer:
                note_separated_lines = re.split(r"(<note:.*?>)", line)
                paragraphs = coerce_paragraphs(note_separated_lines)
                en.extend(paragraphs)

            if current_section is not None:
                current_section["parts"].append(
                    {"lzh": chinese_buffer.copy(), "en": en}
                )
            chinese_buffer.clear()
            english_buffer.clear()

    previous_line = None

    for line in lines[1:]:  # Skip the first line as it is the file ID
        line = line.strip()
        if line:
            if is_fascicle_start_lzh_start_line(line):
                add_translation()  # Add the previous translation if any
                current_section = {"h2": line, "parts": []}
                data["body"].append(current_section)
            elif "。" in line:
                add_translation()  # Add the previous translation if any
                chinese_buffer.append(line)
            else:
                english_buffer.append(line)
        previous_line = line

    # for line in lines[1:]:  # Skip the first line as it is the file ID
    #     line = line.strip()
    #     if line and previous_line is not None:
    #         if len(previous_line) == 0 and is_heading_line(line):
    #             add_translation()  # Add the previous translation if any
    #             current_section = {"heading": line, "parts": []}
    #             data["body"].append(current_section)
    #         elif "。" in line:
    #             add_translation()  # Add the previous translation if any
    #             chinese_buffer.append(line)
    #         else:
    #             english_buffer.append(line)
    #     previous_line = line

    add_translation()  # Add the last translation if any

    return data


def save_to_json(data, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def extract_id_from_filename(filename):
    id = filename.strip(".txt")
    return id.split("_")[-1]


def main(directory_path, output_directory):
    files = sorted(os.listdir(directory_path))
    for i, filename in enumerate(files):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)

            content_data = parse_txt_content(file_path)

            # add prev/next data
            content_data["file"] = extract_id_from_filename(filename)
            content_data["prev_file"] = (
                extract_id_from_filename(files[i - 1]) if i > 0 else None
            )
            content_data["next_file"] = (
                extract_id_from_filename(files[i + 1]) if i < len(files) - 1 else None
            )

            output_path = os.path.join(
                output_directory, f"{os.path.splitext(filename)[0]}.json"
            )
            save_to_json(content_data, output_path)
            print(f"Saved translations to {output_path}")


input_directory = args.input_dir
output_directory = args.output_dir
main(input_directory, output_directory)
