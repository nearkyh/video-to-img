import cv2
import numpy as np
import os


video_path = "video/test.MOV"

def video_to_image(video_path):
    cap = cv2.VideoCapture(video_path)
    count = 0
    while (cap.isOpened()):
        ret, image_np = cap.read()
        if not ret:
            break

        # 60프레임당 이미지 1장
        frame = 60
        if (int(cap.get(1)) % frame == 0):
            video_name = video_path.split('/')[-1][:-4]
            image_name = "{}_{}.png".format(video_name, "{0:04d}".format(count))
            image_path = "images/"
            if not os.path.isdir(image_path):
                os.mkdir(image_path)
                print("Create directory({})".format(image_path))
            print("Save,", image_path + image_name)
            cv2.imwrite(image_path + image_name, image_np)
            count += 1

    cap.release()
    print("Success, video to image")

video_to_image(video_path=video_path)
