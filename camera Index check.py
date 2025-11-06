import cv2

def print_and_launch_cameras():
    for index in range(10):
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            print(f"Camera Index: {index}")
            launch_camera(cap)
        else:
            print(f"Camera with index {index} is not available.")

def launch_camera(cap):
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        cv2.imshow('Camera Feed', frame)
        
        # Wait for a key press with a timeout of 1 millisecond
        key = cv2.waitKey(1)
        
        # Press any key or press Enter to exit
        if key != -1 or key == 13:  # Check for any key or Enter (key code 13)
            break
    
    cap.release()
    cv2.destroyAllWindows()

def main():
    print_and_launch_cameras()

if __name__ == "__main__":
    main()