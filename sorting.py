from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def getNames(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page=urlopen(req)
    namesList=[]
    soup = BeautifulSoup(page.read(), features='lxml')
    sources=soup.findAll(attrs={'itemprop':'name'})
    for source in sources:
        namesList.append(str(source.get_text()))
    names = sort(namesList)
    return names

def sort(names):
    len_liststring=len(names) 
 
    for i in range(len_liststring-1): 
        for j in range(len_liststring-i-1): 
            if names[j]>names[j+1]: 
                names[j],names[j+1]=names[j+1],names[j] 

    new_string=list("")
    for m in names: 
        new_string.append(m)
    #hello = [new_string.strip(' ') for x in hello]
    sortedNames = map(lambda each:each.split("[email\xa0protected]"), new_string)
    
    return list(sortedNames)

url="https://mlh.io/seasons/2021/events"
sortedNames=getNames(url)
for name in list(sortedNames):
    print(' '.join(name))