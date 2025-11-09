def print_hello_world ():
    print ("Hello world!")
    
    print_hello_world ()

def add_excla(arg):
       new_arg = arg + "!"
       print (new_arg)

add_excla("hello")

def add_excla(text = 10):
    print(str(text) + "!")
fun_var = add_excla
    print(fun_var("test"))