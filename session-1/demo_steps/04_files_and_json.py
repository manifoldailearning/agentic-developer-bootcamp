import json
from pathlib import Path
from functions_and_flow import parse_line, normalise_priority

# __file__ is the current file path
print("__file__:")
print(__file__)
print(type(__file__))
print("--------------------------------")

# create file path
file_path = Path(__file__)
print("file_path:")
print(file_path)
print(type(file_path))
print("--------------------------------")

# get parent directory
parent_dir = file_path.parent
print("parent_dir:")
print(parent_dir)
print(type(parent_dir))
print("--------------------------------")

file_name = "support-ticket-v1.txt"
full_file_name = parent_dir / file_name
print("full_file_name:")
print(full_file_name)
print(type(full_file_name))
# Read the file
output = full_file_name.read_text(encoding="utf-8")
print("output:")
print(output)
print(type(output))
print("--------------------------------")

# get grandparent directory
root = Path(__file__).resolve().parents[1]
print("grand parent directory:")
print(root)
print(type(root))
print("--------------------------------")
input_path = root / "data" / "support-ticket.txt"
output_path = root / "output" / "step-04-ticket.json"

text = input_path.read_text(encoding="utf-8")
# \n is a newline character
split_lines = text.split("\n")
print("split_lines:")
print(split_lines)
print(type(split_lines))
print("--------------------------------")

# Assigment:
# Use the parse_line function to parse the lines by iterating over the split_lines
# Hint: Use for loop and the parse_line function

output_dict = {}
for line in split_lines:
    k,v = parse_line(line)
    output_dict[k] = v
    print(f"k: {k}, v: {v}")

print(output_dict)
print("--------------------------------")
#normalise the priority
output_dict["priority"] = normalise_priority(output_dict["priority"])
print(output_dict)
print("--------------------------------")

# Fix the tags
output_dict["tags"] = output_dict["tags"].split(",")
print(output_dict)
print("--------------------------------")

json_output = json.dumps(output_dict, indent=2)
print(json_output)
print(type(json_output))
print("--------------------------------")

output_path.parent.mkdir(parents=True, exist_ok=True) # create the output directory if it doesn't exist
output_path.write_text(json_output, encoding="utf-8") # write the json output to the file
print(f"Created: {output_path}")
