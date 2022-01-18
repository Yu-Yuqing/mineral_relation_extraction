import os
import re
import json
import random

random.seed(12345)

here = os.path.dirname(os.path.abspath(__file__))


def convert_data(line):
    head_name, no1, nu1, tail_name, no2, nu2, relation, text = re.split(r'\t', line)
    print()
    nu11 = int(nu1)+len(head_name)
    nu22 = int(nu2)+len(tail_name)
    head_pos = (int(nu1),nu11)
    tail_pos = (int(nu2),nu22)
    item = {
        'h': {
            'name': head_name,
            'pos': head_pos
        },
        't': {
            'name': tail_name,
            'pos': tail_pos
        },
        'relation': relation,
        'text': text
    }
    return item



def save_data(lines, file):
    print('保存文件：{}'.format(file))
    unknown_cnt = 0
    with open(file, 'w', encoding='utf-8') as f_out:
        for line in lines:
            item = convert_data(line)
            if item is None:
                continue
            json_str = json.dumps(item, ensure_ascii=False)
            f_out.write('{}\n'.format(json_str))
 


def split_data(file):
    file_dir = os.path.dirname(file)
    train_file = os.path.join(file_dir, 'train1.jsonl')
    val_file = os.path.join(file_dir, 'val1.jsonl')
    with open(file, 'r', encoding='utf-8') as f_in:
        lines = f_in.readlines()
    lines = [line.strip() for line in lines]
    random.shuffle(lines)
    lines_len = len(lines)
    train_lines = lines[:lines_len * 7 // 10]
    val_lines = lines[lines_len * 7 // 10:]
    save_data(train_lines, train_file)
    save_data(val_lines, val_file)


def main():
    all_data = os.path.join(here, 'copy.txt')
    split_data(all_data)


if __name__ == '__main__':
    main()
