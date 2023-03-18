from typing import Optional, Iterable

from functions import filter_query, unique_query, limit_query, map_query, sort_query

CMD_TO_FUNCTIONS = {
    'filter': filter_query,
    'unique': unique_query,
    'limit': limit_query,
    'map': map_query,
    'sort': sort_query
}

def read_file(file):
    with open(file) as file:
        for line in file:
            yield line

def convert_query(cmd, value, file, data: Optional[Iterable[str]]):
    if data is None:
        prepared_data = read_file(file)
    else:
        prepared_data = data

    return list(CMD_TO_FUNCTIONS[cmd](value=value, data=prepared_data))

