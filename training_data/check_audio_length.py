import wave
import os

def wav_file_length(file_path):
    with wave.open(file_path, 'r') as wav_file:
        frames = wav_file.getnframes()
        rate = wav_file.getframerate()
        duration = frames / float(rate)
        return duration

# Example usage

if os.path.exists(file_path):
    length = wav_file_length(file_path)
    print(f"The duration of the audio file is {length} seconds.")
else:
    print("File does not exist.")
