import os
import dotenv
import dropbox

# Load environment variables
dotenv.load_dotenv()
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN1')

# Initialize Dropbox client
d = dropbox.Dropbox(ACCESS_TOKEN)

# Directory containing files to upload
local_directory = 'files'
"""
# The os.listdir() method in Python is used to get the list of
# all files and directories in the specified directory
"""
# iterate thur each file.
for filename in os.listdir(local_directory):
    # build a full local path
    local_path = os.path.join(local_directory,filename)
    #os.path.join() to join path components intelligently and
    # handle file paths safely in Python

    """returns True if path refers to an existing regular file or 
    an open file descriptor"""
    if os.path.isfile(local_path):

        with open(local_path, 'rb') as file:
            content = file.read()
            # Upload to Dropbox with the same filename
            dropBox_path = f'/{filename}'
            d.files_upload(content,
                       dropBox_path,
                       mode=dropbox.files.WriteMode('overwrite'))

            print(f'File {local_path} was uploaded to the drive')
