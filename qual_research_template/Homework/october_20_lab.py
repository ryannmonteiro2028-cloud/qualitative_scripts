# october_20_lab.py

        
def hello_five_times():
    for _ in range(5):
        print("hello world")

hello_five_times()

def hello_with_validation(user_input):
    valid_inputs = {"yes", "y", "true", "ok"}
    if str(user_input).lower() in valid_inputs:
        print("hello world")
    else:
        raise ValueError("Invalid input. Please enter one of: yes, y, true, ok.")

# example
hello_with_validation("yes")  

def hello_limited_times(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    
    if n > 5:
        raise ValueError("Number too large. Cannot exceed 5.")
    
    for _ in range(n):
        print ("hello world")
    
hello_limited_times(3)
