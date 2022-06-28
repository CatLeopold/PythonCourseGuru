while True:
    action_request = input('Enter command "read" or ""copy":')
    if action_request == "read":
        file_path = input("Write the path to the file whose contents you want to view:")
        handler = open(file_path, 'r')
        print(handler.read())
        handler.close()
    elif action_request == "copy":
        file_path = input("Write the path to the file you want to copy:")
    else:
        print("Unknown command!")
