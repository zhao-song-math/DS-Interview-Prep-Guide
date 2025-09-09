<!-- TOC -->

<!-- /TOC -->

# String [^1][^2]

### 字符串的连接符和内置操作：
加号（+）是字符串的连接符，星号（*）用来复制字符串，请看下面代码：
```
str = 'TuringPlanet'
 
print (str)          # 输出字符串 -> TuringPlanet
print (str + "ENOCH") # 连接字符串 -> TuringPlanetEnoch
print (str * 2)      # 输出字符串两次 -> TuringPlanetTuringPlanet 
print (str[0:-1])    # 输出第一个到倒数第二个的所有字符 -> TuringPlane
print (str[0])       # 输出字符串第一个字符 -> T
print (str[2:5])     # 输出从第三个开始到第五个的字符 -> rin
print (str[2:])      # 输出从第三个开始的后的所有字符 -> ringPlanet
```
**reverse string:** `str[::-1]`


### 有用的字符串函数：
```
name = "Hello World"
print(name.title()) # Hello World
print(name.upper()) # HELLO WORLD
print(name.lower()) # hello world
str1 = "    Hello"
str2 = "  World"
# 用来消除空格的函数
print(str1.strip() + str2.strip()) # HelloWorld
字符串格式化
```

对于单个字符的编码，Python提供了`ord()`函数获取字符的整数表示，`chr()`函数把编码转换为对应的字符：
```
>>> ord('A')
65
>>> ord('中')
20013
>>> chr(66)
'B'
>>> chr(25991)
'文'
```

要计算str包含多少个字符，可以用`len()`函数：
```
>>> len('ABC')
3
>>> len('中文')
2
```

字符串的很多函数都会返回**布尔函数**：
```
string = "Hello Word"
print(string.isalnum()) # 查看是否所有字符都是(A-Z, a-z, 0-9)  -> False
print(string.isalpha()) # (A-Z, a-z)
print(string.isupper()) # Check if string contains upper case
```

### 字符串格式化

我们可以在字符串中带入变量，只要在开头引号前加f就可以了 (f代表format)
```
first_name = "Enoch"
last_name = "Zheng"
full_name = f"{first_name} {last_name}" # Enoch Zheng
full_name2 = f"{first_name.upper()} {last_name.upper()}" # ENOCH ZHENG
```

```
print("%s was born in %d." % ('Python', 1991))
print("{} was born in {}.".format('Python', 1991))
message = "{} was born in {}"
print(message.format('Python', 1991))
lan = 'Python'
year = 1991
print(f"{lan} was born in {year}.")
```


[^1]: [廖雪峰的官方网站](https://liaoxuefeng.com/books/python/basic/string-encoding/index.html)
[^2]: [图灵星球](https://turingplanet.org/2019/08/22/%e5%8f%98%e9%87%8f-%e5%9f%ba%e7%a1%80%e6%95%b0%e6%8d%ae%e7%bb%93%e6%9e%84/#zi_fu_chuan_String)

## Backlinks
- [Leetcode问题目录](Leetcode问题目录.md)
- [125. Valid Palindrome](125-Valid_Palindrome.md)
- [242. Valid Anagram](242-Valid_Anagram.md)