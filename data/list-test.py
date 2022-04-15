def fun(x):
    if x>0:
        fun(x-1)
        print(x)

fun(3)
