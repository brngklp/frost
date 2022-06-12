def defaultFile(filename:str) -> None:
    defaultString = "[\n]"
    with open(filename, 'w') as f:
        f.write(defaultString)
