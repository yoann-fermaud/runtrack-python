# --| 1 |-- #
def developer(language: str):
    match language:
        case 'javascript':
            return 'You are a web developer'
        case 'python':
            return 'You are an AI developer'
        case 'java':
            return 'You are an engineer software'
        case 'reactjs':
            return 'You are a mobile developer'
        case _:
            return 'One day, I will be the best developer...'


print(f'\nFirst method :')          # 'You are a web developer'
print(developer('javascript'))      # 'You are an AI developer'
print(developer('python'))          # 'You are an engineer software'
print(developer('java'))            # 'You are a mobile developer'
print(developer('reactjs'))         # 'You are a mobile developer'
print(developer('I don\'t know'))   # 'One day, I will be the best developer...'


# --| 2 |-- #
def developer_if(language_if: str):
    if language_if == 'javascript':
        return 'You are a web developer'
    elif language_if == 'python':
        return 'You are an AI developer'
    elif language_if == 'java':
        return 'You are an engineer software'
    elif language_if == 'reactjs':
        return 'You are a mobile developer'
    else:
        return 'One day, I will be the best developer...'


print(f'\nSecond method :')            # 'You are a web developer'
print(developer_if('javascript'))      # 'You are an AI developer'
print(developer_if('python'))          # 'You are an engineer software'
print(developer_if('java'))            # 'You are a mobile developer'
print(developer_if('reactjs'))         # 'You are a mobile developer'
print(developer_if('I don\'t know'))   # 'One day, I will be the best developer...'
