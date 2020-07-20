# Traffic Management and Emergency Vehicle Detection

The main objective of the project is to develop an autonomous system to avoid the need of a timer based system in India. The following work has been done in the arena:
1. Machine Learning algorithms have been used to predict the traffic on a road throughout the day so that traffic management strategies can be planned accordingly.

2. Emergency vehicles (such as ambulance) have been detected using OpenCV for better automated prioritization of vehicles.

# Traffic Prediction
The dataset used includes traffic data of 1 year. Since, data has been collected every 3 hours, the dataset has 2920 entries.

<img src = "https://github.com/isha-git/Traffic-Management-and-Emergency-Vehicle-Detection/blob/master/images/TrafficDataset.PNG" width=200>

The dataset input was converted from 'csv' to 'arff' format using the Weka web application. With the limited dataset, an accuracy of 60% has been achieved using Decision Trees. The given code has been implement on Python 2.7 using Weka, which is a Machine Learning library. The weka library can be installed using the pip command before running the code.

The output looks something like this:

<img src = "https://github.com/isha-git/Traffic-Management-and-Emergency-Vehicle-Detection/blob/master/images/TrafficPredicted.PNG" width=400>

# Detecting Emergency Vehicles
A dataset of sample 1000 Ambulance images has been developed. Later, a vector was created for the training of data. Training is done using the Haar Cascade classifiers provided by OpenCV in Python. Multiple stages of training takes place and the algorithm approximately took approximately 3 hour to develop a suitable xml file of 10 stages for the training dataset.

The algorithm was then evaluated on a test video is then passed as the test video. The screenshots of ambulance detection can be seen below:

<img src="https://github.com/isha-git/GreenGo/blob/master/images/AmbulanceDetection.PNG" width=400>

Augmentation can also be used to increase the size of the dataset. 

**Note:** For creating an XML file, we have taken a reference from <a href="https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/">this blog</a>.
