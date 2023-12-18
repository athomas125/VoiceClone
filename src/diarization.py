import assemblyai as aai
from dotenv import load_dotenv
import os

# Load the environment variables from .env file
load_dotenv()

# Now you can access your API keys
assemblyai_api_key = os.getenv('ASSEMBLYAI_API_KEY')
aai.settings.api_key = assemblyai_api_key

# You can also transcribe a local file by passing in a file path
FOLDER = './Dad_Newscasts'

# iterate over files in
# that directory
i = 0
for filename in os.listdir(FOLDER):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
        i += 1
    if i > 3:
        return

# SEE DOCUMENTATION FOR USAGE
# https://www.assemblyai.com/docs/speech-to-text/speaker-diarization
FILE = FOLDER + '/bt M 10p newscast 12152023.MP3'

config = aai.TranscriptionConfig(speaker_labels=True)

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(
  FILE,
  config=config
)


for utterance in transcript.utterances:
  print(f"Speaker {utterance.speaker}: {utterance.text}")