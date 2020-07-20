# Traffic Management and Emergency Vehicle Detection

The main objective of the project is to develop an autonomous system to avoid the need of a timer based system in India. The following work has been done in the arena:
1. Machine Learning algorithms have been used to predict the traffic on a road throughout the day so that traffic management strategies can be planned accordingly.

2. Emergency vehicles (such as ambulance) have been detected using OpenCV for better automated prioritization of vehicles.

# Traffic Prediction

We have used Decision Trees to train our dataset which looks like:

<img src = "https://github.com/isha-git/Traffic-Management-and-Emergency-Vehicle-Detection/blob/master/images/TrafficDataset.PNG" width=200>

Python is used to implement the code using Weka which is a Machine Learning library. It takes the dataset input in 'arff' format, that is why we converted the csv format to arff using the Weka web application. With the limited dataset, our model provided an accuracy of 60%, however, will a large dataset, it can be improved significantly. The given code runs fine with Python version 2.7. You need to install weka library using the pip command before running the code.

The output will look something like this:

<img src = "https://github.com/isha-git/Traffic-Management-and-Emergency-Vehicle-Detection/blob/master/images/TrafficPredicted.PNG" width=400>

# Detecting Emergency Vehicles

We are detecting emergency vehicles using OpenCV in Python. A dataset of sample 1000 Ambulance images has been developed. Later, a vector is created for the training of data. Training is done using the classifiers provided by OpenCV. Haar Cascade is one such classifier. It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images. Multiple stages of training takes place and this algorithm approximately took 3 hour to develop a suitable xml file of 10 stages as our training dataset. A video is then passed as the test video to check whether the algorithm detects the ambulance accurately. Here are the screenshots of the image detection:

<img src="https://github.com/isha-git/GreenGo/blob/master/images/AmbulanceDetection.PNG" width=400>

One could also use augmentation to increase the size of the dataset. 

**Note:** For creating an XML file, we have taken a reference from this <a href="https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/">blog</a>

