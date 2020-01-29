films = {
    'Finding Dory':[5,3],
    'Jason Bourne': [18,17],
    'Tarzan': [1,0],
    'Ghost Busters':[12,13]
    }

while True:
    choice = input('What movie do you want to watch?: ').strip().title()

    if choice in films:
        age = int(input('How old are you?: ').strip())

#check user age

        if age >= films[choice][1]:

            #check enough seats
            
            if films[choice][0] > 0:
                print('Enjoy the film!')
                films[choice][0] = films[choice][0]-1
            else:
                print('Sorry we are sold out')
        else:
            print('You are too young to see that film')
    else:
        print ('We do not have that film...')
