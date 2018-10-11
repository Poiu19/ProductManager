import urllib.request
import json

class ApiControler():
    def __init__(self, body):
        url = "http://localhost/pythonAPI/api.php"
        req = urllib.request.Request(url)
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        jsondata = json.dumps(body)
        jsondataasbytes = jsondata.encode('utf-8')
        req.add_header('Content-Length', len(jsondataasbytes))
        response = urllib.request.urlopen(req, jsondataasbytes)
        data = response.read()
        encoding = response.info().get_content_charset('utf-8')
        self.response = json.loads(data.decode(encoding))

    def getResponse(self):
        return self.response