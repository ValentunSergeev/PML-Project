# PML-Project
This repository is the project for Practical Machine Learning and Deep Learning course at Innopolis University

## Project description
We will be building a pipeline for running Classification/Detection models on Raspberry Pi


## Models
### YOLO
Our first approach was to use YOLO to detect objects. It is one of the leading models to perform object detection. We run it on the samples from the Pascal dataset.

![Yolo output](https://github.com/ValentunSergeev/PML-Project/blob/main/Media/YOLO%20output.png)

Yolo had a long inferrence time ~ 2-3 seconds on laptop CPU, leaving aside the IoT devices.
Thus, our next goal was to find a model which can provide real time object detection.

### Inception
> Used [model_garden repo ](https://github.com/jiteshsaini/model_garden)

The inception models family is used for classification and was developd by Google, it was designed to be a deep network while keeping the number of parameters realtively small.

By running inception models on the Raspberry PI 4 we were able to classifiy in real-time

![Inception output](https://github.com/ValentunSergeev/PML-Project/blob/main/Media/Inception%20output.jpg)

### MobileNet
> Used [model_garden repo ](https://github.com/jiteshsaini/model_garden)

The MobileNet models family is used for Detection and was developd as a light weight models for mobile and embedded vision applications. we used MobileNet SSD v2 to get real-time object detection. SSD is Single Shot object detection this means that it take one shot to detect multiple objects within the image.

![MobileNet output](https://github.com/ValentunSergeev/PML-Project/blob/main/Media/MobileNet%20output.jpg)

## Todo
- Test and analyze more models
- Try to run the models using [ONNX](https://github.com/onnx/onnx) to utalize the built-in GPU


