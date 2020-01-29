#list of known users
known_users=['Alice', 'Bob','Claire', 'Dan', 'Emma', 'Fred', 'Georgie', 'Harry']

while True:
    print('Hi. My name is Travis')
    name = input('What is your name?: ').strip().capitalize()

    if name in known_users:
        print('Hello ' + name + '!')
        remove = input('Would you like to be removed from the system (y/n)?: ').lower().strip()
        if remove == 'y' or remove == 'yes':
            known_users.remove(name)
        elif remove == 'n' or remove == 'no':
            print('No problem. I did not want you to leave anyways')

    else: 
        print('I dont think I have met you yet {}'.format(name))
        add_me = input('Would you like to be added to the system (y/n)?: ').strip().lower()
        if add_me == 'y'or add_me == 'yes':
            known_users.append(name)
        elif add_me == 'n' or add_me == 'no':
            print('Oh, okay. It was a pleasure! Bye-bye')
            
