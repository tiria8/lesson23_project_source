import re
from typing import Iterable, Iterator, Any, Set, List


def filter_query(value: str, data: Iterable[str]) -> Iterator[str]:
    return filter(lambda x: value in x, data)

def unique_query(data: Iterable[str], *args: Any, **kwargs: Any) -> Set[str]:
    return set(data)

def limit_query(value: str, data: Iterable[str]) -> List[str]:
    limit: int = int(value)
    return list(data)[:limit]

def map_query(value: str, data: Iterable[str]) -> Iterator[str]:
    column_number = int(value)
    return map(lambda x: x.split(' ')[column_number], data)

def sort_query(value: str, data: Iterable[str]) -> List[str]:
    reverse = value == 'desc'
    return sorted(data, reverse=reverse)

def regex_query(value: str, data: Iterable[str]) -> Iterator[str]:
    regex = re.compile(value)
    return filter(lambda x: re.search(regex, x), data)