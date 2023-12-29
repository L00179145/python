square_text = "Square of X after import="

def square(x):
    return x*x

print("Square of X is=", square(3))

if __name__ == '__main__':
    print(f"This module is called {__name__} and executes as a standalone script")
else:
    print(f"This module is called {__name__} and is being called by another script")
