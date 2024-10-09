import os
import subprocess

# Define the folder containing your SRT files
srt_folder = 'srt'

# Iterate over all files in the folder
for filename in os.listdir(srt_folder):
    if filename.endswith('.srt'):
        # Construct the file path
        file_path = os.path.join(srt_folder, filename)
        
        # Construct the command
        command = f'python __main__.py --to uk "{file_path}"'
        
        # Execute the command
        subprocess.run(command, shell=True)
        print(f'Processed: {file_path}')
