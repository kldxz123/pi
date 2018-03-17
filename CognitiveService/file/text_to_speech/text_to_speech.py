import urllib,httplib,json
from xml.etree import ElementTree
import wave

apiKey = "34c7815245934e4a8e088956af4e62d7"

headers = {"Ocp-Apim-Subscription-Key": apiKey}
AccessTokenHost = "api.cognitive.microsoft.com"
path = "/sts/v1.0/issueToken"

conn = httplib.HTTPSConnection(AccessTokenHost)
conn.request("POST", path, '', headers)
response = conn.getresponse()


data = response.read()
conn.close()

accesstoken = data.decode("UTF-8")
#print ("Access Token: " + accesstoken)

body = ElementTree.Element('speak', version='1.0')
body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
voice = ElementTree.SubElement(body, 'voice')
voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
voice.set('{http://www.w3.org/XML/1998/namespace}gender', 'Male')
voice.set('name', 'Microsoft Server Speech Text to Speech Voice (en-US, BenjaminRUS)')
voice.text = "I am going to give him an offer he cannot refuse."
print(body)

headers = {"Content-type": "application/ssml+xml", 
			"X-Microsoft-OutputFormat": "riff-16khz-16bit-mono-pcm", 
			"Authorization": "Bearer " + accesstoken, 
			"X-Search-AppId": "07D3234E49CE426DAA29772419F436CA", 
			"X-Search-ClientID": "1ECFAE91408841A480F00935DC390960", 
			"User-Agent": "TTSForPython"}
	


#Connect to server to synthesize the wave
print ("\nConnect to server to synthesize the wave")
conn = httplib.HTTPSConnection("speech.platform.bing.com")
conn.request("POST", "/synthesize", ElementTree.tostring(body), headers)
response = conn.getresponse()
print(response.status, response.reason)

data = response.read()
conn.close()
print("The synthesized wave length: %d" %(len(data)))

#Write data in wav file
f = wave.open(r"result.wav","wb")
f.setnchannels(1)
f.setsampwidth(2)
f.setframerate(16000)
f.writeframes(data)
f.close()