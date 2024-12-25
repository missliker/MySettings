import os
import re


def replace_colons_in_file(file_path): 
    """将文件中的中文冒号替换为英文冒号"""
    with open(file_path, 'r', encoding='utf-8') as f: 
        content = f.read()

    # 替换中文冒号为英文冒号
    updated_content = re.sub(': ', ':  ', content)

    if content != updated_content: 
        with open(file_path, 'w', encoding='utf-8') as f: 
            f.write(updated_content)
        print(f"已修改文件:  {file_path}")


def process_directory(directory): 
    """递归遍历目录并处理文件"""
    for root, _, files in os.walk(directory): 
        for file in files: 
            file_path = os.path.join(root, file)
            try: 
                replace_colons_in_file(file_path)
            except Exception as e: 
                print(f"处理文件时出错:  {file_path}, 错误:  {e}")


if __name__ == "__main__": 
    current_directory = os.getcwd()
    print(f"开始处理路径:  {current_directory}")
    process_directory(current_directory)
    print("处理完成")
