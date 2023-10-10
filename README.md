# 算24
## 童年游戏:四张扑克牌(点数1-13),加减乘除算得24.
- A=1;
- J=11;
- Q=12;
- K=13.
例如四张牌分别为`[5,6,10,8]`;一个解法是:`6/(10/5)*8=24`.

## 函数说明
```python
def 算24(n:list,全解:bool=False):
    '''参数:
    n:4个数字组成的列表
    全解:False-找到一个解就返回,字符串;True-找出所有解并以列表返回.
    若无解,则返回空字符串或空数组
    '''
```
## 调用示例:
`算24([11, 6, 10, 5])`返回`(11 - 5) * (10 - 6)`


##对于四张牌的所有排列组合,经计算有解的占77.6%.
