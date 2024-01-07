import os 

curpath = os.path.dirname(os.path.abspath(__file__))
with open("training_data/training_data.txt", "r", encoding="utf-8") as fp1:
    with open("training_data/training_data_2.txt", "w", encoding="utf-8") as fp2:
        for line in fp1:
            filename = "wavs/" + line.split("|")[0] + ".wav"
            path = os.path.join(curpath, filename)
            if os.path.isfile(path):
                fp2.write(line)