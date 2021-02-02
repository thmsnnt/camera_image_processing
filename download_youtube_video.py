from pytube import YouTube
import os
import shutil
import math
import datetime
import matplotlib.pyplot as plt
import cv2

video = YouTube('https://www.youtube.com/watch?v=mg6-SnUl0A0')
video.streams.get_by_itag(18).download()
