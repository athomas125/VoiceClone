import torch
from TTS.api import TTS

OUTPUT_PATH = "generated_clips/long_run_glow.wav"

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"
# /home/hice1/athomas314/.local/share/tts/tts_models--en--ljspeech--glow-tts
# Init TTS with the target model name
tts = TTS(model_path="/storage/ice1/9/0/athomas314/VoiceClone/src/best_raw_model/best_model_3240.pth", config_path="/storage/ice1/9/0/athomas314/VoiceClone/src/best_raw_model/config.json", progress_bar=False).to(device)
tts.is_multi_lingual = False
# Run 
tts.tts_to_file(text="AP News, I'm Ben Thomas. This just in, AP News Anchor Ben Thomas has been replaced by a digital entity that is weaponizing his likeness for unknown purposes.", file_path=OUTPUT_PATH)