#initialize RPC
from xmlrpc.server import SimpleXMLRPCServer
server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")

import ftplib
from genericpath import exists
import os
import threading
import time

FTP_Host_ID = 'localhost'
FTP_Port_ID = 21
FTP_User_ID = 'Nav'
FTP_Password = 'NAV213'
Local_File_Path = 'C:\Users\navnk\OneDrive\Desktop\DS_PROJECT1_1002039449\Part 2'
serverFilePath= 'C:\Users\navnk\OneDrive\Desktop\DS_PROJECT1_1002039449\Part 2'
remoteFolder = "/"


def getFtpFilenames(FTP_Host_ID, FTP_Port_ID, FTP_User_ID, FTP_Password, Remote_Directory):
    ftp = ftplib.FTP(timeout=30)
    ftp.connect(FTP_Host_ID, FTP_Port_ID)
    ftp.login(FTP_User_ID, FTP_Password)
    if not (Remote_Directory == None or Remote_Directory.strip() == ""):
        _ = ftp.cwd(Remote_Directory)
    fnames = []
    try:
        fnames = ftp.nlst()
    except ftplib.error_perm as resp:
        if str(resp) == "No files found":
            fnames = []
        else:
            raise
    ftp.quit()
    return fnames

def uploadFileToFtp(Local_File_Path,i, FTP_Host_ID, FTP_Port_ID, FTP_User_ID, FTP_Password, Remote_Directory):
    Local_File_Path=Local_File_Path+i
    isUploadSuccess: bool = False
    _, targetFilename = os.path.split(Local_File_Path)
    ftp = ftplib.FTP(timeout=30)
    ftp.connect(FTP_Host_ID, FTP_Port_ID)
    ftp.login(FTP_User_ID, FTP_Password)
    if not (Remote_Directory == None or Remote_Directory.strip() == ""):
        _ = ftp.cwd(Remote_Directory)
    with open(Local_File_Path, "rb") as file:
        retCode = ftp.storbinary(f"STOR {targetFilename}", file, blocksize=1024*1024)
    ftp.quit()
    if retCode.startswith('226'):
        isUploadSuccess = True
    return isUploadSuccess

def rename(old_file_name,new_file_name):
    ftp=ftplib.FTP(timeout=30)
    ftp.connect(FTP_Host_ID, FTP_Port_ID)
    ftp.login(FTP_User_ID, FTP_Password)
    ftp.cwd("/")
    ftp.rename(old_file_name,new_file_name)
    #ftp.mkd("test")
    ftp.quit()

def delete(name):
    ftp=ftplib.FTP(timeout=30)
    ftp.connect(FTP_Host_ID, FTP_Port_ID)
    ftp.login(FTP_User_ID, FTP_Password)
    ftp.cwd("/")
    ftp.delete(name)
    ftp.quit()



def file_sync():        
    # upload file

    ##############file name####################
    fnames = getFtpFilenames(FTP_Host_ID, FTP_Port_ID, FTP_User_ID, FTP_Password, remoteFolder)
    print("files in server", fnames)
    path = 'C:\DS 5306\server'
    dir_list = os.listdir(path)
    print("Files in local server",dir_list)
    path = 'C:\DS 5306\client'
    dir_list = os.listdir(path)
    print("Files in client",dir_list)
    ############################################

    ##############upload########################
    #upload files which are not in server
    if(fnames!=dir_list):
        for i in dir_list:
            #print(i)
            isUploadSuccess = uploadFileToFtp(Local_File_Path,i, FTP_Host_ID, FTP_Port_ID, FTP_User_ID, FTP_Password, remoteFolder)
            print("upload status = {0}".format(isUploadSuccess)) 
   
    #delete file which are not in client
    if(fnames!=dir_list):
        for i in fnames:
            if(i not in dir_list):
                delete(i)

    #if(fnames!=dir_list):
    #   for i in fnames and i not in dir_list:
    #       delete(i)
    ##############################################

def get_details():
    print("after sync")
    fnames = getFtpFilenames(FTP_Host_ID, FTP_Port_ID, FTP_User_ID, FTP_Password, remoteFolder)
    print("files in server", fnames)
    path = 'C:\DS 5306\client'
    dir_list = os.listdir(path)
    print("Files in client",dir_list)
    path = 'C:\DS 5306\server'
    dir_list = os.listdir(path)
    print("file in local server",dir_list)


def rename_file():
    ###############rename#######################
    fnames = getFtpFilenames(FTP_Host_ID, FTP_Port_ID, FTP_User_ID, FTP_Password, remoteFolder)
    print("files in server", fnames)
    old_file_name=input("file name to change")
    new_file_name=input("enter new file name")
    rename(old_file_name,new_file_name) 



server.register_function(get_details, "get_details")
server.register_function(rename_file, "rename_file")
server.register_function(file_sync, "file_sync")
server.serve_forever()