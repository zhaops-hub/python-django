import base64
import urllib

import numpy as np
from django.http import HttpResponse, HttpRequest, JsonResponse
import cv2

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

face_detector = "haarcascade_frontalface_default.xml"


def reg(request: HttpRequest):
    return HttpResponse("test")


def get_image(request: HttpRequest):
    img = cv2.imread("E:\\1.jpg")
    imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imwrite("E:\\2.jpg", imgGray)
    return HttpResponse("成功")


@csrf_exempt
def face_detect(request):
    default = {"safely executed": False}  # 初始未执行
    # 规定客户端使用POST请求上传检测图片
    if request.method == "POST":
        if request.FILES.get("image", None) is not None:
            image_to_read = read_image(stream=request.FILES["image"])

        else:
            default["error_value"] = "提交格式错误，无法解析到image图像"
            return JsonResponse(default)

        imgGray = cv2.cvtColor(image_to_read, cv2.COLOR_BGR2GRAY)  # 彩色图像转灰度
        detector_value = cv2.CascadeClassifier(face_detector)  # 生成人脸检测器

        # 进行人脸检测
        values = detector_value.detectMultiScale(imgGray,
                                                 scaleFactor=1.1,
                                                 minNeighbors=5,
                                                 minSize=(30, 30),
                                                 flags=cv2.CASCADE_SCALE_IMAGE)
        # 将检测得到的人脸检测关键点坐标封装
        values = [(int(a), int(b), int(a + c), int(b + d)) for (a, b, c, d) in values]

        for (w, x, y, z) in values:
            cv2.rectangle(image_to_read, (w, x), (y, z), (0, 255, 0), 2)

        buffer_img = cv2.imencode('.jpg', image_to_read)
        img64 = base64.b64encode(buffer_img[1])  # base64编码转换用于网络传输
        img64 = str(img64, encoding='utf-8')  # bytes转换为str类型
        default["img64"] = img64  # json封装

    return JsonResponse(default)


def read_image(stream=None, url=None):
    if url is not None:
        response = urllib.request.urlopen(url)
        data_temp = response.read()

    elif stream is not None:
        data_temp = stream.read()

    image = np.asarray(bytearray(data_temp), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image
