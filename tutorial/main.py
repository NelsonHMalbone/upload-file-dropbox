import dropbox
import os
import dotenv

# load all variable in dotenv file
dotenv.load_dotenv()

# all caps or 'constant' variable because the value never changes
# provid the key from the .env file.
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

# Dropbox is a class of dropbox library
# will access the Access_token as input
# store in a varible to applie to other files?
d = dropbox.Dropbox(ACCESS_TOKEN)

# cxan and better idea to automate so place file path in a variable
filepath = 'IMG_3621.JPG'

# open file that needs to be uploaded to create python file object
with open(filepath, 'rb') as file:
    # will give us the binery content of file
    content = file.read()
    # want to store file as og name
    # this file will be store in the app/appname fold in the drive
    # mode will over the file if name is the same
    d.files_upload(content, f'/{filepath}', mode=dropbox.files.WriteMode('overwrite'))
    # print a upload comformation
    print(f'File {filepath} was uploaded to the drive')