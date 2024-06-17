from xmlrpc.server import SimpleXMLRPCServer
import os
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client


# Restrict t-o a particular path.
class Handle_request(SimpleXMLRPCRequestHandler):
    rpc_path = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=Handle_request) as server:
    server.register_introspection_functions()

    # Define a directory for file storage
    file_dir = 'server_upload'
    file_dir2 = 'server_download'

    # Create file directory if it does not exist
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    if not os.path.exists(file_dir2):
        os.makedirs(file_dir2)

    # Define upload file method
    def upload_file(file_name, file_data):
        with open(os.path.join(file_dir, file_name), 'wb') as f:
            f.write(file_data.data)
        return True
    # Define download file method
    def download_file(file_name):
        with open(os.path.join(file_dir, file_name), 'rb') as f:
            return xmlrpc.client.Binary(f.read())
        # Define rename file method
    def rename_file(old_file_name, new_file_name):
        os.rename(os.path.join(file_dir, old_file_name), os.path.join(file_dir, new_file_name))
        return True
        
    def delete_file(file_name):
        os.remove(os.path.join(file_dir, file_name))
        return True

    # Register upload and download methods
    server.register_function(upload_file, 'upload_file')
    server.register_function(download_file, 'download_file')
    server.register_function(rename_file, 'rename_file')
    server.register_function(delete_file, 'delete_file')

    # Run the server's main loop
    server.serve_forever()






