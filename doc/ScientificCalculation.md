# 科学计算文档

[TOC]

## 模板

```python
sympy
#注释
a=cos(pi)

show([a])
play
```

## 输出结果

最后一行输入`play`，学妹会将结果渲染为图片并输出
部分命令无法渲染的，必须调用`show()`以文本形式输出
`show()`以文字消息输出结果
单变量：`show(单变量)`
多变量：`show([变量1，变量2，变量3])`

## 功能

### 符号表示

```python
# 变量名=Symbol(‘变量表达式’)
a=Symbol(‘alpha**2’)
x=Symbol(‘x’)
```

变量名要求为单个字母

支持希腊字母（以英文拼写）和数学常数

### 恒等变换

#### 展开方程

```python
# 表达式.expand( )展开方程
((x+y)**3).expand()
```

#### 折叠方程

```python
# facrot(表达式)折叠方程
factor(x**2 + 2*x*y + y**2)
```

#### 分离分式

```python
# apart(表达式)分离分式
apart((x+3)/(x-1))
```

#### 合并分式

```python
# together(表达式)合并分式
together(1/x+1/y+1/z)
```

### 化简

#### 常规化简

```python
# simplify( )常规化简
simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1))
```

#### 三角化简

```python
# trigsimp( )三角化简
trigsimp(sin(x)/cos(x))
```

#### 指数化简

```python
# powsimp( )指数化简
powsimp(x**a*x**b)
```

### 解方程

#### 解方程

第一个参数为要解的方程，要求右端等于0，第二个参数为要解的未知数

```python
# 二元一次方程
solve([2 * x - y - 3, 3 * x + y - 7],[x, y])
```

### 极限

#### 求极限

```python
# limit(函数,变量,趋近于,可选:趋近方向)求极限
# 无穷用两个小写的oo表示.
# dir='+'求右极限,'-'求左极限,''求极限
# 不写dir也是求极限
limit(1/x,x,2)
a=limit(1/x,x,oo,dir='-')
show([a])
```

### 微积分

#### 求导

```python
# diff(函数,求导变量,可选:求导阶数)求导
diff(x**3,x,2)
```

#### 不定积分

```python
# integrate(被积函数,积分变量)不定积分
integrate(sin(x),x)
```

#### 定积分

```python
# integrate(被积函数,(积分变量,下限,上限))定积分
integrate(sin(x),(x,0,pi/2))
```

### 微分方程

#### 微分方程

```python
#以 y′=2xy 为例
f =Function('f')
a=dsolve(diff(f(x),x) - 2*f(x)*x,f(x))
show([a])
```

### 矩阵化简