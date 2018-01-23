#!/usr/bin/env python3
# coding:utf-8

class Animal(object):

	def __init__(self, name):
		self.name = name

	def run(self):
		print("Animal is running")

class Dog(Animal):

	def __init__(self, name, gender):
		self.gender = gender
		super(Dog, self).__init__(name)

	def run(self):
		super(Dog, self).run()
		print("dog dog run")

def main():
	dog = Dog("budi", "male")
	print("name: " + dog.name)
	print("gender: " + dog.gender)
	dog.run()
	# name: budi
	# gender: male
	# Animal is running
	# dog dog run

if __name__ == "__main__":
	main()