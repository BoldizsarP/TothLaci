import datetime
def printer(*args,**kwargs):
    with open('stdout.txt', 'a') as f:
        f.write(f'{args},{kwargs}\n')

    print(f'{args},{kwargs}')

printer('asdasd','basd',printer='csigusz')
printer({1:'salala', printer:datetime.datetime.now()})