import rpyc
remoteconnection= rpyc.connect("localhost",14789)
sortedresults= remoteconnection.root.sort([3, 8, 2])
print(sortedresults)