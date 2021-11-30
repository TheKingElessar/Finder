from pathlib import Path

input_file = Path("found.txt")
sorted_list = []
with input_file.open("r") as f:
    for line in f:
        sorted_list.append(line)

sorted_list = list(dict.fromkeys(sorted_list))
output_file = Path("sorted.txt")
with output_file.open("a") as f:
    for line in sorted(sorted_list):
        f.write(line)
