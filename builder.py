from typing import Optional, Iterable, Dict, Callable, List

from functions import filter_query, unique_query, limit_query, map_query, sort_query, regex_query

CMD_TO_FUNCTIONS: Dict[str, Callable] = {
    'filter': filter_query,
    'unique': unique_query,
    'limit': limit_query,
    'map': map_query,
    'sort': sort_query,
    'regex': regex_query
}

def read_file(file: str) -> Iterable[str]:
    with open(file) as file:
        for line in file:
            yield line

def convert_query(cmd: str, value: str, file: str, data: Optional[Iterable[str]]) -> List[str]:
    if data is None:
        prepared_data: Iterable[str] = read_file(file)
    else:
        prepared_data = data

    return list(CMD_TO_FUNCTIONS[cmd](value=value, data=prepared_data))

