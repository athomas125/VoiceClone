import assemblyai as aai
from dotenv import load_dotenv
import os

def get_diarization(filepath, api_key):

    # SEE DOCUMENTATION FOR USAGE
    # https://www.assemblyai.com/docs/speech-to-text/speaker-diarization
    aai.settings.api_key = api_key
    config = aai.TranscriptionConfig(speaker_labels=True)

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(
    filepath,
    config=config
    )

    return transcript

  
def get_chapters(filepath, api_key):

    aai.settings.api_key = api_key

    config = aai.TranscriptionConfig(auto_chapters=True)

    transcript = aai.Transcriber().transcribe(filepath, config)

    return transcript

def get_api_key():
    # Load the environment variables from .env file
    load_dotenv('.env.private')

    # Now you can access your API keys
    assemblyai_api_key = os.getenv('ASSEMBLYAI_API_KEY')
    return assemblyai_api_key