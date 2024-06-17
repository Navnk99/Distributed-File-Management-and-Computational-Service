import rpyc
remoteconnection = rpyc.connect("localhost",14789)
outcome = []
asyncsortmethod = rpyc.async_(remoteconnection.root.asyncsort)
m = [2, 8, 3]
w = tuple(m)
asyncsortresult =asyncsortmethod(w)
outcome.append(asyncsortresult)
asyncsortresult.wait()
for p in outcome:
    if p.ready == True:
        fetchresults =remoteconnection.root.fetch_res(p.value, "sorted_Computations.db", "sortedresults")
        print(fetchresults)
    else:
        asyncsortresult.wait()
        continue

