import assemblyai as aai
from dotenv import load_dotenv
import os

# Load the environment variables from .env file
load_dotenv()

# Now you can access your API keys
assemblyai_api_key = os.getenv('ASSEMBLYAI_API_KEY')
print(assemblyai_api_key)
aai.settings.api_key = assemblyai_api_key

audio_url = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"

config = aai.TranscriptionConfig(auto_chapters=True)

transcript = aai.Transcriber().transcribe(audio_url, config)

for chapter in transcript.chapters:
  print(f"{chapter.start}-{chapter.end}: {chapter.headline}")