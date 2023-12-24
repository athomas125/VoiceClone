# https://stackoverflow.com/questions/75733809/how-to-crop-an-audio-file-based-on-the-timestamps-present-in-a-list
from pydub import AudioSegment
import os
import json
import utils as u

def trim_audio(intervals, input_file_path, output_file_path):
    # load the audio file
    audio = AudioSegment.from_file(input_file_path)
    
    # Initialize an empty audio segment for concatenation
    concatenated_segment = AudioSegment.silent(duration=0)
    
    # iterate over the list of time intervals
    for start_time, end_time in intervals:
        # Extract the segment of the audio
        segment = audio[start_time*1000:end_time*1000]

        # Concatenate this segment to the previous segments
        concatenated_segment += segment
    
    # Export the concatenated segments to a single file
    concatenated_segment.export(output_file_path, format='mp3')

directory = "./Dad_Newscasts"
transcript_dir = "./whisper_diarized"
audio_tracking_file = "cropped_audio.txt"
audio_output_dir = "./cropped_audio"
text_tracking_file = "cropped_text.txt"
text_output_dir = "./cropped_text"

updated_audio_files = u.create_directory_and_tracking_file(audio_output_dir, audio_tracking_file)
updated_text_files = u.create_directory_and_tracking_file(text_output_dir, text_tracking_file)

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    prefix = filename.split('.')[0]
    audio_out_path = os.path.join(audio_output_dir, prefix + "_trimmed.MP3")
    text_out_path = os.path.join(text_output_dir, prefix + "_trimmed.txt")
    time_stamps_path = os.path.join(transcript_dir, prefix + ".json")
    if file not in updated_text_files:
        if os.path.isfile(time_stamps_path):
            with open(time_stamps_path) as fp:
                contents = json.load(fp)
                with open(text_out_path, "a", encoding="utf-8") as fp:
                    for segment in contents['segments']:
                        fp.write(f"{segment['text']} ")
            with open(text_tracking_file, "a", encoding="utf-8") as ttf:
                print(f"text_updated: {file}!!")
                ttf.write(f"{file}\n")
    else:
        print(f"Skipped {filename}, text already updated")
        
    timestamps = []
    if file not in updated_audio_files:
        if os.path.isfile(time_stamps_path):
            with open(time_stamps_path) as fp:
                contents = json.load(fp)
                for segment in contents['segments']:
                    timestamps.append([segment['start'], segment['end']])
            trim_audio(timestamps, file, audio_out_path)
            with open(audio_tracking_file, "a", encoding="utf-8") as atf:
                print(f"audio updated: {file}!!")
                atf.write(f"{file}\n")
        else:
            print(f"Skipped {filename}, no time stamps file")
    else:
        print(f"Skipped {filename}, audio already updated")