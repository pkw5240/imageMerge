import glob
import os
from PIL import Image

# 배경 -> 다리 -> 몸통 -> 입 -> 눈 -> 악세

targetDir = 'C:\\Users\\test\\Documents\\카카오톡 받은 파일\\nft조합\\nft조합\\'


print(targetDir)
f = glob.glob(targetDir + "눈_*.png")
print(len(f))

body = "body.png"

datas = ["배경_","다리_","입_","눈_","악세서리_"]

groups = []

for i in range(len(datas)):
    f = glob.glob(targetDir + datas[i]+"*.png")
    temp = datas[i]
    tempGroup = []
    for j in range(1,len(f)+1):
        tempGroup.append(temp+str(j)+".png")
    groups.append(tempGroup)

bodyImg = Image.open(targetDir+body)
(height,width) = bodyImg.size

''' test

result = Image.new("RGBA",(width,height))

test = Image.open(groups[0][0])
test2 = Image.open(groups[1][0])
test3 = Image.open(groups[2][0]) 

result.paste(test, (0,0), test)
result.paste(test2, (0,0), test2) 
result.paste(test3, (0,0), test3)
result.show()
'''
folderPart = 0

def mixImage(nowStep, resultImage, groups):
    global count
    global partCnt
    global folderPart
    
    if nowStep == partCnt :
        count+=1
        fileName = "{}{}{}".format('res_',count,".png")

        if not os.path.exists(targetDir+str(folderPart)):
            os.makedirs(targetDir+str(folderPart))
            
        resultImage.save(targetDir+str(folderPart)+"\\"+fileName)
        return

    originImg = resultImage.copy()
    
    for imgName in groups[nowStep]:
        backImg = originImg.copy()
        nowImg = Image.open(imgName)
        backImg.paste(nowImg,(0,0),nowImg)

        if nowStep == 1: 
            backImg.paste(bodyImg,(0,0),bodyImg)
        mixImage(nowStep+1, backImg, groups)
        


partCnt = len(groups)
count = 0

for background in groups[0]:
    folderPart = folderPart+1
    newImg = Image.new("RGBA", (width,height))
    bgImg = Image.open(background) 
    newImg.paste(bgImg,(0,0),bgImg)
    mixImage(1,newImg,groups)
