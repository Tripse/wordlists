import re

# 输入和输出文件路径
input_file = "/Users/leadlife/wordlists/endpoints/intersting.txt"  # 替换为你的输入文件路径
output_file = "output.txt"  # 替换为你的输出文件路径

# 打开输入文件，逐行处理
with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        # 去掉每行开头的 "/"
        cleaned_line = re.sub(r"^/", "", line)
        outfile.write(cleaned_line)  # 写入到输出文件
