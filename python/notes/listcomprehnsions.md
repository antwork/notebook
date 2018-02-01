# List Comprehensions

>看了各家的教程说明，转了一圈最后发现官网才是最好的。

*链接地址：[https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)*

**官方语法描述：**
>A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it   
>中文版：左中括号 表达式 for子句 0个或多个for子句或if子句 右中括号 

缩写为：

[expression for item in iterable for other in iterable, ... if xxx]

List Comprehension可以替换map\reduce\filter三个高阶函数，实际在Visual Studio Code中pylint也会警告*map/filter on lambda could be replaced by comprehension*

### 示例1：map功能

```python
>>> values = [1, 2, 3, 4]
>>> values = [x * 2 for x in values]
>>> values
[2, 4, 6, 8]

# 等同于

>>> values = [1, 2, 3, 4]
>>> values = map(lambda x: x * 2, values)
>>> values
[2, 4, 6, 8]
```

### 示例2：filter功能

```python
>>> values = [1, 2, 3, 4]
>>> values = [x for x in values if x % 2 == 0]
>>> values
[2, 4]

# 等同于

>>> values = filter(lambda x: x % 2 != 0, values)
>>> values
[1, 3]
```

### 示例3：reduce功能
```python
>>> values = [[1, 2, 3], [4, 5], [6, 7]]
>>> values = [item for sub in values for item in sub]
>>> values
[1, 2, 3, 4, 5, 6, 7]

# 等同于

>>> values = [[1, 2, 3], [4, 5], [6, 7]]
>>> values = reduce(lambda x, y: x + y, values, [])
>>> values
[1, 2, 3, 4, 5, 6, 7]

# 小思考
>>> values = [[1, 2, 3], [4, 5], [6, 7]]
>>> values = reduce(lambda x, y: x.extend(y), values, [])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <lambda>
AttributeError: 'NoneType' object has no attribute 'extend'

为什么会报错???
```

### 示例4： 列表生成tuple
```python
>>> values = ["life", "is", "short", "you", "need", "python"]
>>> values = [(item, item.upper(), len(item)) for item in values]
>>> values
[('life', 'LIFE', 4), ('is', 'IS', 2), ('short', 'SHORT', 5), ('you', 'YOU', 3), ('need', 'NEED', 4), ('python', 'PYTHON', 6)]
```

### 示例5： 嵌套list comprehensions
>虽然是官网例子，但都是我手打出来的

```python
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# 个人推荐类型
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


>>> transposed = []
>>> for i in range(4):
...     transposed_row  = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
### 备注：
1. 官网强调，如果要生成tuple数组，必须在for循环前使用()， 否则会报语法错误

```python
>>> values = ["life", "is", "short", "you", "need", "python"]
>>> values = [item, item.upper() for item in values]
  File "<stdin>", line 1
    values = [item, item.upper() for item in values]
                                   ^
SyntaxError: invalid syntax

```
2. 格式要求，逗号、冒号后添加一个空格，中括号、小括号左右不要留空格

```python
yes
values = [[1, 2, 3], [4, 5], [6, 7]]
values = filter(lambda x: x % 2 != 0, values)
values = [item for sub in values for item in sub]

no
values = [ [1,2,3],[4,5],[6,7] ]
values = filter( lambda x:x % 2 != 0, values )
values = [ item for sub in values for item in sub ]
```

### 遇到的问题？
*reduce打平数组那里我也犯错了，答案其实挺简单，list.extend(another)返回的None, 而reduce希望expression能够返回一个新数组，None终结了运行。