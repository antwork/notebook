#!/usr/bin/env python3
# coding:utf-8

class Student(object):

	def __init__(self, name, gender):
		self.__name = name
		self.__gender = gender
		self._private_old = 1

	def get_name(self):
		return self.__name

	def get_gender(self):
		return self.__gender

	# 使用setter访问私有属性
	# 使用setter校验器参数
	def set_gender(self, gender):
		if gender != "male" and gender != "female":
			raise ValueError("春哥是个传说, 你只能成为东方不败")
		else:
			self.__gender = gender


def main():
	stu = Student("qxu", "male")

	# 直接访问带以__的私有属性, 会报AttributeError
	# print(stu.__name)
	# AttributeError: 'Student' object has no attribute '__name'

	if hasattr(stu, '__name'):
		print("stu have attribute __name")
	else:
		print("stu not have attribute __name")
	# stu not have attribute __name

	print("name: " + stu.get_name())
	print("gender: " + stu.get_gender())
	# name: qxu
	# gender: male

	stu.set_gender("female")
	print("gender: " + stu.get_gender())
	# gender: female

	print("old: " + str(stu._private_old))
	# old: 1

if __name__ == "__main__":
	main()