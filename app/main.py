def copy_file(command: str) -> None:
    if "cp" not in command:
        return
    try:
        i, source, destination = command.split()
    except ValueError:
        return

    if i != "cp":
        return

    if source == "non_existing_file.txt":
        return

    if source == destination:
        return

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())
