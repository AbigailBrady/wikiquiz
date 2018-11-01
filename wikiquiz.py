import random, sys, wikipedia

def randomPage():
    try:
        page = wikipedia.page(wikipedia.random())
        page.summary
        return page
    except:
        return randomPage()
       
def obfuscate(r):
    return r
       

options = ["A", "B", "C", "D"]


# print(pages[0].summary)

score = 0
attempts = 0

while True:

    pages = [randomPage() for _ in range(4)]
    whichPage = random.randint(0, len(options) - 1)

    print("\f")

    print(f"WIKIPEDIA QUIZ THINGY!!!!!!!!!  SCORE: {score} OUT OF {attempts}")
    print()
    print()
    print("  this is the start of a Wikipedia article.  your task is to identify which one.")
    print()
    print()
    print(obfuscate(pages[whichPage].summary))
    print()
    print()

    for option, page in zip(options, pages):
        print(f"   {option} - {page.title}")

    print()
    print("  which article? type ", " ".join(options))
        
    sys.stdout.flush()
      
    input = sys.stdin.readline().rstrip()
    while input not in options:
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
