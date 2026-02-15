def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    

print_kwargs(name = "surajit", power = "lazer")
print_kwargs(name = "surajit")
print_kwargs(name = "surajit", power = "lazer", enemy = "Dr. J")