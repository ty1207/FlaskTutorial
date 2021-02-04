#Python upper() 方法将字符串中的小写字母转为大写字母。
#str.upper()
#str = "this is string example....wow!!!";
#print "str.upper() : ", str.upper()
#str.upper() :  THIS IS STRING EXAMPLE....WOW!!!

def to_upper_case(aaa):
    return aaa.upper()

name = "quanquan616"

print(f"{to_upper_case(name)} is funny.")

print("="*50,"分割线","="*50)

# 定义函数
def printme(str):
    # 打印任何传入的字符串
    print(str)
    #return

# 调用函数
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")

print("="*50,"分割线","="*50)
# 定义一个函数
def sayHello():
    print("Hello world")
# 执行上面定义的函数
sayHello()

print("="*50,"分割线","="*50)

# 定义可以打印出任何讯息的函数,函数参数的设计，让每次执行函数的时候有弹性
def say(msg):
    print(msg)
# 执行上面定义的函数
say("Hello Fuction")
say("Hello Python")

print("="*50,"分割线","="*50)

# 定义一个可以做加法的函数
def add(n1,n2,n3):
    result1 = n1 * n2 * n3
    result2 = n1 + n2 + n3
    print(result1)
    print(result2)
#执行上面定义的函数
add(1,2,3)
add(2,2,2)
add(3,3,3)

print("="*50,"分割线","="*50)

# 函数运行完成，返回return就是none
def say(msg):
    print(msg)
    return
value = say("Hello Fuction")
print(value)

print("="*50,"分割线","="*50)

# 函数回传字符串 Hello
def add(n1,n2):
    result = n1 + n2
    #print(result)
    return "Hello"
# 执行函数，取得回传值
value = add(3,4)
print(value)

print("="*50,"分割线","="*50)

# 函数回传字符串 result的值
def add(n1,n2):
    result = n1 + n2
    #print(result)
    return result
# 执行函数，取得回传值
value = add(3,4)
print(value)

print("="*50,"分割线","="*50)
# 定义一个乘法函数
# 函数内部的程序，或是没有被调用，就不会有结果返回
def multiply(n1,n2):
    #print(n1 * n2)
    return n1 * n2
# 执行函数
value = multiply(3,4)+multiply(5,10)+multiply(10,10)
print(value)

print("="*50,"分割线","="*50)
# 函数可以做程式的包装，同样的逻辑可以重复利用
def calculate(max):
    sum = 0
    for n in range(1,max+1):
        sum = sum + n
    print(sum)

calculate(10)
calculate(20)



