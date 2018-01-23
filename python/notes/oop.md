# Python面向对象编程

#### 1. 基本类		

```python
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

```
[示例代码(student_base.py)](../demos/student_base.py)

#### 2. 实例变量      
```python
## python的可以动态添加实例属性
stu.score = 100
print("score: " + str(stu.score))
# score: 100

# 判断是否拥有某属性
if hasattr(stu, 'score'):
	print("stu has attri score")
else:
	print("stu don't has attr score")

del stu.score

if hasattr(stu, 'score'):
	print("stu has attri score")
else:
	print("stu don't has attr score")
# stu has attri score
# stu don't has attr score

```

##### 2.1 私有属性及Getter\Setter    

> * 使用`__varname`(双下横线+属性名)定义私有属性, 外部无法通过`stu.varname`直接访问, 私有变量实际转化为`_classname__variable`, 所以可通过stu._Student__name直接访问私有变量, 实际是变相私有, 怎么使用还是看开发者自己    
> * 通过getter方法将私有变量暴露给外部, 使用方法`def get_xxx(): pass`    
> * 通过setter方法对参数校验, 避免直接写入错误数据    
        

```python
...
def __init__(self, name, gender):
	self.__name = name
	self.__gender = gender

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


...
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
```
[示例代码(student_private.py)](../demos/student_private.py)

##### 2.2 可访问私有属性(但不推荐访问)
> 使用`_varName`单横线变量名组合创建   
> 该命名仅有指示作用, 实际可以通过obj._varname进行访问


```python
_name = "name" # 单横线_VarName

# 示例
def __init__(self, name, gender):
	...
	self._private_old = 1

stu = Student("qxu", "male")

print("old: " + str(stu._private_old))
# old: 1

```

[示例代码(student_private.py)](../demos/student_private.py)

#### 3. 类变量
> 所有类实例共享类变量   
> 通过ClassName.class_property访问设置类变量

```python
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

```

#### 4. 继承\多态

##### 4.1 继承
>子类默认继承父类方法, 所以啥不写也能调用父类方法 

```python
class Animal(object):
	def run(self):
		print("Animal is running")

class Dog(Animal):
	pass

class Cat(Animal):
	pass

def main():
	dog = Dog()
	dog.run()

	cat = Cat()
	cat.run()
	# Animal is running
	# Animal is running

if __name__ == "__main__":
	main()
```

##### 4.2 多态:子类默认继承父类方法, 所以啥不写也能调用父类方法 
> 当参数是父类型时, 传入不同的子类实例, 触发方法时会优先调用子类方法, 从而实现调用同一方法, 不同子类的实例会有不同的响应

```python
class Animal(object):
	def run(self):
		print("Animal is running")

class Dog(Animal):
	def run(self):
		print("dog dog run")

class Cat(Animal):
	def run(self):
		print("cat cat run")

def runRunAnimal(animal):
	animal.run()
	animal.run()

def main():
	dog = Dog()
	cat = Cat()
	runRunAnimal(dog)
	runRunAnimal(cat)

	# dog dog run
	# dog dog run
	# cat cat run
	# cat cat run

if __name__ == "__main__":
	main()
```

##### 4.3 子类调用父类方法
> 使用`super(Self_Class_Name, self).fun_name(param)`调用父类方法
> 示例1: `super(Dog, self).__init__(name)`   
> 示例2: `super(Dog, self).run()`

```
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
```