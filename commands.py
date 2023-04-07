def commands(file, cmd, val):
    res = None

    if cmd == 'filter':
        res = list(filter(lambda v: val in v, file))

    if cmd == 'map':
        res = '\n'.join([i.split()[int(val)] for i in file])

    if cmd == 'unique':
        res = list(sorted(set(file)))

    if cmd == 'sort':
        is_rev = False

        if val == 'desc': is_rev = True

        res = sorted(file, reverse=is_rev)

    if cmd == 'limit':
        res = list(file)[:int(val)]

    return res
