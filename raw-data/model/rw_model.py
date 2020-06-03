#!/usr/bin/env python
import json
import os
import os.path as path
import datetime

def gen_frame(record, id_frame):
    current_time = datetime.datetime.now()

    frame = {
            'id': id_frame,
            'date': current_time.strftime("%m/%d/%Y, %H:%M:%S"),
            'record': record,
            'values': {
                    'world_population': record[0],
                    'year_births': record[1],
                    'today_births': record[2],
                    'year_deaths': record[3],
                    'today_deaths': record[4]
                }
        }

    return frame


def read_json(file_path):
    if (not does_exists(file_path)) or is_empty(file_path):
        return []

    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def does_exists(file_path):
    return path.exists(file_path)

def is_empty(file_path):
    return os.stat(file_path).st_size == 0


def append_json(file_path, record):
    content = read_json(file_path)

    id_frame = len(content)
    frame = gen_frame(record, id_frame)
    content.append(frame)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(content, f, indent=4)
