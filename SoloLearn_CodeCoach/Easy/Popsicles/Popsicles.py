print(
    'give away'
    if (foo := (int(input()), int(input())))[1] % foo[0] == 0
    else
    'eat them yourself'
)
