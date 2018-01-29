# import

#### 问题:

1. import长什么样?
2. import有什么用?
3. import都能引入些什么?
4. 什么是Module, Package, 怎么用?

#### 问题1: import长什么样
```python
import os.path
from modulesample import hello_module, varname
from modulesample import *
import os.path as path
```

#### 问题2: import有什么用
最简单的答案是代码复用. 试想所有功能都写在一个文件里, 也是可以执行的, 但是每个地方都要再写一遍, 将不同的功能放在不同的文件, 按需引入, 大大增强了代码灵活性.

#### 问题3: import都能引入些什么

1. 引入module
2. 从module中引入module内方法\变量等
3. 从package引入module

#### 问题4: 什么是Module, Package, 怎么用?
**神马是module** : module最简单的描述就是一个python文件, 如`modulesample.py`, module名称为文件名`modulesample`, 同目录文件需要引入的话使用`import modulesample`就可以通过`modulesample.xxx()`来使用其中的方法\变量了

**神马是package** : 其实就是个文件夹, 文件夹下多了一个`__init__.py`, python解释器通过这个文件来区分是普通文件夹还是package. package干嘛的呢?我理解最直接的功能就是namespace, 利用物理文件夹让代码结构更清晰, 同时利用namespace减少名字冲突

*示例1 :标准import*

>创建了modulesample.py和hello.py两个文件, 从hello.py中引入了modulesample.py, 然后通过modulesample.hello_module()使用modulesample中的方法了
```python
# modulesample.py 
def hello_module():
    print("hello module")

# hello.py
import modulesample
if __name__ == "__main__":
    modulesample.hello_module()
```

*示例2: from..import*
> 从module中引入具体的方法, 使用的时候可以直接使用hello_module(), 而需要带上modulename(此处为: modulesample)
```python
# hello.py
from modulesample import hello_module

if __name__ == "__main__":
    hello_module()
```

*示例3: import..as*
> import..as用于改变引入模块名称. 

```python
# hello.py
import modulesample as ms

if __name__ == "__main__":
    ms.hello_module()
    print(ms.varname)
```
>根据["python as 用法" http://blog.sina.com.cn/s/blog_76e94d210100vxu1.html](http://blog.sina.com.cn/s/blog_76e94d210100vxu1.html)
>如果想要改变被引入模块在当前模块中的名称，而不是sys.modules中的名称。可以使用import as，例如：
```python
import some as other
print(other.name) 

# 等同于
 
import some
other = some
del some
print(other.name)
```

*示例4: from module import* *
> 使用*可以引入模块内非_开头的方法或变量, **不建议使用, 可能引入些不该引入的内容且很难Debug到, 所以建议需要什么就引入什么**
```python
# hello.py
from modulesample import *

if __name__ == "__main__":
    hello_module()
    print(varname)
```

*示例5: from module import method/variable/class or other items*
> 引入模块内具体方法, 用法同import *, 此处为具体内容
```python
from modulesample import hello_module, varname

if __name__ == "__main__":
    hello_module()
    print(varname)
```

#### 参考
* [官方文档](https://docs.python.org/3/tutorial/modules.html)
* [廖雪峰Python教程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431845183474e20ee7e7828b47f7b7607f2dc1e90dbb000)
* ["python as 用法" http://blog.sina.com.cn/s/blog_76e94d210100vxu1.html](http://blog.sina.com.cn/s/blog_76e94d210100vxu1.html)

