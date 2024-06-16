import os

def generate_hierarchy_with_py_files(folder_path, indent=0):
    with open("zzz_py_folders_and_files_hierarchy.txt", "ab") as file:
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path):
                file.write(f"{'  ' * indent}[Folder] {item}\n".encode('utf-8'))
                generate_hierarchy_with_py_files(item_path, indent + 1)
            else:
                file.write(f"{'  ' * indent}[File] {item}\n".encode('utf-8'))

# Replace 'your_folder_path' with the path of the folder you want to analyze
generate_hierarchy_with_py_files('Rana Universe Folder Name')
