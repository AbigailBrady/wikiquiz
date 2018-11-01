import random, sys, wikipedia
import re

def randomPage():
    try:
        while True:
            page = wikipedia.page(wikipedia.random())
            if gen_question(wikipedia.summary(page.title, sentences=1)):
                return page
    except wikipedia.exceptions.DisambiguationError as e:
        return randomPage()
       
def gen_question(summary):
    start = summary.find(" is ")

#    if start != -1:
#       start = summary.find(" was ")

    end = min(summary.find(".", start), summary.find(",", start))
    
    if start == -1:
        return None
    else:
        return "What/Who " + summary[start+1:end] + "?"
       

options = ["A", "B", "C", "D"]


# print(pages[0].summary)

score = 0
attempts = 0

while True:

    pages = [randomPage() for _ in range(4)]
    whichPage = random.randint(0, len(options) - 1)

    print("\033c")

    print(f"WIKIPEDIA QUIZ THINGY!!!!!!!!!  SCORE: {score} OUT OF {attempts}")
    print()
    print()
    print()
    print()
    print(gen_question(wikipedia.summary(pages[whichPage].title, sentences=1)))
    print()
    print()

    for option, page in zip(options, pages):
        print(f"   {option} - {page.title}")

    print()
    print("  which article? type ", " ".join(options))
        
    sys.stdout.flush()
      
    input = sys.stdin.readline().rstrip()
    while input.upper() not in options:
        print("   not a valid option, try again.")
        sys.stdout.flush()
        input = sys.stdin.readline().rstrip()

    if input.upper() == options[whichPage].upper():
       print("CORRECT!")
       score += 1
    else:
       print("INCORRECT!")
       
    sys.stdout.flush()

    attempts += 1
