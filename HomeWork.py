import dropbox,os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            relative_path = os.path.realpath(local_path,file_from)
            dropbox_path = os.path.join(file_to,relative_path)
        with open(local_path,'rb') as f:
            dbx.files_upload(f.read(),dropbox_path,mode = WriteMode('overwrite'))
def main():
    access_token = 'sl.AztNpg-inn1XSn1sQe3aa-sl.Az8zbml7qoaf2pKJ70NKVr5-5Rxwv0YP26D_zT-BlOzSM7i5nfX3xJl9ovTfZEbE_NBbY0S1NYtNqL1Oj17rRi1IU-9vN9Xr1XgDDdQmfbaZ8rPbDvqGQV1WQ1Q3uCKfHRXPhkKwg9Ml'
    transferData = TransferData(access_token)
    file_from = input("write the file name which you want to upload")
    file_to = '/'+ file_from
    transferData.upload_file(file_from, file_to)
main()