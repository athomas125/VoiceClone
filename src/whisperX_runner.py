import os
import utils as u
import shutil

api_key = u.get_hf_api_key()

i = 0
directory = './Dad_Newscasts'
tracking_file = "whisper_diarized.txt"
output_dir = "whisper_diarized"
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)


transcribed_files = set()

if os.path.isfile(tracking_file):
    with open(tracking_file, "r", encoding="utf-8") as tf:
        for line in tf:
            transcribed_files.add(line.strip())
else:
    with open(tracking_file, "w", encoding="utf-8") as fp:
        print(f"tracking file created at {tracking_file}")


for filename in os.listdir(directory):
    audio_file = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(audio_file) and audio_file not in transcribed_files:
        # Replace 'your_command' with the command you want to run
        os.system(f"whisperx --model Systran/faster-whisper-large-v3 --language en --diarize --min_speakers 2 --hf_token {api_key} '{audio_file}'")
        
        prefix = filename.split('.')[0]
        output_file = prefix + '.json'
        if os.path.isfile(output_file):
            shutil.move(output_file, os.path.join(output_dir, output_file))
        u.delete_files_with_substring('./', prefix)

        with open(tracking_file, "a", encoding="utf-8") as tf:
            print(f"transcribed: {audio_file}!!")
            tf.write(f"{audio_file}\n")
    else:
        print(f"Skipped {audio_file}")

"""
import whisperx
import gc
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
batch_size = 16 # reduce if low on GPU mem
compute_type = "float16" # change to "int8" if low on GPU mem (may reduce accuracy)

# 1. Transcribe with original whisper (batched)
model = whisperx.load_model("Systran/faster-whisper-large-v3", device, compute_type=compute_type)

# save model to local path (optional)
model_dir = "./models/"
model = whisperx.load_model("large-v2", device, compute_type=compute_type, download_root=model_dir)

audio = whisperx.load_audio(audio_file)
result = model.transcribe(audio, batch_size=batch_size)
print(result["segments"]) # before alignment

# delete model if low on GPU resources
gc.collect(); torch.cuda.empty_cache(); del model

# 2. Align whisper output
model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device)
result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)

print(result["segments"]) # after alignment

# delete model if low on GPU resources
import gc; gc.collect(); torch.cuda.empty_cache(); del model_a

# 3. Assign speaker labels
diarize_model = whisperx.DiarizationPipeline(use_auth_token=YOUR_HF_TOKEN, device=device)

# add min/max number of speakers if known
diarize_segments = diarize_model(audio)
# diarize_model(audio, min_speakers=min_speakers, max_speakers=max_speakers)

result = whisperx.assign_word_speakers(diarize_segments, result)
print(diarize_segments)
print(result["segments"]) # segments are now assigned speaker IDs
"""