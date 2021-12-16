import cv2
import json

file = 'video.mp4'

#5 images
cap= cv2.VideoCapture(file)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
nom_video = '"nom_video":"' + file + '",'
nb_frame='"nb_frame":"' + str(frame_count) + '",'

images = '"images":['
sep_frame = int(frame_count / 5)
i=1
while(cap.isOpened()):
    
    ret, frame = cap.read()
    if ret == False:
        break
    if i%sep_frame==0:
        cv2.imwrite('5images/img'+str(i)+'.jpg',frame)
        images += '{"nom_img":"img'+str(i)+'.jpg","debut":'+str(i)+',"fin":'+str(i+sep_frame)+'},'
    i+=1

images = images[:-1] + "]"
json_str = "{" + nom_video + nb_frame + images + "}"
print(json_str)
json_obj = json.loads(json_str)

#10 images
cap= cv2.VideoCapture('video.mp4')
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
sep_frame = int(frame_count / 10)
i=1
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    if i%sep_frame==0:
        cv2.imwrite('10images/img'+str(i)+'.jpg',frame)
    i+=1

#20 images
cap= cv2.VideoCapture('video.mp4')
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
sep_frame = int(frame_count / 20)
i=1
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    if i%sep_frame==0:
        cv2.imwrite('20images/img'+str(i)+'.jpg',frame)
    i+=1
 
cap.release()
cv2.destroyAllWindows()
