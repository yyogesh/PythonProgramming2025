print("\nLocal and Global Variables Examples:")

global_var = "I'm global"

def local_function():
    global global_var
    local_var = "I'm local"
    global_var = "I'm also global"
    print(local_var)
    print(global_var)
    print("Inside local_function:", locals())
    print("Inside local_function:", globals())


local_function()
print(global_var)