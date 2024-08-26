user_input = input("Please provide alpha numberic input: ")
print(f"The input is {'not numeric' if user_input.isalpha() else 'numeric'}")