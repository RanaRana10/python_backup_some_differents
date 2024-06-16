import os

def generate_hierarchy_with_py_files(folder_path='.', indent=0):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            print(f"{'  ' * indent}[Folder] {item}")
            generate_hierarchy_with_py_files(item_path, indent + 1)
        else:
            print(f"{'  ' * indent}[File] {item}")

# Replace 'Rana Universe Folder Name' with the path of the folder you want to analyze
generate_hierarchy_with_py_files()
