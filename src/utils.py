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


def create_directory_and_tracking_file(output_dir, tracking_file):
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)


    updated_files = set()

    if os.path.isfile(tracking_file):
        with open(tracking_file, "r", encoding="utf-8") as tf:
            for line in tf:
                updated_files.add(line.strip())
    else:
        with open(tracking_file, "w", encoding="utf-8") as fp:
            print(f"tracking file created at {tracking_file}")
    return updated_files

def loop_thru_files_w_func(directory, func, skip_tracking_file=None, skip_set=None, *args, **kwargs):
    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)
        if os.path.isfile(file) and skip_set is not None and file not in skip_set:
            func(file, *args, **kwargs)

            if skip_tracking_file is not None:
                with open(skip_tracking_file, "a", encoding="utf-8") as tf:
                    print(f"processed: {file}!!")
                    tf.write(f"{file}\n")
        else:
            print(f"Skipped {file}")

def loop_thru_folders_w_func(directory, func, skip_tracking_file=None, skip_set=None, *args, **kwargs):
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isdir(path) and skip_set is not None and path not in skip_set:
            func(path, *args, **kwargs)

            if skip_tracking_file is not None:
                with open(skip_tracking_file, "a", encoding="utf-8") as tf:
                    print(f"processed: {file}!!")
                    tf.write(f"{file}\n")
        else:
            print(f"Skipped {file}")