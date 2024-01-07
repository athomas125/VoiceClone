import os
from mutagen.wave import WAVE
import wave

curpath = os.path.dirname(os.path.abspath(__file__))
# Path to your training data file
training_data_file = path = os.path.join(curpath, "training_data.txt")
# Directory containing your audio files
audio_files_directory = "training_data/wavs"

def wav_file_length(file_path):
    with wave.open(file_path, 'r') as wav_file:
        frames = wav_file.getnframes()
        rate = wav_file.getframerate()
        duration = frames / float(rate)
        return duration

def check_audio_files(training_data_file, audio_files_directory):
    lengths = []
    lines = set()
    cnt = 0
    with open(training_data_file, "r") as file:
        # with open("training_data/training_data_2.txt", "w") as fp:
        for line in file:
            cnt += 1
            if line not in lines:
                lines.add(line)
            else:
                continue
            # Assuming your training_data.txt has the format: text|audio_file_path|speaker_name
            # Modify as per your file's format
            audio_file_path = line.strip().split("|")[0] + '.wav'
            full_path = os.path.join(audio_files_directory, audio_file_path)

            # Check if file exists
            if not os.path.exists(full_path):
                print(f"File not found: {full_path}")
                continue
            
            audio_length = wav_file_length(full_path)
            if audio_length > 14:
                print(audio_length, full_path)
                
            # if wav_file_length(full_path) < 1:
            #     os.remove(full_path)
            #     print(f"{full_path} removed, too short")
            #     continue
            # Check if it's a valid WAV file
            try:
                # audio = WAVE(full_path)
                if len(line.split('|')) > 3:
                    line = '|'.join(line.split('|')[0:3])+'\n'
                # fp.write(line)
            except Exception as e:
                print(f"Error in file {full_path}: {e}")
    print(len(lines))
    print(cnt)

# Run the check
check_audio_files(training_data_file, audio_files_directory)
