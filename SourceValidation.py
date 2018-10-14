import MySQLdb


def SourceValidation(url):

    url.replace("https://","")
    url.replace("http://","")

    url.index()

    db = MySQLdb.connect("35.239.255.99","root","password","source_validation")

    cursor = db.cursor()

    sql = "select score from urls where url = /'" + httpUrl + "/' or url = /'" + httpsUrl + "/'"