import decorator


# TODO write commone
@decorator.time_consuming
def function():
    print("a")


function()
