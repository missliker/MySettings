import os

def delete_exe_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".exe"):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")

# 执行删除操作
current_directory = os.getcwd()
delete_exe_files(current_directory)
