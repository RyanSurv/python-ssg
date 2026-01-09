def markdown_to_blocks(markdown):
    # Am I fuckin functional now or what???!
    return list(filter(lambda b: len(b) != 0, map(lambda b: b.strip(), markdown.split("\n\n"))))