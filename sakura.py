from parsing import parse


def sakura(html: str, vars_) -> str:
    parsed = parse(html)
    return parsed


if __name__ == '__main__':
    print(sakura(open('Test.html', 'r').read(), {'name': 'Igor', 'hobby': ['music', 'games', 'sport']}))
