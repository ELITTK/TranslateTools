import os
import re


def process_files(directory, file_extension, pattern):
    # 遍历指定目录中的所有文件
    for filename in os.listdir(directory):
        if filename.endswith(file_extension):
            # 打开文件并读取内容
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                content = file.read()
                # print(content)

            # 使用正则表达式进行匹配
            matches = re.findall(pattern, content)

            # 将匹配结果写入到同名的txt文件中
            output_filename = os.path.splitext(filename)[0] + '.txt'
            with open(os.path.join(directory, output_filename), 'w', encoding='utf-8') as output_file:
                for match in matches:
                    output_file.write(match + '\n')


def writeback_files(directory, file_extension, pattern):
    for filename in os.listdir(directory):
        if filename.endswith(file_extension):
            translatedfilename = re.sub(r"\.ks", ".txt", filename)
            print(translatedfilename)
            with open(os.path.join(directory, translatedfilename), 'r', encoding='utf-8') as file:
                translated_lines = file.readlines()
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                content = file.readlines()

            translated_lines_index = 0
            for i in range(len(content)):
                if re.search(pattern, content[i]) is not None:
                    content[i] = re.sub(pattern, translated_lines[translated_lines_index], content[i])
                    translated_lines_index += 1

            with open(os.path.join(directory, filename), 'w', encoding='utf-8') as file:
                file.writelines(content)


# 示例用法
directory = 'D:/Code/Python/ksTextExtractor/ksFiles'  # 替换为你的目录路径
file_extension = '.ks'  # 替换为你的文件后缀名
pattern = r'.+\[p]'  # 替换为你的正则表达式模式

# process_files(directory, file_extension, pattern)
writeback_files(directory, file_extension, pattern)