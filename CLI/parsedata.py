import re   


def parsexdata():
    with open('exploitdata.txt','r') as file:
        countriesStr = file.read()
    #print(countriesStr)


    t = countriesStr.replace("-", "")

    res = re.sub(' +', ' ', t)

  
    newres = re.sub(r'[^\x00-\x7f]', '', res)
    return newres
