import os

# Path to the *original* monolithic script whose functions you want to extract
original_file_path = os.path.join(os.path.dirname(__file__), "medigate final (3).py")

# Create a directory to store the separated files
separated_files_dir = os.path.join(os.path.dirname(__file__), "separated_functions")
os.makedirs(separated_files_dir, exist_ok=True)

# Read the updated original file
with open(original_file_path, "r") as updated_file:
    updated_code = updated_file.readlines()

# Variables to track function extraction
functions = {{}}
current_function = []
inside_function = False
function_name = ""

# Extract each function into a separate file
for line in updated_code:
    if line.strip().startswith("def "):
        if inside_function:  # Save the previous function
            functions[function_name] = current_function
        # Start a new function
        function_name = line.split("def ")[1].split("(")[0].strip()
        current_function = [line]
        inside_function = True
    elif inside_function:
        current_function.append(line)
        if line.strip() == "":  # Function ends when an empty line is encountered
            functions[function_name] = current_function
            inside_function = False

# Add any remaining function
if inside_function:
    functions[function_name] = current_function

# Write each function to its own file and replace it in the original code with an import statement
remaining_code = []
for function_name, function_code in functions.items():
    # Write the function to its own file
    function_file_path = os.path.join(separated_files_dir, f"{{function_name}}.py")
    with open(function_file_path, "w") as function_file:
        function_file.writelines(function_code)
    # Add import statement to the remaining code
    remaining_code.append(f"from separated_functions.{{function_name}} import {{function_name}}\n")

# Write the remaining non-function code back to the original file
with open(original_file_path, "w") as reduced_file:
    reduced_file.writelines(remaining_code)

print("Functions split successfully into:", separated_files_dir)
