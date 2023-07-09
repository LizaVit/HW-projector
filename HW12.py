#1. Write a decorator that ensures a function is only called by users with a specific role. 
#Each function should have an user_type with a string type in kwargs. Example:
'''
def show_customer_receipt(user_type: str):
    def wraper():
        user_type == 'admin'
        if user_type =! "admin" :
            raise ValueError('Permision denied')
        return func(*args, **kwargs)
'''        

def is_admin(func):
    def control(**kwargs):
        if 'user_type' in kwargs and kwargs['user_type'] == 'admin':
            func(**kwargs)
        else:
            raise ValueError('Permision denied')
    return control

@is_admin
def show_customer_receipt(user_type: str):
    print('function pass as it should be')               

show_customer_receipt(user_type = 'admin')
show_customer_receipt(user_type = 'user')

# Write a decorator that wraps a function in a try-except 
# block and prints an error if any type of error has happened.

def catch_errors(fun):
    def wrap(*args, **kwargs):
        try:
            fun(*args, **kwargs)
        except Exception as error:
            print(f'Found 1 error during execution of your function: {type(error).__name__} {str(error)}')
    return wrap

@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])

some_function_with_risky_operation({'foo': 'bar'})
some_function_with_risky_operation({'key': 'bar'})