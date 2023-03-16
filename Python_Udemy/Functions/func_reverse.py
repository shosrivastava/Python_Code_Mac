def rev(text):
    return text[: : -1]

text = input("Enter a text to print it in reverse:\n").strip()

print(rev(text))