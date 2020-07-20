# Traffic Management and Emergency Vehicle Detection

The main objective of the project is to develop an autonomous system to avoid the need of a timer based system in India. The following work has been done in the arena:
1. Machine Learning algorithms have been proposed to predict the traffic on a road throughout the day so that traffic management strategies can be planned accordingly.

2. Emergency vehicles (such as ambulance) have been detected using OpenCV for better automated prioritization of vehicles.

**Machine Learning Algorithm**

We have used Decision Trees to train our dataset which looks like:

Python is used to implement the code using Weka which is a Machine Learning library. It takes the dataset input in 'arff' format, that is why we converted the csv format to arff using the Weka web application. With the limited dataset, our model provided an accuracy of 60%, however, will a large dataset, it can be improved significantly. The given code runs fine with Python version 2.7. You need to install weka library using the pip command before running the code.

The output will look something like this:


<!-- # Traffic Prediction
Decision trees are trained on the dataset provided by the counters. Our current model has been trained on a data of 1 year. Since, data has been collected every 3 hours, that leads to a total entries of 2920. Training a machine on large amount of data results in better outcome. Our current model provides an accuracy of 60 percent. However, with the passage of time, as more data is collected, accuracy will exponentially increase.
The general form of a decision tree is illustrated below:>
