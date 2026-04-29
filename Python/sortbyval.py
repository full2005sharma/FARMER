def sort_by_value(d: dict) -> list:
    return sorted(d.items(), key=lambda x: -x[1])
print(sort_by_value({'a':2,'b':6}))