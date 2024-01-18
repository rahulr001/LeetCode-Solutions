# asteroids = [10,2,-5]
# asteroids = [5,10,-5]
# asteroids = [8,-8]
# asteroids = [-2,-1,1,2]
asteroids = [-2, -2, 1, -2]


def asteroidCollision(asteroids):
    res = []

    def po(val1, val2):
        if val1 < val2:
            res.pop()

    for ast in asteroids:
        res.append(ast)
        if ast > 0 or res and ast == res[-1]:
            continue
        else:
            while ast 

    return res


print(asteroidCollision(asteroids))
