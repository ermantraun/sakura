from parse import parse
from renderer import renderer


def put_render(html, render, template_start, template_stop, bounds_len):
    return html[:template_start - bounds_len] + render + html[template_stop + bounds_len:]


def sakura(html: str, vars_) -> str:
    bounds = ['{%', '%}']
    bounds_len = len(bounds[0])
    parsed, template_start, template_stop = parse(html, bounds)
    render = renderer(parsed, vars_)
    result = put_render(html, render, template_start, template_stop, bounds_len)
    return result


if __name__ == '__main__':
    print(sakura(open('Test.html', 'r').read(), {'name': 'Igor', 'hobby': ['music', 'games', 'sport']}))
