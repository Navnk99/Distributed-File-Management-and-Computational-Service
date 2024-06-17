import xmlrpc.client
import os
import threading
import time

def helper_thread(num):
    print("sync")
    with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
        while(True):
            proxy.file_sync()
            time.sleep(10)
            print("syncing")
def thread_2(num):
    with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
        proxy.rename_file()
        proxy.get_details()
        path = 'C:\DS 5306\client'
        dir_list = os.listdir(path)
        print("Files in client",dir_list)
        
  

if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=helper_thread, args=(1,))
    t2 = threading.Thread(target=thread_2, args=(1,))
  
    # starting thread 1
    t1.start()
    # starting thread 2
    #=t2.start()
    # both threads completely executed
    print("Done!")