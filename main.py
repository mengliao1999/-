# 项目名称: python案例
# 编写时间: 2022/10/3
# 编写人员: 孟利奥
import os
import re
import shutil
import send2trash


def move_to_trash_if_contains_bracket_number(path):
    # 正则表达式匹配包含括号数字的文件或文件夹名
    pattern = re.compile(r'\(\d+\)')

    # 遍历文件夹及其子文件夹
    for root, dirs, files in os.walk(path, topdown=False):
        # 遍历文件
        for name in files:
            if pattern.search(name):
                file_path = os.path.join(root, name)
                print(f'Moving file to trash: {file_path}')
                send2trash.send2trash(file_path)

        # 遍历文件夹
        for name in dirs:
            if pattern.search(name):
                dir_path = os.path.join(root, name)
                print(f'Moving directory to trash: {dir_path}')
                send2trash.send2trash(dir_path)


# 替换为你想要遍历的文件夹路径
folder_path = "C:\\Users\MENGLIAO\Desktop\试验"
move_to_trash_if_contains_bracket_number(folder_path)
