import requests

#https://www.googleapis.com/customsearch/v1?key=AIzaSyAT3PKpgtjWdjHBemeHT5ZkDbwnZBARBEE&cx=011809875003834266328:_eunbtqpsiq&q= 

#input: author's name
#append to URL
#Make GET request for search
#Look at all those pages and see if they are articles
#For every article, bump Classifier

def AuthorNoteriety( authorName ):
    noteriety = 0
    url = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyAT3PKpgtjWdjHBemeHT5ZkDbwnZBARBEE&cx=011809875003834266328:_eunbtqpsiq&q='
    search = url + authorName

    req = requests.get(url = search, params = None)
    data = req.json()

    for i in range(0,len(data['items'])):
        print(data['items'][i]['link'])
        #if ( authorName == findAuthors(data.items[i].link) ):
        if( 1==1 ):
            noteriety += 1
        
    return noteriety

print(AuthorNoteriety('Joe Guilliums'))