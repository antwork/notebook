# import的思考

### 1. from...import的意义
>导入模块(包)的某个部分, 注意这时并没有导入模块, 所以使用模块会报错, 但是此时可以直接使用模块内引入的方法或

```python
# p1.py
def hello_p1():
    print("hello p1.py")

# p2.py
from p1 import hello_p1

def hello_p2():
    # p1.hello_p1() # 出错 NameError: name 'p1' is not defined, 因为仅导入hello_p1方法, 
    hello_p1()

if __name__ == "__main__":
    hello_p2()
```

### 2. package使用
>将模块分割为多个文件, 但是外部保留与单文件相同的使用方式

原方式 

```python
# mymodule.py
class A:
    def spam(self):
        print('A.spam')

class B(A):
    def bar(self):
        print('B.bar')


```

新方式
```python
文件结构
mymodule/
    __init__.py
    a.py
    b.py

# a.py
class A(object):
    def spam(self):
        print("A.spam")

# b.py
class B(object):
    def bar(self):
        print("B.bar")

# __init__.py
from .a import A
from .b import B

# test.py
import mymodule

a = mymodule.A()
a.spam()

b = mymodule.B()
b.bar()
```
### 参考
[http://python3-cookbook](http://python3-cookbook.readthedocs.io/zh_CN/latest/c10/p04_split_module_into_multiple_files.html
)