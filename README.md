# Face-Detection 人脸检测系统

### **任务分解**

|                            任务项                            |         进程         |
| :----------------------------------------------------------: | :--------------------: |
|          **加载 Opencv haarcascade_frontalface_alt.xml 分类器。**                       |        **ING**       |
|        **图像的 cvtColor，equalizeHist 处理**                        | **ING** |
|          **使用 detectMultiScale 进行识别**           | **ING** |
|       **使用 rectangle 绘制找到的目标矩形框**                     | **ING** |
|       **在原图像上 ROI 截取彩色的人脸保存**                       |    **ING**     |
