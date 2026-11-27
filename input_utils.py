
def get_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print("Please enter a valid number.")
