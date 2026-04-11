def copy_file(command: str) -> None:
    try:
        cmd, source, destination = command.split()
    except ValueError:
        return

    if cmd != "cp":
        return

    if source == destination:
        return

    try:
        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
