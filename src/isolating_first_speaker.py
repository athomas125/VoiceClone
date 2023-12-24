import os
import json

i = 0
directory = "./whisper_diarized"
tracking_file = "whisper_speaker_selection.txt"
output_dir = "./whisper_diarized"
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)


updated_files = set()

if os.path.isfile(tracking_file):
    with open(tracking_file, "r", encoding="utf-8") as tf:
        for line in tf:
            updated_files.add(line.strip())
else:
    with open(tracking_file, "w", encoding="utf-8") as fp:
        print(f"tracking file created at {tracking_file}")


for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(file) and file not in updated_files:
        write = False
        with open(file) as f:
            contents = json.load(f)
            new_contents = {'segments': []}
            i = 0
            for segment in contents['segments']:
                if 'speaker' in segment:
                    write = True
                    new_segment = {}
                    if i == 0:
                        speaker_og = segment['speaker']
                    if segment['speaker'] == speaker_og:
                        new_segment['start'] = segment['start']
                        new_segment['end'] = segment['end']
                        new_segment['text'] = segment['text']
                        new_contents['segments'].append(new_segment)
                    i += 1
        if write:
            with open(file, 'w', encoding='utf-8') as f:
                json.dump(new_contents, f, ensure_ascii=False, indent=4)


        with open(tracking_file, "a", encoding="utf-8") as tf:
            print(f"updated: {file}!!")
            tf.write(f"{file}\n")
    else:
        print(f"Skipped {file}")
