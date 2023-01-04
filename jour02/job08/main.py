def type_season(type: str, season: str):
    if type == 'fruits' and season == 'winter':
        return 'Orange, tangerine and kiwi'
    elif type == 'fruits' and season == 'summer':
        return 'Pear, strawberry, blackcurrant'
    elif type == 'vegetables' and season == 'winter':
        return 'Carrot, Jerusalem artichoke, endive'
    elif type == 'vegetables' and season == 'summer':
        return 'Artichoke, eggplant, turnip'


print(type_season('fruits', 'winter'))
print(type_season('fruits', 'summer'))
print(type_season('vegetables', 'winter'))
print(type_season('vegetables', 'summer'))
