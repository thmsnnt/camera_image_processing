import cv2
import mediapipe as mp
import glob
import os

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# For static images:
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5)

folders_path = 'datas/TownCentreXVID'
images_path = glob.glob(os.path.join(folders_path,'*.jpg'))


for img in images_path:
    image = cv2.imread(img)
    image_hight, image_width, _ = image.shape

    # Convert the BGR image to RGB before processing.
    #results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Draw pose landmarks on the image.
    #mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    cv2.imshow('Frame',image)
    cv2.waitKey(20)
pose.close()