def addition_simplified(*args):
    return sum(args)

addition_simplified(3,5,7,12,14,55)

##

def what_are_kwargs(*args,**kwargs):
    print(args)
    print(kwargs)

what_are_kwargs(12,34,56,name="Jose", location="UK")
