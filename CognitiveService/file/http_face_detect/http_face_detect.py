import httplib, urllib, base64
import os

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '232d6ece9aad407c89067c63be83c3cf'#replace your API key here
}

params = urllib.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age',
})
os.system("v4l2grab -o temp.jpg -W 640 -H 480")

img = open('temp.jpg','rb')#Read Picture

#img = open('detection1.jpg','rb')
picData = img.read()

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/detect?%s" % params, picData, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
