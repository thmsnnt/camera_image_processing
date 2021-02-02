import cv2
import numpy as np
import copy

video = "data/VIRAT_S_050000_08_001235_001295.mp4"
capture = cv2.VideoCapture(video)

def resize(frame, factor):
    #frame = frame[...,0]
    x = int(frame.shape[0]*factor)
    y = int(frame.shape[1]*factor)
    return cv2.resize(frame, (y,x))

def threshold(mask):
    mask_copy = copy.deepcopy(mask)
    mask_binary = mask < 125
    mask_copy[mask_binary] = 0
    return mask_copy, mask_binary

def flou(im):
    im = cv2.GaussianBlur(im, (3, 3), 0)
    return im

def delete_blobs(im):
    nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(im, connectivity=8)
    sizes = stats[1:, -1]; nb_components = nb_components - 1
    min_size = 50
    img2 = np.zeros((output.shape))
    for i in range(0, nb_components):
        if sizes[i] >= min_size:
            img2[output == i + 1] = 255
    return img2

def reshape(im):
    im = im[..., np.newaxis]
    im = np.repeat(im, 3, axis=-1)
    return im

backSub = cv2.createBackgroundSubtractorMOG2()

while(True):
    _, frame = capture.read()
    if frame is None:
        break
    frame = resize(frame,0.35)
    mask = backSub.apply(frame)
    mask_blobs = delete_blobs(mask)
    num_frame = int(capture.get(cv2.CAP_PROP_POS_FRAMES))
    mask = reshape(mask)
    mask_blobs = reshape(mask_blobs)

    mask_flou = flou(mask_blobs)
    mask_threshold, mask_binary = threshold(mask_flou)
    #cv2.putText(mask, str(num_frame), (10, 18), cv2.FONT_HERSHEY_SIMPLEX, 0.5 , (255,255,255))
    concat = np.hstack((mask,mask_blobs))
    concat_2 = np.hstack((mask_flou,mask_threshold))
    concat = np.vstack((concat,concat_2))
    cv2.imshow('Masque',concat)
    cv2.waitKey(1)