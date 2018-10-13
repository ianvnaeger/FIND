def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/0.12/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Hello World!'


def Parser(request): 
    #given a link to an article, the function can find information about the article
        #information to be found: author, source of article, title, etc.
    return

def Classifier():
    #take the parsed info, make classifiers based on the validity of the info
    return

def Decider():
    #given ratings from the classifier, use Machine Learning Magic to determine if fake news
    return

def FIND():
    #call Parser
    #call Classifier
    #call Decider