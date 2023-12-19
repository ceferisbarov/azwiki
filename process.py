import os
import re
import json

MIN_LENGTH = 250

def process_wiki(text):
    text = re.sub(r'\n','', text) # Remove newline characters
    text = re.sub(r'\t', '', text) # Remove tab characters
    text = re.sub(r'\([^)]*\)', '', text) # Remove between ()
    text = re.sub(r'==\s*İstinadlar\s*==[\s\S]*', '', text) # Remove everything after headline
    text = re.sub(r'==\s*Həmçinin bax\s*==[\s\S]*', '', text)
    text = re.sub(r'==\s*Qalereya\s*==[\s\S]*', '', text)
    text = re.sub(r'==\s*Mənbə\s*==[\s\S]*', '', text)
    text = re.sub(r'==\s*Tanınmış işləri\s*==[\s\S]*', '', text)
    text = re.sub(r'==\s*Xarici keçidlər\s*==[\s\S]*', '', text)
    text = re.sub(r'==\s*Filmoqrafiya\s*==[\s\S]*', '', text)
    text = re.sub(r'==\s*Tanınmış nümayəndələri\s*==[\s\S]*', '', text)
    text = re.sub(r'==\s*Mükafatları\s*==[\s\S]*', '', text)
    text = re.sub(r'==.*?==', '\n', text) # Remove everthing between ==
    text = re.sub(r'\/[^\/]*\/', '', text) # Remove between //
    text = re.sub(r'Fayl:[^.]*\.', '', text) # Remove descriptive words
    text = re.sub(r'Şəkil:[^.]*\.', '', text)
    text = re.sub(r'Misallar[^.]*\.', '', text)
    text = re.sub(r'[^a-zA-Z0-9\sƏəŞşÇçĞğÖöIıÜüİi,.?!:;\-]+', '', text) # Remove everything except alnum
    text = re.sub(r'<.*?>', '', text) # Remove between <>
    text = re.sub(r'https?:\/\/\S+', '', text) # Remove all the links
    text = re.sub(r' +', ' ', text) # Remove multiple space with single

    return text

pattern = r"''\w+''\s+''\w+''"
# path to the folder containing the text files
folder_path = "raw"
# path to the folder to save the processed files
output_folder_path = "processed"

# create the output folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# iterate through all the text files in the folder
for i, file_name in enumerate(os.listdir(folder_path)):
    # check if the file is a text file
    if file_name.endswith(".json"):
        # read the contents of the file
        with open(os.path.join(folder_path, file_name), "r") as f:
            content = json.load(f)

        # check if the file matches the regex pattern
        # if not (re.search(pattern, text) or "**" in text):
            # if the file does not match the pattern, processed the text
        processed_text = process_wiki(content["text"])

        # write the cleaned text back to the file
        if "." in processed_text and len(processed_text) >= MIN_LENGTH:
            content["text"] = processed_text
            with open(os.path.join(output_folder_path, file_name), "w") as f:
                json.dump(content, f, ensure_ascii=False)

            # print(f"Cleaned text no. {i}")
    else:
        print(file_name)
