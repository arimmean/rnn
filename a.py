import difflib

file1 = "/Users/amitin/Desktop/DL1/intro-to-dl-hse/homeworks-small/shw-03-rnn/dataset.py"
file2 = "/Users/amitin/Desktop/HW3/DL-1/SHW/RNN/dataset.py"

with open(file1) as f1, open(file2) as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

differ = difflib.HtmlDiff()
html_diff = differ.make_file(lines1, lines2, file1, file2)

with open("diff.html", "w") as output_file:
    output_file.write(html_diff)

print("Diff saved to diff.html")
