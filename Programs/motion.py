import numpy as np
import cv2
import copy

# Camera
cam = cv2.VideoCapture(0)

prev = None
while True:
    ret, frame = cam.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Error check
    if not ret:
        print('Problem with getting frame')
        break
    
    if prev is not None:
        frame = frame.astype(np.int32)

        # Compute distance and only keep values bigger than threshold
        diff = np.absolute(np.subtract(frame, prev))
        threshold = 10
        diff[diff < threshold] = 0
        diff = diff.astype(np.uint8)

        # Back to 3 channels
        diff = cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR)

        # Keep only the red channel (BGR)
        diff[:,:,:2] = 0

        # Show the image
        cv2.imshow('Motion in the Ocean!', diff)

    # Assign prev frame to current frame
    prev = frame

    # Press 'q' to quit the program
    if cv2.waitKey(20) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()


