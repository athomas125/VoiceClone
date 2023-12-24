import utils as u
import os

# You can also transcribe a local file by passing in a file path
directory = './Dad_Newscasts'

# iterate over files in
# that directory
api_key = u.get_assembly_api_key()
i = 0
diarization_directory = './Diarized_Transcripts'
tracking_file = "transcribed_files.txt"
transcribed_files = set()
with open(tracking_file, "r", encoding="utf-8") as tf:
    for line in tf:
        transcribed_files.add(line.strip())

for filename in os.listdir(directory):
    txt_file = filename.replace("MP3", "txt")
    txt_f = os.path.join(diarization_directory, txt_file)
    file = os.path.join(directory, filename)
    
    # checking if it is a file
    if os.path.isfile(file) and file not in transcribed_files:
        diary = u.get_diarization(file, api_key)
        
        with open(txt_f, "w") as fp:
            for utterance in diary.utterances:
                if utterance.speaker == "A":
                    fp.write(utterance.text)
                    fp.write("\n")
                
        with open(tracking_file, "a", encoding="utf-8") as tf:
            print(f"transcribed: {file}!!")
            tf.write(f"{file}\n")
    else:
        print(f"Skipped {file}")