import random
import re
from replies import eightball_replies

random.seed(1234)

QUESTION_REGEX = re.compile(r'.+\?')


def get_reply(message):
    message_text = message.text

    if QUESTION_REGEX.match(message_text):
        return eightball_reply(message)
    else:
        return 'I\'m not sure what to say.'
    pass


def eightball_reply(message):
    random_index = random.randint(0, len(eightball_replies) - 1)
    reply = eightball_replies[random_index]

    return reply
