#breaking video into individual frames. COmpression not done yet. will be done in diff_image_2.py

import cv2
cap = cv2.VideoCapture("Wild.mp4")
cap.open("Wild.mp4")
print cap.isOpened()
i=0
while(cap.isOpened()):
    global i
    ret, frame = cap.read()
    frame = cv2.resize(frame, (frame.shape[1]/3, frame.shape[0]/3))
    cv2.imwrite(str(i)+".jpg", frame)     # save frame as JPEG file
    i=i+1
    #cv2.imshow("20sec",frame)	
#vidcap.set(cv2.CV_CAP_PROP_FRAME_COUNT,20000)      # just cue to 20 sec. position
#success,image = vidcap.read()
#if success:
 #   cv2.imwrite("frame20sec.jpg", image)     # save frame as JPEG file
  #  cv2.imshow("20sec",image)
   # cv2.waitKey()     
