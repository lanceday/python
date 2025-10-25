def read_file_to_string():
    file_path = "your_filename_here.txt"  # Insert your filename here
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found"
    except Exception as e:
        return f"Error: {str(e)}"

# Execute the read_file_to_string function and print the result
content = read_file_to_string()
print(content)
