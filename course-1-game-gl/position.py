def position(x, y):
    """ returns the given x, y co-ordinate as a string """
    return f'{x}:{y}'


def north(position):
    """ Moving north increases the y value by 1 """
    x, y = position.split(':')
    return f'{x}:{int(y) + 1}'


def south(position):
    """ Moving south decreases the y value by 1 """
    x, y = position.split(':')
    return f'{x}:{int(y) - 1}'


def east(position):
    """ Moving east increases the x value by 1 """
    x, y = position.split(':')
    return f'{int(x) + 1}:{y}'


def west(position):
    """ Moving west decreases the x value by 1 """
    x, y = position.split(':')
    return f'{int(x) - 1}:{y}'


def can_go(position, nodes):
    """ Given an initial position and an array of nodes,
        returns a humanised list of directions that you can
        travel in. """
    pos = decode(position)
    directions = []
    for node in nodes:
        x, y = decode(node)
        if pos[0] == x and pos[1] + 1 == y:
            directions.append("North")
        if pos[0] == x and pos[1] - 1 == y:
            directions.append("South")
        if pos[0] + 1 == x and pos[1] == y:
            directions.append("East")
        if pos[0] - 1 == x and pos[1] == y:
            directions.append("West")
    return directions


def decode(position):
    x, y = position.split(':')
    return [int(x), int(y)]
