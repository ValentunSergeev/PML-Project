import cv2
import requests

import json

from pipeline.models import Frame, Detection

HOST_URL = "http://127.0.0.1:8000"


def send_frame(frame: Frame, cv_image):
    imencoded = cv2.imencode(".jpg", cv_image)[1]
    file = {'image': ('frame.jpg', imencoded.tobytes(), 'image/jpeg', {'Expires': '0'})}

    data = {'frame': json.dumps(frame.dict())}

    return requests.post(f"{HOST_URL}/frames/", files=file, data=data, timeout=5)


if __name__ == "__main__":
    frame = Frame(
        detections=[
            Detection(
                startX=0.0,
                startY=0.0,
                endX=1.0,
                endY=1.0,
                category="cat",
                confidence=0.99,
            )
        ],
        deviceId="sample_id"
    )

    cv_image = cv2.imread("sample_dog.jpg", cv2.COLOR_BGR2RGB)
    response = send_frame(frame, cv_image)

    print(response.text)
