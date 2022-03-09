def y(v0,t):
    """calcula posição vertical de um corpo"""
    g = 9.8
    return v0 * t - 1 / 2 * g * (t**2)
help(y)
y(1,2)
