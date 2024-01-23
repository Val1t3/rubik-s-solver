#!/usr/bin/env python3

import cv2

class Webcam:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)


    def run(self) -> None:
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('a'):
                self.check_color()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # RELEASE CAPTURE
        self.cap.release()
        cv2.destroyAllWindows()


    def check_color(self) -> None:
        print("color")