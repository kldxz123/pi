import CreateProfile
import EnrollProfile
import VerifyFile
import GetProfile
import os



def GetFileListFromDir(dir):
    l = []
    for p, d, f in os.walk(dir):
        for fname in f:
            l.append(os.path.join(p,fname))
    return l


key = "a5ac34fbe6fd4fbab539919808687653"#Replace your own subscription key here.
locale = "en-us"#Change language
profile_id = CreateProfile.create_profile(key,locale)#Create profile


s = 'Audio'
list = GetFileListFromDir(s)
for l in list:
	dirs = l

	EnrollProfile.enroll_profile(key,profile_id,dirs)

'''
for i in range(3):
	print "Read this sentence: This is a demo for Microsoft speaker recognition."
	os.system("arecord -f S16_LE -r 16000 -c 1 temp.wav")
	EnrollProfile.enroll_profile(key,profile_id,"temp.wav")
'''
	
#Test
test_audio = "Test1.wav"

VerifyFile.verify_file(key,test_audio,profile_id)

test_audio = "Test2.wav"

VerifyFile.verify_file(key,test_audio,profile_id)

