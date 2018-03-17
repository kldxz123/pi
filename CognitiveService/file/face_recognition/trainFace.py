import cognitive_face as CF
import os
import json

def GetFileListFromDir(dir):
    l = []
    for p, d, f in os.walk(dir):
        for fname in f:
            l.append(os.path.join(p,fname))
    return l

def CheckGroupIdExistStatus(groupId):
    for info in CF.person_group.lists():
        if info['personGroupId'] == groupId:
            return True
    return False

# set Key
KEY = "232d6ece9aad407c89067c63be83c3cf"
CF.Key.set(KEY)

# create group and person

personGroupId = "myfriends"
if not CheckGroupIdExistStatus(personGroupId):
    CF.person_group.create(personGroupId, "My Friends")
user1 = CF.person.create(personGroupId, "Dad")
#print(user1)

# add face
friendImageDir = "img/person"
for fname in GetFileListFromDir(friendImageDir):
    CF.person.add_face(fname, personGroupId, user1['personId'])

# train
CF.person_group.train(personGroupId)


trainingStatus = "running"
while(True):
    trainingStatus = CF.person_group.get_status(personGroupId)
    if trainingStatus['status'] != "running":
        print(trainingStatus)
        break

# # recognitize face
# testImageFile = "img/identification1.jpg"
# faces = CF.face.detect(testImageFile)
# faceIds = []
# for face in faces:
#      faceIds.append(face['faceId'])

# res = CF.face.identify(faceIds, personGroupId)
# re = json.dumps(res,indent = 2)
# print(re)
