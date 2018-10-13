import requests

def DateResearchValue( date, keywords ):
    #date needs to be in format -> 20140815:20140931
    #keywords can be a string with words seperated by spaces, I guess
    dateValue = 0
    url = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyAT3PKpgtjWdjHBemeHT5ZkDbwnZBARBEE&cx=011809875003834266328:_eunbtqpsiq&q='
    search = url + keywords
    dateBefore = date - 100
    dateAfter = date + 100 
    search = url + keywords + '&sort=date:r:' + str(dateBefore) + ':' + str(dateAfter) 

    req = requests.get(url = search, params = None)
    data = req.json()

    for i in range(0,len(data['items'])):
        print(data['items'][i]['title'])
        #if ( data['items'][i]['title'] has keywords ):
        if( 1==1 ):
            dateValue += 1

    return dateValue

print(DateResearchValue( 20140624, "Fortunate Son"))