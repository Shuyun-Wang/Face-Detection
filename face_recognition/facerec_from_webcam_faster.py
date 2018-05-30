import face_recognition
import cv2




# 获取摄像头的权限 #0 (the default one)
video_capture = cv2.VideoCapture(0)

# 加载图片，进行学习训练
face_image = face_recognition.load_image_file(str)
image_face_encoding = face_recognition.face_encodings(face_image)[0]


# 创建一个已知的人脸编码数组和所对应的名字
known_face_encodings = [
    image_face_encoding
]
known_face_names = [
    "Barack Obama",
]

# 初始化一些列表
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # 获取视频的一个画面
    ret, frame = video_capture.read()

    # 重新调整视频画面为1/4大小
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # 转变的图片的颜色空间为RGB
    rgb_small_frame = small_frame[:, :, ::-1]

    # 只处理视频的每一个画面来节省时间
    if process_this_frame:
        # 找出当前帧的所有面部
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # 检测当前脸是否和已知的脸匹配
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # 如果在已有的人脸库中找到相匹配人脸，选定
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # 展示结果
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # 将我们检测到的人脸位置缩小到原来1/4大小
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # 选定人脸识别
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # 人脸下显示姓名
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # 展示图片结果
    cv2.imshow('Video', frame)

    # 'q'结束退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头的权利
video_capture.release()
cv2.destroyAllWindows()