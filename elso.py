import random
import json


def legyenonismilliomos(question):
    temp_out = ''
    temp_out += f"{question.get('question','Nincs kerdes').capitalize()}\n"

    # print([question.get('answer','Nincs valasz')]+question.get('bad_answer','Nincs valasz'))

    shuffled_answers = [question.get('answer','Nincs valasz')]+question.get('bad_answer','Nincs valasz')

    random.shuffle(shuffled_answers)

    # print(shuffled_answers)
    # print(zip(shuffled_answers,['A','B','C','D']))
    # print(list(zip(shuffled_answers,['A','B','C','D'])))

    zipped_answer = [(answer,key) for answer,key in zip(shuffled_answers,['A','B','C','D'])]

    print(zipped_answer)

    good_answer = ''

    for ans in zipped_answer:
        temp_out += f"{ans[1]}: {ans[0]}\n"
        # print(f"{ans[1]}: {ans[0]}\n")
        # print("{ans[1]}: {ans[0]}\n")
        if ans[0] == question.get('answer','Nincs valasz'):
            good_answer = ans[1]



    print(temp_out)

    answer = input()

    if answer == good_answer:
        print("Jo valasz!")
    else: print("Rossz valasz!")

def behely(question):
    print(question.get('question','error'))
    answer = input()
    if answer == question.get('answer','error'):
        print("Jo valasz!")
    else: print("Rossz valasz!")

KERDESEK = json.load(open('kerdes_bank.json')).get('kerdesek')

n = random.randint(0,len(KERDESEK)-1)

question = KERDESEK[n]

if question.get('tipus') == 'abcd':
    legyenonismilliomos(question)
elif question.get('tipus') == 'bhely':
    behely(question)


