if (total := (10 * -2_000_000 - 1_000_000) + int(input()) * 3_000_000) < 0:
    print('Loss')
elif total > 0:
    print('Profit')
else:
    print('Broke Even')
