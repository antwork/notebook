#!/usr/bin/env python3
# coding:utf-8

class Student(object):

	# 统计初始次数
	count = 0

	def __init__(self, name):
		self.name = name

		Student.count += 1

def main():
	stu = Student("qxu")
	print("stu count:" + str(stu.count))
	# stu count:1

if __name__ == "__main__":
	main()
