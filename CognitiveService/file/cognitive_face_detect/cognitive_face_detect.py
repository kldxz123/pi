import cognitive_face as CF
import json
import os


apiKey = '232d6ece9aad407c89067c63be83c3cf'  # Replace with a valid Subscription Key here.
CF.Key.set(apiKey)

#os.system("v4l2grab -o temp.jpg -W 640 -H 480")
#img_url = 'temp.jpg'
img_url = 'detection1.jpg'

result = CF.face.detect(img_url,attributes = 'age')
print(json.dumps(result,indent = 4))
