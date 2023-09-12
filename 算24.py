import random

def 排列(数量):
    for i in range(数量):
        for j in set(range(数量)) - set([i]):
            for k in set(range(数量)) - set([i, j]):
                l = set(range(数量)) - set([i, j, k])
                l = l.pop()
                yield (i, j, k, l)

class 四则运算():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def 枚举(self):
        temp=[ 运算(self.a,self.b,'+') ,运算(self.a,self.b,'-'),运算(self.a,self.b,'*')]
        if self.b!=0 :
            temp.append(运算(self.a,self.b,'/'))
        return temp

class 运算():
    def __init__(self,a,b='',op=''):
        self.a=a
        self.b=b
        self.op=op
        if b=='':
            self.v=a
        else:
            if op=='+':
                self.v=a+b
            elif op=='-':
                self.v=a-b
            elif op=='*':
                self.v=a*b
            elif op=='/' :
                self.v=a/b

    def __add__(self,other):
        return self.__class__(self.v,other.v if isinstance(other,运算) else other,'+')

    def __sub__(self,other):
        return self.__class__(self.v,other.v if isinstance(other,运算) else other,'-')

    def __mul__(self,other):
        return self.__class__(self.v,other.v if isinstance(other,运算) else other,'*')

    def __truediv__(self,other):
        return self.__class__(self.v,other.v if isinstance(other,运算) else other,'/')

    def __eq__(self, other) -> bool:
        if isinstance(other,运算):
            return self.v==other.v
        else:
            return self.v==other

    def __str__(self):
        if self.b=='':
            return f'{self.a}'
        a=self.a
        while isinstance(a,运算):a=a.v
        b=self.b
        while isinstance(b,运算):b=b.v
        v=self.v
        while isinstance(v,运算):v=v.v
        return f'{a}{self.op}{b}={v}'

    def __repr__(self) -> str:
        return str(self)

运算优先级={'+':0,'-':0,'*':1,'/':1}
def 算24(n:list,找全解=False):
    '''参数n:4个数字组成的列表
    找全解:False-找到一个解就返回,字符串;True-找出所有解并以列表返回.
    '''
    for 顺序 in 排列(4):
        牌 = []
        for i in range(4):
            牌.append(运算(n[顺序[i]]))
        解=[]
        for op1 in 四则运算(牌[0],牌[1]).枚举():
            for op2 in 四则运算(op1,牌[2]).枚举():
                for op3 in 四则运算(op2,牌[3]).枚举():
                    if op3==24:
                        # print(op1,op2,op3)
                        括号1= 运算优先级[op2.op]>运算优先级[op1.op]
                        括号2= 运算优先级[op3.op]>运算优先级[op2.op]
                        算术表达式=f'{"(" if 括号2 else ""}{"(" if 括号1 else ""}{牌[0]} {op1.op} {牌[1]}{")" if 括号1 else ""} {op2.op} {牌[2]}{")" if 括号2 else ""} {op3.op} {牌[3]}'
                        if not 找全解:return 算术表达式
                        解.append(算术表达式)
        for op1 in 四则运算(牌[0],牌[1]).枚举():
            for op3 in 四则运算(牌[2],牌[3]).枚举():
                for op2 in 四则运算(op1,op3).枚举():
                    if op2==24:
                        # print(op1,op2,op3)
                        算术表达式=f'({牌[0]} {op1.op} {牌[1]}) {op2.op} ({牌[2]} {op3.op} {牌[3]})'
                        if not 找全解:return 算术表达式
                        解.append(算术表达式)
    return 解


if __name__=='__main__':
    # n = [random.randint(1, 13) for i in range(4)]
    # n=[11,2,6,3]
    # n=[5,2,3,5]
    # n=[11,5,6,2]
    # print(n)
    有解=0
    已测=0
    for i in range(1,14):
        for j in range(1,14):
            for k in range(1,14):
                for l in range(1,14):
                    n=[i,j,k,l]
                    解=算24(n)
                    if 解:
                        有解+=1
                    # print(n,解)
                    已测 +=1
                    if 已测%1000==0:
                        print(已测,有解,f'{有解/已测:.1%}')
    print(已测,有解,f'{有解/已测:.1%}')
