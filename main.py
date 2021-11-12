import cv2
import numpy as np


def get_bbox_list(bbox_path):
    bbox_list = []

    with open(bbox_path) as file:
        for i in range(4):
            line = file.readline()
            line = line.strip().split(', ')
            temp_list = line[2:6]
            temp_list = [int(x, 16) for x in temp_list]
            bbox_list.append(temp_list)

    return bbox_list


def draw_rect(img_path, bbox_path):
    img = cv2.imread(img_path)

    bbox_list = get_bbox_list(bbox_path)

    for bbox in bbox_list:
        x, y, w, h = bbox[0], bbox[1], bbox[2], bbox[3]
        roi = img[y:y+h, x:x+w]
        cv2.rectangle(roi, (0, 0), (w-1, h-1), (0, 255, 0))

    img = cv2.resize(img, dsize=(320, 640), interpolation=cv2.INTER_LINEAR)
    cv2.imshow("Bounding Box", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    image_file_path = '/home/hong/Documents/Draw-Bbox/testImage.png'
    bbox_file_path = '/home/hong/Documents/Draw-Bbox/20_after_NMS.txt'

    draw_rect(image_file_path, bbox_file_path)


