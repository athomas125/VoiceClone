import librosa
import soundfile as sf
import utils as u

def downsample_wav(file_path):
    audio, sample_rate = librosa.load(file_path, sr=22050)  # Loads file at 22050 Hz

    sf.write(file_path, audio, 22050)

u.loop_thru_files_w_func("demucs_fractured/", downsample_wav)