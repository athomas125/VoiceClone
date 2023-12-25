import os 
import shutil

directory = './cropped_audio'
tracking_file = "spleeter_output.txt"
output_dir = "spleeter_output"
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
        os.system(f"spleeter separate -p spleeter:2stems -o {output_dir} '{audio_file}'")
        output_folder = output_dir + '/' + filename.split('.')[0]
        os.remove(os.path.join(output_folder, 'accompaniment.wav'))
        shutil.move(os.path.join(output_folder, 'vocals.wav'), os.path.join(output_dir, filename.split('.')[0] + '_vocals.wav'))
        shutil.rmtree(output_folder)
        
        with open(tracking_file, "a", encoding="utf-8") as tf:
            print(f"separated: {audio_file}!!")
            tf.write(f"{audio_file}\n")
    else:
        print(f"Skipped {audio_file}")