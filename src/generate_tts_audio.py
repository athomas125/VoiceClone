import torch
from TTS.api import TTS

OUTPUT_PATH = "generated_clips/first_run_glow.wav"

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Init TTS with the target model name
tts = TTS(model_path="/storage/ice1/9/0/athomas314/VoiceClone/src/run-January-07-2024_10+53AM-1d78a73/best_model_4310.pth", config_path="/storage/ice1/9/0/athomas314/VoiceClone/src/run-January-07-2024_10+53AM-1d78a73/config.json", progress_bar=False).to(device)
tts.is_multi_lingual = False
# Run 
tts.tts_to_file(text="AP News, I'm Ben Thomas. This just in, AP News Anchor Ben Thomas has been replaced by a digital entity that is weaponizing his likeness for unknown purposes.", file_path=OUTPUT_PATH)