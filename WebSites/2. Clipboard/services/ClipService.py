from Clipboard.model.Clip import Clip
import os
class ClipService:
    def get(self, clipId):
        if os.path.isfile("clips\\"+clipId+".clip"):
            f=open('clips\\'+clipId+'.clipdata', 'r')
            data=f.read()
            clipInfo=data.split(',')
            f.close()
        
            f=open("clips\\"+clipId+".clip")
            clipData=f.read()
            f.close()
            return Clip(clipId, clipInfo[0], clipInfo[1], clipData)
    def set(self,clip, userId):
        if os.path.isfile("clips\\"+clip.id+".clip"):
            f = open("clips\\"+clip.id+".clipdata", "r")
            data=f.read()
            clipInfo=data.split(',')
            clipOwner=clipInfo[0]
            f.close()
            if clipOwner != userId and clip.visibility=='public':
                f = open("clips\\"+clip.id+".clip", "w")
                f.write(clip.data)
                f.close()
                return 'successful_save'
            elif clipOwner != userId and clip.visibility=='private':
                return 'access_denied'
            else: 
                f = open("clips\\"+clip.id+".clipdata", "w")
                clipInfo=clipOwner+','+clip.visibility
                f.write(clipInfo)
                f.close()
                return 'successful_save'
        else:
            f = open("clips\\"+clip.id+".clip", "w")
            clipOwner=userId
            f.write(clip.data)
            f.close()
            f = open("clips\\"+clip.id+".clipdata", "w")
            clipInfo=clipOwner+','+clip.visibility
            f.write(clipInfo)
            f.close()
            return 'successful_save'