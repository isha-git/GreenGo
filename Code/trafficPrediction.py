"""
https://github.com/isha-git
https://github.com/shripriyamaheshwari
"""

import weka.core.jvm as jvm #weka requires java toolkit
import weka.core.converters as con #for converting the data set
from weka.clusterers import Clusterer #for clustering
from weka.classifiers import Classifier
from weka.core.dataset import Instances
from weka.core.dataset import Instance
from weka.classifiers import Evaluation, PredictionOutput
from weka.core.classes import JavaObject
import javabridge
import numpy
import random


jvm.start() #starting jvm
data = con.load_any_file("traffictrainroad1.arff") #to load the required file
data_copy = Instances.copy_instances(data)
test = con.load_any_file("traffictestroad1.arff")
test_copy = Instances.copy_instances(test)
test.delete_last_attribute()
data.class_is_last()
#separate_test = Instances.template_instances(test_copy)



class Instances(JavaObject):
	def __init__(self, jobject):
		self.__num_attributes = javabridge.make_call(self.jobject, "numAttributes", "()I")


	def num_attributes(self):
		return self.__num_attributes()

	num_of_attr = num_attributes(data)
	#print("number of Attributes:",num_of_attr)


	count_instances = 0
	for inst in data:
		count_instances = count_instances + 1
	#print(count_instances)
	#print(len(data))

	trees = Classifier(classname="weka.classifiers.trees.J48")
	trees.build_classifier(data)

	#print(trees)



	data.class_is_last()
	test_copy.class_is_last()
	correct_count = 0
	result = list()
	traffic = list()
	#print(len(test_copy))
	print("Today's traffic on Road 1 will be: ")
	for index, inst in enumerate(test_copy):
		pred = trees.classify_instance(inst)
		predicted_value = inst.class_attribute.value(int(pred))#converts integer label to string
		if(index >=888):
			#print(predicted_value)	
			result.append(predicted_value)
	for item in result:
		if item == 'high':
			number = random.randint(200, 400)
			traffic.append(number)
		if item == 'medium':
			number = random.randint(300,600)
			traffic.append(number)
		if item == 'low':
			number = random.randint(500,700)
			traffic.append(number)
		
	print"12 a.m. - 3 a.m.", traffic[0]
	print"3 a.m. - 6 a.m.", traffic[1]
	print"6 a.m. - 9 a.m.", traffic[2]
	print"9 a.m. - 12 p.m.", traffic[3]
	print"12 p.m. - 3 p.m.", traffic[4]
	print"3 p.m. - 6 p.m.", traffic[5]
	print"6 p.m. - 9 p.m.", traffic[6]
	print"9 p.m. - 12 a.m.", traffic[0]+10
		#actual = inst.get_value(num_of_attr-1)
		#actual_value = inst.class_attribute.value(actual)
		#if (predicted_value == actual_value):
		#	correct_count = correct_count+1
		#else:
		#	continue
	#correct_count = float(correct_count)
	#total = len(test_copy)
	#total = float(total)
	#print(correct_count/total)


	jvm.stop()
