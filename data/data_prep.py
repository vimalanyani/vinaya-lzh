import os
import json
import re

def extract_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Extract the file ID from the first line
    id = lines[0].strip()
    
    # Initialize data structure
    data = {"id": id, "sections": []}
    current_section = None
    chinese_buffer = []
    english_buffer = []

    def add_translation():
        if chinese_buffer and english_buffer:
            if current_section is not None:
                current_section['parts'].append({
                    "lzh": chinese_buffer.copy(),
                    "en": english_buffer.copy()
                })
            chinese_buffer.clear()
            english_buffer.clear()

    for line in lines[1:]:  # Skip the first line as it is the file ID
        line = line.strip()
        if line:
            if re.match(r'^[A-Za-z ]+$', line):  # Heading detection
                add_translation()  # Add the previous translation if any
                current_section = {"heading": line, "parts": []}
                data['sections'].append(current_section)
            elif '。' in line:
                add_translation()  # Add the previous translation if any
                chinese_buffer.append(line)
            else:
                english_buffer.append(line)

    add_translation()  # Add the last translation if any

    return data

def save_to_json(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def main(directory_path, output_directory):
    files = sorted(os.listdir(directory_path))
    for i, filename in enumerate(files):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory_path, filename)
            content_data = extract_content(file_path)
            # Determine previous and next files
            content_data['prev'] = files[i-1] if i > 0 else None
            content_data['next'] = files[i+1] if i < len(files) - 1 else None
            output_path = os.path.join(output_directory, f'{os.path.splitext(filename)[0]}.json')
            save_to_json(content_data, output_path)
            print(f'Saved translations to {output_path}')


input_directory = './src'
output_directory = './json'
main(input_directory, output_directory)
