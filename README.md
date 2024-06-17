# Distributed File Management and Computational Service

This repository contains the implementation of a distributed systems project focused on utilizing Remote Procedure Calls (RPC) to construct a file upload, download, and computational service.

## Structure
The project is divided into three main parts:
1. **Multi-threaded File Server**
2. **Automated File Transfer using Multithreading**
3. **Computational Server using RPCs**

### Part 1: Multi-threaded File Server
Implemented a multi-threaded file server that supports the following operations:
- **UPLOAD**: Uploads files to the server.
- **DOWNLOAD**: Downloads files from the server.
- **DELETE**: Deletes files on the server.
- **RENAME**: Renames files on the server.

Both client and server implementations are done in Python and operate on the Linux OS.

### Part 2: Automated File Transfer using Multithreading
Monitors a directory for changes and automatically updates the server with:
- **File additions**
- **File modifications**
- **File deletions**

A helper thread periodically tracks changes in the server's directory.

### Part 3: Computational Server using RPCs
Implemented two operations using RPCs:
- **add(i, j)**: Adds two integers.
- **sort(array)**: Sorts an array.

Implemented in three different modes:
- **Synchronous RPCs**: Executes functions in a line-by-line manner, with results displayed sequentially.
- **Asynchronous RPCs**: Executes functions without waiting for the previous operation to complete, resulting in delayed output.
- **Deferred Synchronous RPCs**: Combines synchronous and asynchronous methods to optimize performance.

## How to Run
1. Clone the repository.
2. Navigate to the respective directories for each part.
3. Follow the instructions in the README files within each directory to run the client and server applications.

## Acknowledgements
This project was independently completed to demonstrate the capabilities of distributed systems using RPCs.
