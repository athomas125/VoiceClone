import utils as u
# Usage
source_directory = "training_data"
destination_directory = "training_data/wavs"

# Copy all files from source_directory to destination_directory
u.loop_thru_files_w_func(source_directory, u.copy_file_to_directory, dest_directory=destination_directory)