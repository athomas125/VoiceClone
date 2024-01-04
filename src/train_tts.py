from TTS.tts.configs.shared_configs import BaseDatasetConfig
from TTS.tts.datasets import load_tts_samples
import os

# we use the same path as this script as our training folder.
output_path = os.path.dirname(os.path.abspath(__file__))

dataset_config = BaseDatasetConfig(
    formatter="ljspeech", meta_file_train="training_data.txt", path=os.path.join(output_path, "../")
)

# load training samples
train_samples, eval_samples = load_tts_samples(dataset_config, eval_split=True)
print(len(train_samples))
print(len(eval_samples))