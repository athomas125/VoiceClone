import torch
from TTS.api import TTS

OUTPUT_PATH = "generated_clips/tacotron_DDC_baseline.wav"

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Init TTS with the target model name
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False).to(device)
# Run TTS
tts.tts_to_file(text="AP News, I'm Ben Thomas. This just in, AP News Anchor Ben Thomas has been replaced by a digital entity that is weaponizing his likeness for unknown purposes.", file_path=OUTPUT_PATH)