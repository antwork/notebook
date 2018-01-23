# python文件格式

示范代码: hello.py

```python
#!/usr/bin/env python
# coding:utf-8

def main():
	print "hello world"

if __name__ = "__main__":
	main()

```

1. `#!/usr/bin/env python`   
   * 作用: 脚本语言的第一行, 目的是指出该脚本语言应该用什么程序去运行
   * 区别: `#!/usr/bin/env python` vs `#!/usr/bin/python` 
   * 备注: 该行其实可以不写, 当有的时候可以使用`$ ./hello.py`执行python脚本. 如果没有这一行, 需要使用`$ python hello.py`运行, 
  
   >
   `#!/usr/bin/python`是告诉操作系统执行这个脚本的时候，调用/usr/bin下的python解释器；    
`#!/usr/bin/env python`这种用法是为了防止操作系统用户没有将python装在默认的/usr/bin路径里。当系统看到这一行的时候，首先会到env设置里查找python的安装路径，再调用对应路径下的解释器程序完成操作；    
`#!/usr/bin/python`相当于写死了python路径；    
**`#!/usr/bin/env python`**会去环境设置寻找python目录,推荐这种写法；    
来源:[http://blog.csdn.net/wh_19910525/article/details/8040494](http://blog.csdn.net/wh_19910525/article/details/8040494)


2. ```# coding:utf-8```
    * 作用: python 2.x默认编码为ASCII, 如果写中文会报错, 所以需要在第一行或第二行中告知编码格式    
   
    	>SyntaxError: Non-ASCII character '\xe7' in file hello.py on line 5, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
    * 区别: `# -*- coding: utf-8 -*- ` vs `# coding: utf-8`  vs `# coding= utf-8`
       - `# -*- coding: utf-8 -*- `编辑器识别编码模式
       - 另外两个符合正则表达式即可`coding[:=]\s*([-\w.]+)`, 所以coding:和coding=都一样
    * 参考: 
       - [http://blog.csdn.net/orangleliu/article/details/8755461](http://blog.csdn.net/orangleliu/article/details/8755461)
       - [https://www.python.org/dev/peps/pep-0263/](https://www.python.org/dev/peps/pep-0263/)


3. `__name__`说明   
   * 使用`$ python hello.py` 或 `$ ./hello.py` 执行时
`__name__` = `__main__`   

   * 使用`import hello.py`时, 
`__name__` = module_name 即 hello.py的文件名"hello"
