import os
import random
import shutil


def update_labels(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    updated_lines = []
    for line in lines:
        image_name, label = line.strip().split()
        updated_label = str(int(label) - 1)
        updated_lines.append(f"{image_name} {updated_label}\n")

    with open(file_path, 'w') as file:
        file.writelines(updated_lines)


def prepare_label(file_paths):
    for file_path in file_paths:
        update_labels(file_path)


def create_test_subset(file_path, test_max_num, output_directory):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    test_subset = random.sample(lines, min(test_max_num, len(lines)))

    # 获取文件名和扩展名
    file_name, file_extension = os.path.splitext(os.path.basename(file_path))

    # 构建新文件路径
    output_file_path = os.path.join(output_directory, f'{file_name}{file_extension}')

    with open(output_file_path, 'w') as test_file:
        test_file.writelines(test_subset)


def prepare_test_anno(file_paths, output_directory, test_max_num=50):
    # 创建存放测试文件的目录
    os.makedirs(output_directory, exist_ok=True)

    for processed_file_path in file_paths:
        create_test_subset(processed_file_path, test_max_num, output_directory)


def prepare():
    # 请替换以下文件路径为你实际的文件路径
    file_paths = ['ct_train.txt', 'ct_val.txt', 'ct_test.txt']
    prepare_label(file_paths)
    # 请替换以下目录为你希望保存测试文件的目录
    output_directory = '../test_anno'
    prepare_test_anno(file_paths, output_directory=output_directory)


if __name__ == '__main__':
    prepare()
