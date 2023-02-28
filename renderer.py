from functions import functions
from Exceptions import NotFoundVar


def get_argument_value(vars_, argument):
    value = vars_.get(argument)
    if value is None:
        raise NotFoundVar('Var "{}" is not found'.format(argument))
    else:
        return value


def renderer(parsed, vars_):
    render = ''
    for operator in parsed['functions']:
        name = operator[0]
        args = [get_argument_value(vars_, arg) for arg in operator[1]]
        render += functions[name](*args)
    for cycle in parsed['cycles']:
        start, stop, step = map(int, cycle[1][1:])
        cycle_var = cycle[1][0]
        for cycle_var_value in range(start, stop, step):
            vars_[cycle_var] = cycle_var_value
            render += renderer(cycle[2], vars_)
    return render