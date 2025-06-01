# -- Homework -- #

# function to shut down the system
def shutdown(user_input):
    if user_input.lower() == "yes":
        return "shutting down..."
    elif user_input.lower() == "no":
        return "abort shut down"
    else:
        return "sorry can't understand."

# asking:
print(shutdown(input("Do you want to shut down? (Yes/No): ")))