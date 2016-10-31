class main_dropbox:
    def __init__(self,app_key,app_secret,access_token,loalpath,remotepath):
        self.app_key=app_key;self.app_secret=app_secret;
        self.access_token=access_token;
        self.loalpath=loalpath;self.remotepath=remotepath
    def main_dropbox(self,localpath,remotepath):

        import dropbox
        from dropbox import session
        # # from session import BaseSession
        # s=session.BaseSession

        # Get your app key and secret from the Dropbox developer website
        # app_key = 'INSERT_APP_KEY'
        # app_secret = 'INSERT_APP_SECRET'
        flow = dropbox.client.DropboxOAuth2FlowNoRedirect(self.app_key, self.app_secret)

        # Have the user sign in and authorize this token
        authorize_url = flow.start()
        print '1. Go to: ' + authorize_url
        print '2. Click "Allow" (you might have to log in first)'
        print '3. Copy the authorization code.'

        # code = raw_input("Enter the authorization code here: ").strip()
        # # This will fail if the user enters an invalid authorization code
        # access_token, user_id = flow.finish(code)

        client = dropbox.client.DropboxClient(self.access_token)
        print 'linked account: ', client.account_info()

        # fh = open("small_test_file.txt","w")
        # fh.write("Small test file")
        # fh.write("Small test file")
        # fh.close()


        try:
	        CurrentDir=os.path.dirname(os.path.realpath(__file__))
	        Parent_Dir=os.path.abspath(os.path.join(CurrentDir, '..'))
        # Destination= os.path.abspath(os.path.join(Parent_Dir, '..'))

        except:
	        CurrentDir=os.getcwd()
	        Parent_Dir=os.path.abspath(os.path.join(CurrentDir, '..'))

        for root, dirs, files in os.walk(CurrentDir):
            curent_path0=root.split(Parent_Dir)[1]+'/'
            curent_path=curent_path0.replace('\\','/')
            root=root.replace('\\','/')
            for dir2 in dirs:
                # if os.path.isdir(Destination+ curent_path+dir2):
                # client.file_create_folder('/'+dir2)
                pass

        #uploading file
        f = open(localpath, 'rb')
        response = client.put_file(remotepath, f,True)
        print "/n uploaded:", response
        f.close()
        # link=dropbox.client.DropboxClient(access_token).share('/magnum-opus.txt')
        link=client.share(remotepath)
        print "/n share_link:", link
        return link

    def download(self):
        #downloading files
        f, metadata = client.get_file_and_metadata('/magnum-opus.txt')
        out = open('magnum-opus.txt', 'wb')
        out.write(f.read())
        out.close()
        print metadata


def my_dropbox(email, password, localpath, remotepath):
    from dbupload import DropboxConnection
    from getpass import getpass

    # email = raw_input("Enter Dropbox email address:")
    # password = getpass("Enter Dropbox password:")

    # Create a little test file
    # fh = open("small_test_file.txt","w")
    # fh = open("small_test_file.txt","w")
    # fh.write("Small test file")
    # fh.write("Small test file")
    # fh.close()
    remote_file=remotepath.split('/')[-1]
    remote_dir=remotepath.split(remote_file)[0]

    try:
    # Create the connection
        conn = DropboxConnection(email, password)

        # Upload the file
        uploader=conn.upload_file(localpath,remote_dir,remote_file)
        public_url=conn.get_download_url(remote_dir,remote_file)
    except:
        print("Upload failed")
    else:
        print("Uploaded small_test_file.txt to the root of your Dropbox")
if __name__ == '__main__':
    import os
    email='ss3@elec-lab.tk';password='ss123456';

    localpath=os.getcwd().replace("\\","/")+'/small_test_file.txt';
    # remotepath='/'+localpath.split('/')[-1]
    try:remotepath0="/"+os.environ('OPENSHIFT_APP_DNS')+'/'
    except:
        remotepath0="/"+'presta4shop-dcmotor.rhcloud.com/'
        remotepath0="/"+'dr2omnia-diy4phantomjs.rhcloud.com/'
        remotepath0="/"+'vb2-fishsmarkets.rhcloud.com/'
		# fh = open("small_test_file.txt","w")
    # fh.write("Small test file")
    # fh.close()
    # my_dropbox( email, password, localpath, remotepath)
    app_key='pzwtcqpfj5ih8p0'
    app_secret='s57axvy6ta0cdpd'
    access_token='Ap8LK01GJbsAAAAAAAAABpqZnhsSpLwvdFgL69ROiQ98N3S-PPwbylCf2Cc5Fxhc'
    # link=main_dropbox(app_key,app_secret,access_token,localpath,remotepath).main_dropbox(localpath,remotepath)


    from dropbox.client import DropboxClient
    # import dropbox
    # import dropbox.client
    # client=dropbox.client.DropboxClient(access_token)
    client = DropboxClient(access_token)

    try:
	    CurrentDir=os.path.dirname(os.path.realpath(__file__))
	    Parent_Dir=os.path.abspath(os.path.join(CurrentDir, '..'))
        # Destination= os.path.abspath(os.path.join(Parent_Dir, '..'))

    except:
	    CurrentDir=os.getcwd()
	    Parent_Dir=os.path.abspath(os.path.join(CurrentDir, '..'))
        # Destination= os.path.abspath(os.path.join(Parent_Dir, '..'))
    CurrentDir='/tmp'
    Destination= os.path.abspath(os.path.join(Parent_Dir, '..'))

    # enumerate local files recursively
    for root, dirs, files in os.walk(CurrentDir):

         for dir2 in dirs:
           # if os.path.isdir(Destination+ curent_path+dir2):
            try:client.file_create_folder(remotepath0+dir2)
            except:pass
         for filename in files:

                # construct the full local path
                local_path = os.path.join(root, filename)
                if os.path.isfile(root+"/"+filename):
                    remotepath=remotepath0
                # construct the full Dropbox path
                    relative_path = os.path.relpath(local_path, CurrentDir)
                    dropbox_path = os.path.join(remotepath, relative_path).replace("\\",'/')

                    # upload the file
                    link=main_dropbox(app_key,app_secret,access_token,local_path,dropbox_path).main_dropbox(local_path,dropbox_path)
            # with open(local_path, 'rb') as f:
            #     client.put_file(dropbox_path, f)



    # for root, dirs, files in os.walk(CurrentDir):
    #     # root=root.replace("/","\\")
    #     curent_path0=root.split(Parent_Dir)[1]+'/'
    #     curent_path=curent_path0.replace('\\','/')
    #     # root=root.replace('\\','/')
    #     for dir2 in dirs:
    #        # if os.path.isdir(Destination+ curent_path+dir2):
    #             try:client.file_create_folder(remotepath0+dir2)
    #             except:pass
    #             for root2, dirs2, files2 in os.walk(dir2):
    #                 for file22 in files2:
    #
    #                     if os.path.isfile(root2+"/"+file22):
    #                         remotepath=remotepath0+dir2+'/'+file22
    #                         path = os.path.join(root2, file22)
    #                         link=main_dropbox(app_key,app_secret,access_token,path,remotepath).main_dropbox(path,remotepath)
    #
    #             # remotepath=remotepath0+dir2+remotepath.replace('/','')
    #     for file2 in files:
    #         # if os.path.isfile(Destination+ curent_path+file2):
    #         if os.path.isfile(root+"/"+file2):
    #             path = os.path.join(root, file2)
    #             try:
    #                 remotepath=remotepath0+dir2+'/'+file2
    #             except:
    #                 remotepath=remotepath0+file2
    #
    #             print "file is:"+file2
    #             link=main_dropbox(app_key,app_secret,access_token,path,remotepath).main_dropbox(path,remotepath)
    #             # except:pass
    #             # size_source = os.stat(path.replace('\\','/')).st_size # in bytes
    #             # size_target=os.stat(root+"\\"+file2).st_size
    #             # if size_source != size_target:
    #                 # replace(Parent_Dir+curent_path+file2,Destination+ curent_path+file2)
    #                 # pass
    #         else:
    #             pass
