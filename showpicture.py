import cv2 as cv
import json
src=cv.imread('../../../../data/coco/images/testdev2017/000000466319.jpg')
weight=src.shape[0]
hight=src.shape[1]

cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
path = r"results.json"
file = open(path, "rb")
fileJson = json.load(file)
t=0
for i in fileJson:

    if(i["image_id"]==466319):
        image_id=i["image_id"]
        category_id = i["category_id"]
        bbox = i["bbox"]
        score = i["score"]
        if(score>0.4):
            cv.rectangle(src, (int(bbox[0]), int(bbox[1])), (int(bbox[0]+bbox[2]), int(bbox[1]+bbox[3])), (0, 255,255),3)

    else:
        break
        #cv.rectangle(src, (91, 95), (270, 51), (0, 255,0),1)

#cv.rectangle(src, (91, 95), (270, 51), (0, 255,0),1)
cv.imshow('input_image', src)


k = cv.waitKey(20000)
if k == ord('s'): # wait for 's' key to save and exit
    cv.imwrite('1.png',img)
    cv.destroyAllWindows()
else:
    cv.destroyAllWindows()
