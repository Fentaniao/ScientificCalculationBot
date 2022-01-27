# 绘图文档

[TOC]

## 模板

```python
function('p1','p2')
```

==每个参数前后必须加上单引号==

## 功能

### 一元函数

绘制并输出一元显函数

`draw(fun, x_arange)`

```python
# 绘制并输出一元显函数
draw_fun('sin(x) / x', '-10，10，0.1')
```

### 隐函数

绘制并输出二元隐函数

`draw_imp(fun, x_arange,y_arange)`

```python
# 绘制并输出二元隐函数
draw_imp('17 * x**2 -16*abs(x)*y + 17 * y**2-256','-6,6','-6,6')
```

### 参数方程

绘制并输出单参数的参数方程

`draw_para(x_eq, y_eq, t_arrange)`

```python
# 绘制并输出单参数的参数方程
draw_para('2*sin(t)','3*cos(t)','0, 2*pi, 0.1')
```
