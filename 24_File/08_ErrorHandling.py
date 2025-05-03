import os


def file_Handling():
     try:
        # Check if file exists before reading
        if not os.path.exists('important.txt'):
            raise FileNotFoundError("File not found")
            
        # Check permissions
        if not os.access('important.txt', os.R_OK):
            raise PermissionError("No read permission")
            
        # Open with proper error handling
        with open('important.txt', 'r') as file:
            content = file.read()
            print(content)
            
     except FileNotFoundError as e:
        print(f"Error: {e}. Please check the file path.")
     except PermissionError as e:
        print(f"Error: {e}. Check file permissions.")
     except IOError as e:
        print(f"I/O Error: {e}")
     except Exception as e:
        print(f"Unexpected error: {e}")
     finally:
        print("File operation attempt completed.")