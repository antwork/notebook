#!/usr/bin/env python3
# coding:utf-8

class Student(object):

	def __init__(self, name, gender):
		self.name = name
		self.gender = gender


def main():
	stu = Student("qxu", "male")
	print("name: " + stu.name)
	print("gender: " + stu.gender)
	# name: qxu
	# gender: male


if __name__ == "__main__":
	main()