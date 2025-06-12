
def remove_dot_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f_in, \
         open(output_file, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            if '.' not in line:
                f_out.write(line)

# 使用示例
if __name__ == "__main__":
    input_path = 'input.txt'    # 原始文件
    output_path = 'output.txt'  # 处理后的文件
    remove_dot_lines(input_path, output_path)
