# python3


class Query:

    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    phone_book = dict()
    result = []
    for query in queries:
        if query.type == 'add':
            phone_book[query.number] = query.name
        elif query.type == 'del':
            phone_book.pop(query.number, None)
        else:
            result.append(phone_book.get(query.number, 'not found'))
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

