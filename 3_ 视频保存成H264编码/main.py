import cv2

cap = cv2.VideoCapture('test.mp4')

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = int(cv2.VideoWriter_fourcc(*'H264'))

out = cv2.VideoWriter('output.mp4', fourcc, fps, (width,  height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
