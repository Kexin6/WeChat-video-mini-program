def curvePre():
    a = 25
    def curve(x):
        return(a * x * x)
    return curve
f = curvePre()
print(f(2))

