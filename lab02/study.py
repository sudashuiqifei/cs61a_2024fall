def sum_naturals(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total

def sum_cubes(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k*k*k, k + 1
    return total

def pi_sum(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + 8 / ((4*k-3) * (4*k-1)), k + 1
    return total

# print(sum_naturals(100))
# print(sum_cubes(100))
# print(pi_sum(100))

# 作为参数的函数
def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def cube(k):
    return  k*k*k

def identity(x):
    return x

def pi_term(k):
    return 8 / ((4*k-3) * (4*k-1))


# print(summation(100, cube))
# print(summation(100, identity))
# print(summation(100, pi_term))

# 作为通用方法的函数
def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    return 1/guess + 1

def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)

def approx_eq(x, y, tolerance = 1e-15):
    return abs(x - y) < tolerance

# print(improve(golden_update, square_close_to_successor))

# 嵌套定义
def average(x, y):
    return (x + y) / 2

def sqrt(a):
    def sqrt_update(x):
        return average(x, a/x)
    def sqrt_close(x):
        return approx_eq(x*x, x)
    return improve(sqrt_update, sqrt_close)

# 作为返回值的函数
def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

# 牛顿法
def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update

def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)

# 平方
def square_root_newton(a):
    def f(x):
        return x * x - a
    def df(x):
        return 2 * x
    return find_zero(f, df)
# print(square_root_newton(64))

# 推广到n次方
def power(x, n):
    """返回 n 个 x 相乘"""
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product
# print(power(2, 3))

def nth_of_a(n, a):
    def f(x):
        return power(x, n) - a
    def df(x):
        return n * power(x, n - 1)
    return find_zero(f, df)

# print(nth_of_a(2, 64))
# print(nth_of_a(3, 64))
# print(nth_of_a(6, 64))

# 柯里化——使用高阶函数将一个接收多个参数的函数转化为一个函数链
# 定义power函数的柯里化
def curried_power(x):
    def h(y):
        return power(x, y)
    return h

# print(curried_power(2)(3))

def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start = start + 1

# 用map_to_range和curried_pow计算2的前十次方
# print(map_to_range(0, 10, curried_power(2)))

# Lambda表达式
s = lambda x : x * x
# print(s(10))

# 函数装饰器
def trace(fn):
    def wrapped(x):
        print('->', fn, '(', x, ')')
        return fn(x)
    return wrapped

@trace
def triple(x):
    return 3 * x

# print(triple(12))

def sum_digits(y):
    """Return the sum of the digits of non-negative integer y."""
    total = 0
    while y > 0:
        total, y = total + y % 10, y // 10
    return total
print(sum_digits(519))