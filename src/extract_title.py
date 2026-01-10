def extract_title(markdown):
    lines = markdown.split("\n\n")
    for line in lines:
        if line.startswith("# "):
            if line[-1] == "\n":
                return line[2:-1]
            else:
                return line[2:]
    raise Exception("No title found (h1)")