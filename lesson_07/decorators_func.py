def print_decorator (func):
    def wraper(*args, **kwargs):
        print("Start")
        func(*args, **kwargs)
        print("End")

    return wraper

@print_decorator
def show_message(content):
    print(content)

show_message("Hello, world!")