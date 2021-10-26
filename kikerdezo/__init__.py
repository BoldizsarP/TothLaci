import random
import re
from time import sleep
db = {
    'kerdesek':['a','b']
}
threads = {}

db.get('kerdesek')

method_extractor = re.compile(r'!kvizkerdesek[\s\t]+(abcd|bhely)')

finish_extractor = re.compile(r'!kvizkerdesek[\s\t]+(stop|vege)')

abcd_response_matcher = re.compile(r'([a-dA-D])^[\w\d].*')

abcd_question_matcher = re.compile(r'a, ([\d\w\s]*)\nb, ([\d\w\s]*)\nc, ([\d\w\s]*)\nd, ([\d\w\s]*)\n')

def kvizkerdeskezelo(message):
    if message.author.id in threads:
        if finish_extractor.match(message.content):
            threads.pop(message.author.id)
            return message.reply('Kikerdezo is finished!')
        
        if message.reference and message.reference.cached_message:
            cached_message = message.reference.cached_message
            if cached_message.split('\n')[0].lower() in [q['question'] for q in db['kerdesek']]:
                q_set = db['kerdesek'][[q['question'] for q in db['kerdesek']].index(cached_message.split('\n')[0].lower())]
                if q_set['tipus'] == threads[message.author.id]['tipus']:
                    if q_set['tipus'] == 'abcd':
                        answers = abcd_question_matcher.match(cached_message.split('\n')[1])
                        if not answers:
                            reply(message,'Gecc nem tudom elolvasni a sajat irasom!')
                            sleep(2)
                            reply(message,f'A helyes valasz {answers["answer"]}')
                        else:
                            answer = abcd_response_matcher.match((message.content.lower()))
                            good_answer = ['abcd'[k] for k in range(4) if answers[k+1]==q_set['answer']][0]
                            if answer == good_answer:
                                reply(message, f"That's right, the good answer is {good_answer.toupper()}, {q_set['answer']}")
                                sleep(2)
                            else:
                                reply(message, f"Na ah, the good answer is {good_answer.toupper()}, {q_set['answer']}")
                            
                            if threads[message.author.id]['kerdesek']:
                                next_kerdes = threads[message.author.id]['kerdesek'].pop()
                                reply(message,'Akkor johet a kovetkezo kerdes!')
                                sleep(1)

                                reply(message,legyenonismilliomos(next_kerdes))
                            
                            


async def reply(message, reply):
    return await message.reply(reply)


async def answer(message):
    pass

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
        temp_out += f"{ans[1]}, {ans[0]}\n"
    return temp_out
