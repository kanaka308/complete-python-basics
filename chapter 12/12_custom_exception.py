


def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good bro")


a = increment('56p')

print(a)