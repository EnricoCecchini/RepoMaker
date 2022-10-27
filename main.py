# Import libraries
import os
import se

user = ''
password = ''
projectPath = ''

def getUserData():
    if not os.path.exists('config.ini'):
        user = input('Github Email: ')
        password = input('Password: ')
        projectPath = input('Projects Path to create new Repos: ')
        with open('config.ini', 'w') as f:
            f.write(f'{user}\n')
            f.write(f'{password}\n')
            f.write(f'{projectPath}\n')
    else:
        with open('config.ini', 'r') as f:
            user = f.readline().replace('\n', '')
            password = f.readline().replace('\n', '')
            projectPath = f.readline().replace('\n', '')

    return user, password, projectPath

user, password, projectPath = getUserData()