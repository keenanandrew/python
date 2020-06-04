# a decorator is a function that takes another function and does something to it
# Amends it, or precedes/follows it with notes, etc

def announce(f):
    def wrapper():
        print("About to GO!")
        f()
        print("Phew, done with that function.")
    return wrapper

# this is how decorators are added - with @
@announce
def hello():
    print("Sup motherfuckers")

hello()
