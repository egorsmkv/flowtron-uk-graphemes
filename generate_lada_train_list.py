import json

ROWS_FILE = '/home/yehor/ML/flowtron/dataset_lada_trimmed/accept/metadata.jsonl'

with open(ROWS_FILE) as x:
    dataset = [json.loads(s) for s in x.readlines()]

with open('filelists/lada_ukrainian_train_filelist.txt', 'w') as x:
    for s in dataset:
        g = s['orig_text']

        print(s)
        path='/home/yehor/ML/flowtron/dataset_lada_trimmed/accept/' + s['file']

        line = f'{path}|{g}|0'
        x.write(line + '\n')
