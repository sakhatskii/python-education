class Closure:
    def outer_function(self, x):
        def inner_function(y):
            return x * y
        return inner_function


closure = Closure().outer_function(7)

print(closure(5))  # 35 (7 * 5)
