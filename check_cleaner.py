import json
from text import cleaners

ROWS_FILE = '/home/yehor/ML/flowtron/dataset_lada_trimmed/accept/metadata.jsonl'

with open(ROWS_FILE) as x:
    dataset = [json.loads(s) for s in x.readlines()]

for s in dataset:
    text = s['orig_text']
    text = cleaners.flowtron_cleaners(text)

    print(s['orig_text'])
    print(text)
    print()
