import dropbox
from dropbox.files import WriteMode

class storage:
    TOKEN = ""
    dbx = ""

    def __init__(this, TOKEN):
        this.TOKEN = TOKEN
        this.dbx = dropbox.Dropbox(TOKEN)
        this.dbx.users_get_current_account()

    def uploadFile(this, file):
        with open(file, 'rb') as f:
            this.dbx.files_upload(f.read(), '/' + file, mode=WriteMode('overwrite'))
            print("Uploaded " + file)
    
    def getFile(this, file):
        # this.dbx.files_restore('/' + file, None)
        this.dbx.files_download_to_file(file, '/' + file, None)
        print("Downloaded " + file)

    
