# Side Effect exercise from shorts          / global /

emoticon = "^.^"

def main():
    global emoticon
    say("Is anyone there? ")
    emoticon = ":D"
    say("Oh, hi!")

def say(phrase):

    print(phrase + " " + emoticon)
    
main()