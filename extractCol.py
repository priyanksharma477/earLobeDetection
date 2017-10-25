f=open("/home/priyank/P.E python/defaultTrain2.txt", "r")
out=open("/home/priyank/P.E python/output.txt", "w")
lines=f.readlines()

for x in lines:
    out.write(x.split(' ')[16]+"    "+x.split(' ')[17]+"    "+x.split(' ')[18]+"    "+x.split(' ')[19]+x.split(' ')[29]+"    "+x.split(' ')[30]+"    "+x.split(' ')[31]+"    "+x.split(' ')[32]+"    "+x.split(' ')[84]+"    "+x.split(' ')[85]+"    "+x.split(' ')[86]+"    "+x.split(' ')[87]+x.split(' ')[97]+"    "+x.split(' ')[98]+"    "+x.split(' ')[99]+"    "+x.split(' ')[100]+"\n")
f.close()
out.close()
