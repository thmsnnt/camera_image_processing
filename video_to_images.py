import cv2
import os

video_name = 'TownCentreXVID.mp4'
path_video = 'datas/{}'.format(video_name)
cap = cv2.VideoCapture(path_video)
path_out = 'datas/{}'.format(video_name.split('.')[0])

if not os.path.exists(path_out):
    os.mkdir(path_out)

nb=0
while True:
    ret, image = cap.read()
    nb+=1
    if nb < 10:
        nbS = '000{}'.format(nb)
    elif nb < 100:
        nbS = '00{}'.format(nb)
    elif nb < 1000:
        nbS = '0{}'.format(nb)
    else:
        nbS = '{}'.format(nb)
    cv2.imwrite(os.path.join(path_out,'frame_{}.jpg'.format(nbS)),image)