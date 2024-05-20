import os
import json
import re
import argparse
import copy

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


def is_open_grouping_info_line(lang, line):
    if line is None:
        return False
    regex = re.compile(rf"<{lang}-(fascicle|division)-(start|end)>")
    return re.match(regex, line)


def is_close_grouping_info_line(lang, line):
    if line is None:
        return False
    regex = re.compile(rf".*</{lang}-(fascicle|division)-(start|end)>")
    return re.match(regex, line)


def is_h2_line(line):
    if line is None:
        return False
    regex = re.compile(r"<h2>")
    return re.match(regex, line)


def is_open_lzh_line(line):
    if line is None:
        return False
    regex = re.compile(r"<lzh>")
    return re.match(regex, line)


def is_close_lzh_line(line):
    if line is None:
        return False
    regex = re.compile(r".*<\/lzh>")
    return re.match(regex, line)


def is_open_verse_line(line):
    if line is None:
        return False
    regex = re.compile(r"<verse>")
    return re.match(regex, line)


def is_close_verse_line(line):
    if line is None:
        return False
    regex = re.compile(r".*<\/verse>")
    return re.match(regex, line)


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
        "h2": "",
        "lzh": [],
        "en": [],
        "en_verse": [],
        "lzh_grouping_info": [],
        "en_grouping_info": [],
    }

    is_first_section = True

    lzh_buffer = []
    en_buffer = []
    h2_buffer = ""
    en_verse_buffer = []
    lzh_grouping_info_buffer = []
    en_grouping_info_buffer = []

    def add_body_section_and_reset():
        section = section_model.copy()

        if is_first_section is not True:
            section["lzh"] = lzh_buffer
            section["en"] = en_buffer
            section["h2"] = h2_buffer
            section["en_verse"] = en_verse_buffer
            section["lzh_grouping_info"] = lzh_grouping_info_buffer
            section["en_grouping_info"] = en_grouping_info_buffer

            data["body"].append(copy.deepcopy(section))

        lzh_buffer.clear()
        en_buffer.clear()
        en_verse_buffer.clear()
        lzh_grouping_info_buffer.clear()
        en_grouping_info_buffer.clear()

    buffering_lzh = False
    buffering_en_verse = False
    buffering_lzh_grouping_info = False
    buffering_en_grouping_info = False

    for line in lines[1:]:  # Skip the first line as it is the file ID
        line = line.strip()

        if line:
            if is_open_grouping_info_line("lzh", line):
                add_body_section_and_reset()  # Add the previous translation if any
                is_first_section = False

                if is_close_grouping_info_line("lzh", line):
                    buffering_lzh_grouping_info = False
                else:
                    buffering_lzh_grouping_info = True

                lzh_grouping_info_buffer.append(re.sub(r"<\/?lzh.*?>", "", line))

            elif is_close_grouping_info_line("lzh", line):
                buffering_lzh_grouping_info = False
                lzh_grouping_info_buffer.append(re.sub(r"<\/?lzh.*?>", "", line))

            elif buffering_lzh_grouping_info:
                lzh_grouping_info_buffer.append(line)

            elif is_open_grouping_info_line("en", line):
                if is_close_grouping_info_line("en", line):
                    buffering_en_grouping_info = False
                else:
                    buffering_en_grouping_info = True
                en_grouping_info_buffer.append(re.sub(r"<\/?en.*?>", "", line))

            elif is_close_grouping_info_line("en", line):
                buffering_en_grouping_info = False
                en_grouping_info_buffer.append(re.sub(r"<\/?en.*?>", "", line))

            elif buffering_en_grouping_info:
                en_grouping_info_buffer.append(re.sub(r"<\/?en.*?>", "", line))

            elif is_h2_line(line):
                add_body_section_and_reset()  # Add the previous translation if any
                is_first_section = False
                h2_buffer = re.sub(r"<\/?h2>", "", line)

            elif is_open_lzh_line(line):
                if is_close_lzh_line(line):
                    buffering_lzh = False
                else:
                    buffering_lzh = True
                lzh_buffer.append(re.sub(r"<\/?lzh>", "", line))

            elif is_close_lzh_line(line):
                buffering_lzh = False
                lzh_buffer.append(re.sub(r"<\/?lzh>", "", line))

            elif buffering_lzh:
                lzh_buffer.append(line)

            elif is_open_verse_line(line):
                if is_close_verse_line(line):
                    buffering_en_verse = False
                else:
                    buffering_en_verse = True
                en_verse_buffer.append(re.sub(r"<\/?verse>", "", line))

            elif is_close_verse_line(line):
                buffering_en_verse = False
                en_verse_buffer.append(re.sub(r"<\/?verse>", "", line))

            elif buffering_en_verse:
                en_verse_buffer.append(line)

            else:
                en_buffer.append(line)

    add_body_section_and_reset()  # Add the last translation if any

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
