command = input("> ")
is_start = False

while command.lower() != "quit":
    if command == "help":
        print("""
start - to start the car")
stop - to stop the car
quit - to exit
        """)
    elif command == "start":
        if is_start:
            print("The car is already started!")
        else:
            print("Car started...Ready to go!")
            is_start = True
    elif command == "stop":
        if not is_start:
            print("The car is already stopped!")
        else:
            print("Car stopped.")
            is_start = False
    else:
        print("I don't understand that...")
    command = input("> ")
    command.lower()

