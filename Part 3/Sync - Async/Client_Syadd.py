import rpyc
remoteconnection = rpyc.connect("localhost", 14789)
#m = 1
#while True:
p =remoteconnection.root.add(3, 2)
print(p)
    #
