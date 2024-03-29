import utils as u
import os
from pydub import AudioSegment
import json
import random

def get_timestamps(audio_file):
    json_name = audio_file.split('/')[-1].split('_')[-3] + '.json'
    json_path = os.path.join('whisper_diarized', json_name)
    audio = AudioSegment.from_file(audio_file)
    out_file = "fractured_data.txt"
    output_base = audio_file.split('/')[-1].split('_')[-3]
    with open(json_path) as f:
        with open(out_file, "a", encoding='utf-8') as of:
            contents = json.load(f)
            start = 0
            i = 0
            for segment in contents['segments']:
                end = segment['end'] - segment['start'] + start
                # Extract the segment of the audio
                audio_clip = audio[start*1000:end*1000]
                start = end
                # Export the concatenated segments to a single file
                out_path = os.path.join('training_data', f"{output_base}_{i}.wav")
                if i > 0 or random.randint(0, 1000) > 999:
                    audio_clip.export(out_path, format='wav')
                    i += 1
                    of.write(f"{out_path}|{segment['text']}|{segment['text']}\n")
                else:
                    i += 1

u.loop_thru_files_w_func('demucs_separated', get_timestamps)