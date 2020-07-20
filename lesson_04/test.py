def cal(make, salery, prize):
    try:
        return make * salery + prize
    except TypeError:
        return

def hello(name):
    print(f"Hello, {name}")