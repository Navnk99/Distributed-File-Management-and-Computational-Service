import rpyc
remoteconnection = rpyc.connect("localhost", 14789)
m = 1
outcome = []
while True:
    async_method = rpyc.async_(remoteconnection.root.asyncadd)
    result =async_method(3, 6)
    outcome.append(result)
    m = m + 1
    if m == 5:
        break
for p in outcome:
    if p.ready == True:
        fetchresults = remoteconnection.root.fetch_res(p.value, "addition_Computations.db", "additionresults")
        print(fetchresults)
    else:
        result.wait()
        continue