import av
import numpy as np
import cv2

def read_frames(path, max_frames=None):
    container = av.open(path)
    stream = container.streams.video[0]
    stream.thread_type = 'AUTO'
    for i, frame in enumerate(container.decode(stream)):
        img = frame.to_ndarray(format='bgr24')
        yield i, img
        if max_frames and i+1 >= max_frames:
            break

for idx, frame in read_frames('test1.mp4'):
    cv2.imshow('frame', frame)
    if cv2.waitKey(1):
        pass