def newton(function, derivative, error=0):
    x = 1
    fx = function(x)
    dfx = derivative(x)
    k = 0
    while abs(fx) > error:
        xk = x - fx / dfx
        x = xk
        fx = function(x)
        dfx = derivative(x)
        k += 1
    print(fx)
    print(xk)
    print(k)

if __name__ == '__main__':
    from math import cos, sin
    from exponential import exponential as e

    function = lambda x: e(x) - 2 * cos(x)
    derivative = lambda x: e(x) + 2 * sin(x)
    newton(function, derivative, 10**-7)