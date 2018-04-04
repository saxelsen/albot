import random
import re
from replies import eightball_replies
import json
import time

# random.seed(1234)

QUESTION_REGEX = re.compile(r'.+\?')

with open('random_quotes.json', 'r') as random_quotes_file:
    random_quotes = json.load(random_quotes_file)
    random_quotes = [quote['quote'] for quote in random_quotes]


def get_reply(message):
    message_text = message.text

    # Add delay to simulate bot typing
    time.sleep(0.5)

    if QUESTION_REGEX.match(message_text):
        return eightball_reply(message)
    else:
        return random_quote(message)
    pass


def eightball_reply(message):
    random_index = random.randint(0, len(eightball_replies) - 1)
    reply = eightball_replies[random_index]

    return reply


def random_quote(message):
    random_index = random.randint(0, len(random_quotes) - 1)
    reply = random_quotes[random_index]

    return reply
