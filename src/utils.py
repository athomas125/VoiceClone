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

def get_assembly_api_key():
    # Load the environment variables from .env file
    load_dotenv('.env.private')

    # Now you can access your API keys
    assemblyai_api_key = os.getenv('ASSEMBLYAI_API_KEY')
    return assemblyai_api_key

def get_hf_api_key():
    # Load the environment variables from .env file
    load_dotenv('.env.private')

    # Now you can access your API keys
    hf_api_key = os.getenv('HF_TOKEN')
    return hf_api_key

import os

def delete_files_with_substring(directory, substring):
    """
    Delete all files in the specified directory that contain the given substring.
    This function does not search in subfolders.

    :param directory: Path to the directory where files are to be searched and deleted.
    :param substring: Substring to search for in file names.
    """
    for filename in os.listdir(directory):
        # Construct full file path
        file_path = os.path.join(directory, filename)

        # Check if it's a file and contains the substring
        if os.path.isfile(file_path) and substring in filename:
            os.remove(file_path)
            print(f"Deleted: {filename}")