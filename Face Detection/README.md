# Face-Detection 全脸检测系统

### **任务分解**

|                            任务项                            |         进程         |
| :----------------------------------------------------------: | :--------------------: |
|          **加载 face_recognition, open-cv 包**                       |        **ENG**       |  
|        **使用open-cv的cv.VideoCapture(0)来获取摄像头的权限**                        | **ENG** |
|        **图像的颜色空间处理，转换为RGB**                        | **ENG** |
|          **使用 face_locations 进行识别, 使用face_encodings进行编码**           | **ENG** |
|          **使用 face_recognition.compare_faces 进行人脸匹配识别**           | **ENG** |
|       **使用 cv.rectangle 绘制找到的目标矩形框**                     | **ENG** |
|       **使用open-cv中的样式来打印人脸对应名称**                       |    **ENG**     |
|       **执行结束后释放摄像头的权限 release**                       |    **ENG**     |
