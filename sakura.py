from dataclasses import dataclass


class UnknownOperator(Exception):
    pass


class NotFoundBoundary(Exception):
    pass


class NotFoundBodyBoundary(Exception):
    pass


class NotFoundHeadBoundary(Exception):
    pass


class NotFoundOperatorBoundary(Exception):
    pass


@dataclass(frozen=True)
class Operator:
    name: str


@dataclass(frozen=True)
class SingleOperator(Operator):
    pass


@dataclass(frozen=True)
class CompoundOperator(Operator):
    condition: str
    start_block_symbol: str = '{'
    end_block_symbol: str = '}'


def delete_all_spaces(symbols: str) -> str:
    return ''.join(symbols.split())


def get_index_start_end_block(string: str, start_block: str, end_block: str) -> list[int, int]:
    index_block_start = string.find(start_block) + len(start_block)
    index_block_end = string.find(end_block)
    return index_block_start, index_block_end


def get_grammar():
    grammar = {'single_operators': {'add': SingleOperator('add')},
               'compound_operators': {'for': CompoundOperator('for', '(var[in]IterableObject)')}}

    return grammar


def parse_operator_body(block, body_start):
    pointer = body_start
    body = ''
    body_end = -1
    while pointer < len(block):
        symbol = block[pointer]
        if symbol == '}':
            body_end = pointer
        body += symbol
        pointer += 1
    if body_end == -1:
        raise NotFoundBodyBoundary('End of body not found, maybe you forgot to add "}"')
    grammar = get_grammar()
    body = block[body_start:body_end]
    return pointer, parse_block_body(body, grammar)


def parse_operator_head(block, head_start):
    head = ''
    pointer = head_start
    while pointer < len(block):
        symbol = block[pointer]
        if symbol == ')':
            break
        head += symbol
        pointer += 1
    else:
        raise NotFoundHeadBoundary('End of head not found, maybe you forgot to add ")"')
    return pointer, head.split(',')


def parse_operator(block: list, start_index, compound_operators):
    pointer = start_index
    operator = []
    category = 'single_operators'
    name = ''
    while pointer < len(block):
        symbol = block[pointer]
        if symbol == '\\':
            break
        name += symbol
        pointer += 1
    else:
        raise NotFoundOperatorBoundary('End of operator not found, maybe you forgot to add ">"')
    operator.append(name)
    pointer, head = parse_operator_head(block, pointer + 2)
    operator.append(head)
    if name in compound_operators:
        pointer, body = parse_operator_body(block, pointer + 2)
        category = 'compound_operators'
        operator.append(body)
    return [operator, category, pointer]


def parse_block_body(block: list, grammar: dict) -> dict[str, list]:
    analyzed_block_body: dict[str, list] = {'single_operators': [], 'compound_operators': []}
    single_operators, compound_operators = grammar['single_operators'], grammar['compound_operators']
    pointer = 0
    while pointer < len(block):
        symbol = block[pointer]
        if symbol == '/':
            parsed_operator, category, operator_end_index = parse_operator(block, pointer + 1, compound_operators)
            analyzed_block_body[category].append(parsed_operator)
            pointer = operator_end_index
        else:
            pointer += 1
    return analyzed_block_body


def sakura(html: str, vars_) -> str:
    print(vars_)
    grammar = get_grammar()
    html = delete_all_spaces(html)
    template_start_index, template_stop_index = get_index_start_end_block(html, 'sakura_start{%', '%}sakura_end')
    template_body = html[template_start_index:template_stop_index]
    analyzed_template_body = parse_block_body(list(template_body), grammar)
    return analyzed_template_body


if __name__ == '__main__':
    print(sakura(open('Test.html', 'r').read(), {'name': 'Igor', 'hobby': ['music', 'games', 'sport']}))
