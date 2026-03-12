# a = [1,2,3,4,5,6,7,8,9,10,11,12]
# even = list(filter(lambda x: x%2==0,a))
# odd = list(filter(lambda x: x!=0,a))
# result = even+odd
# print(result)

# reduce with lambda

# from functools import reduce
# l=[1,2,3,4,5]
# res = reduce(lambda x,y : x if x>y else y,l)
# print(res)


# from functools import reduce
# l=[1,2,3,4,5]
# res = reduce(lambda x,y : x if x<y else y,l)
# print(res)


#Decorator
#What is a Decorator in Python?
#A decorator is a function that modifies or extends the behavior 
# of another function without changing its actual code.

def outer(var):
    def inner():
        var()
    return inner
def show():
    print("from show function")
res = outer(show)
res()