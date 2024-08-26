# Print variable value:
proj_name = 'Python Demo'
print(f"Project name: {proj_name}")

# Casting types:
def castingdemo():
    # int parse
    val = int(1.3)
    print(f"Parsed integer value: {val}. The type of value in {type(val)}")
    # string parse
    val = str(1)
    print(f"Parsed string value: {val}. The type of value in {type(val)}")
    # float parse
    val = float(1)
    print(f"Parsed float value: {val}. The type of value in {type(val)}")
    # Boolean parse
    val = bool("test")
    print(f"Parsed bool value: {val}. The type of value in {type(val)}")

castingdemo()

#Get input from user:
input_val = input("Enter input:")
print(f"The entered input is: {input_val}")

