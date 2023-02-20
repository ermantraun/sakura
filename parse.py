from Exceptions import (NotFoundNameBoundary, NotFoundHeadBoundary, UnknownName,
                        NotFoundBodyBoundary)
from operators import operators


def delete_all_spaces(symbols: str) -> str:
    return ''.join(symbols.split())


def get_index_start_end_block(string: str, start_block: str, end_block: str) -> list[int, int]:
    index_block_start = string.find(start_block) + len(start_block)
    index_block_end = string.find(end_block)
    return index_block_start, index_block_end


def parse_cycles_body(block, body_start):
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
    body = block[body_start:body_end]
    return pointer, parse_block_body(body)


def parse_expression_head(block, head_start):
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


def parse_expression(block, start_index):
    pointer = start_index
    expression = []
    category = 'functions'
    name = ''
    while pointer < len(block):
        symbol = block[pointer]
        if symbol == ';':
            break
        name += symbol
        pointer += 1
    else:
        raise NotFoundNameBoundary('End of expression not found, maybe you forgot to add "\\"')
    expression.append(name)
    pointer, head = parse_expression_head(block, pointer + 2)
    expression.append(head)
    if name not in operators:
        if name != 'for':
            raise UnknownName('An unknown operator or cycle is found')
        pointer, body = parse_cycles_body(block, pointer + 2)
        category = 'cycles'
        expression.append(body)
    return [expression, category, pointer]


def parse_block_body(block) -> dict[str, list]:
    analyzed_block_body: dict[str, list] = {'functions': [], 'cycles': []}
    pointer = 0
    while pointer < len(block):
        symbol = block[pointer]
        if symbol == ';':
            parsed_operator, category, operator_end_index = parse_expression(block, pointer + 1)
            analyzed_block_body[category].append(parsed_operator)
            pointer = operator_end_index
        else:
            pointer += 1
    return analyzed_block_body


def parse(html: str, bounds) -> str:
    template_start_index, template_stop_index = get_index_start_end_block(html, bounds[0], bounds[1])
    template_body = html[template_start_index:template_stop_index]
    template_body = delete_all_spaces(template_body)
    analyzed_template_body = parse_block_body(template_body)
    return analyzed_template_body, template_start_index, template_stop_index