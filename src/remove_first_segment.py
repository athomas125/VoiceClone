import utils as u
import os
from pydub import AudioSegment
import json
import random

def get_timestamps(audio_file):
    json_name = audio_file.split('/')[-1].split('_')[-3] + '.json'
    json_path = os.path.join('whisper_diarized', json_name)
    audio = AudioSegment.from_file(audio_file)
    out_file = "full_audio.txt"
    output_base = audio_file.split('/')[-1].split('_')[-3]
    with open(json_path) as f:
        with open(out_file, "a", encoding='utf-8') as of:
            contents = json.load(f)
            start = 0
            i = 0
            if len(contents['segments'])>=2:
                start = contents['segments'][1]['start']
                end = contents['segments'][-1]['end']
                audio_clip = audio[start*1000:end*1000]
                out_path = os.path.join('full_sampled_data', f"{output_base}.wav")
                audio_clip.export(out_path, format='wav')

u.loop_thru_files_w_func('demucs_separated', get_timestamps)