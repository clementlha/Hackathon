import cv2

cap= cv2.VideoCapture('video.mp4')
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#5 images
image = "["
sep_frame = int(frame_count / 5)
i=1
while(cap.isOpened()):
    
    ret, frame = cap.read()
    if ret == False:
        break
    if i%sep_frame==0:
        cv2.imwrite('5images/img'+str(i)+'.jpg',frame)
        image += "{'name':'img"+str(i)+".jpg','start':"+str(i)+",'end':"+str(i+sep_frame)+"},"
    i+=1

image += "]"
print(image)
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
