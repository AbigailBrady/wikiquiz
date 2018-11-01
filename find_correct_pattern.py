import re

import wikipedia


def find_question_body(title):
    summary = wikipedia.summary(title, sentences=1)
    m = re.match(f"{title}.*?(?:is|was) a (.*$)", summary)
    if m:
        return m.groups()[0]
    else:
        return False


"""
If it can find
find_question_body('Albert Einstein')
--> 'German-born theoretical physicist who developed the theory of relativity, one of the two pillars of modern physics (alongside quantum mechanics).'

If cannot match
find_question_body('Albert Einstein')
--> False

"""
