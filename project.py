import cv2,os,sys

def main():
    ask = input("webcam or video name: ")
    if ask == "webcam":
        cap = cv2.VideoCapture(1)
    else:
        cap = cv2.VideoCapture(ask)
        if not cap.isOpened():
            print("Error: Could not open video file.")
            sys.exit()
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