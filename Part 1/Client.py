import xmlrpc.client
choice= int(input("Enter your choice 1.Upload 2.Download 3.Rename 4.Delete 0.Exit"))
with xmlrpc.client.ServerProxy("http://localhost:8000/RPC2") as proxy:
    while choice:
        if (choice==1):
            with open("Nav.txt", "rb") as f:
                file_data = xmlrpc.client.Binary(f.read())
                proxy.upload_file("Nav.txt", file_data)
                choice= int(input("Enter your choice 1.Upload 2.Download 3.Rename 4.Delete 0.Exit"))

        if (choice==2):
            path= "server_download/Nav.txt"
            with open(path, "wb") as f:
                file_data = proxy.download_file("Nav.txt")
                f.write(file_data.data)
            choice= int(input("Enter your choice 1.Upload 2.Download 3.Rename 4.Delete 0.Exit"))

        if (choice==3):
            proxy.rename_file("Nav.txt", "newfile.txt")
            choice= int(input("Enter your choice 1.Upload 2.Download 3.Rename 4.Delete 0.Exit"))
        if (choice==4):
            proxy.delete_file("newfile.txt")
            choice= int(input("Enter your choice 1.Upload 2.Download 3.Rename 4.Delete 0.Exit"))
        if (choice==0):
            print("Exit")
            break
        else:
            print("Enter valid input")
            choice= int(input("Enter your choice 1.Upload 2.Download 3.Rename 4.Delete 0.Exit"))
            continue

