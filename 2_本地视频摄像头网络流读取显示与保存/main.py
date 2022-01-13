import cv2

# VideoCapture参数可以是本地视频文件、本地摄像头的id、网络摄像头的url，如
# cv2.VideoCapture(0)
# cv2.VideoCapture('rtsp://192.168.0.100:554/')
cap = cv2.VideoCapture('test.mp4')

fourcc = cv2.VideoWriter_fourcc(*'XVID')
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)
print('{}, {}, {}'.format(width, height, fps))

out = cv2.VideoWriter('test.avi', fourcc, fps, (int(width), int(height)))

while True:
    # 读取数据帧，返回2个参数
    ret, frame = cap.read()

    # 如果是false的话，表示没有数据，退出循环
    if not ret:
        break

    # 保存
    out.write(frame)

    cv2.imshow('frame', frame)

    # 接收到q键，退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 资源释放
cap.release()
out.release()
cv2.destroyAllWindows()
