print(
    ' '.join(
        {'Grr': 'Lion', 'Rawr': 'Tiger', 'Ssss': 'Snake', 'Chirp': 'Bird'}[noise]
        for noise in input().split()
    )
)
