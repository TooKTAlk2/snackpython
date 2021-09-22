import pyperclip

curr_value = ""
filename = "something"
count = 0
while True:
    copied_value = pyperclip.paste()
    if curr_value != copied_value:
        curr_value = copied_value

        if count != 0:
            with open(f"{filename}_{count}.ipynb", "w", encoding="utf-8") as f:
                f.write(curr_value)

        count += 1
