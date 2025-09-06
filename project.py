import cv2
import os

def main():
    cap = cv2.VideoCapture("cat.mp4")
    if not cap.isOpened():
        print("Error: Could not open video file.")
    else:
        print("Video file opened successfully!")
    for i in range(10):
        ret, frame = cap.read()
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if ret:
            cv2.imwrite(os.path.join("./results", f"frame{i+1}.jpg"), frame_gray)
        else:
            print("Error: Could not read the frame.")
    
    cap.release()


if __name__ == "__main__":
    main()