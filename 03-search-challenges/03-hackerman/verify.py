import re, os, sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def hackfile(path) : 
    return os.path.dirname(os.path.abspath(__file__)) + "/" + path

messages =  [
    ["Great, you managed to find  my notes",
    "I need you to access my computer, but I forgot my password",
    "It's a English word followed by a number with multiple digits",
    "I can look through the book, but I need you to give me the regex to find it",
    "A regex is a vital skill for h4X00rz, it allows you to find stuff fast",
    "",
    "But you don't know what it is yet.",
    "I'd explain it, but the cops are banging on my door",
    "goto https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html",
    "",
    "just put your regex in the (now empty) solution.txt and run this script again"],
    ["TERMINAL UNLOCKED",
        "I'm looking for my ssh key",
        ":>_",
        ":>_ ls -a",
        "!!!!INSUFFICIENT PERMISSIONS!!!!!",
        "Shoot, we can't look at the files directly, they have the system locked down",
        "I need my encrypted container.",
        "I forgot the name though, can you write a regex to find it?",
        "A filename has the format \"name\" + \".\" + \"extension\"",
        "The filename is exactly 7 vowels in a row",
        "The dot is.. well... a dot. Or a period, if you want to be precise",
        "The extension I dont' remember exactly. It's either \"foo\" or \"bar\". Or maybe \"baz\"",
        "Good luck!"
    ]  
]

content_files = ["alice.txt", "filenames.txt"]

fail_messages = [ 
    [
        "We couldn't find a password using your regex",
        "Please try again :)"
    ],
    [
        "No, that doesn't seem to find the correct file",
        "Try again"
    ]
]

success_messages = [
    [
        "You're in. Congrats agent you did it!"
    ],
    [
        "That's it! I'll upload my documents to you tomorrow. But for now, you're done here"
    ]
]


solution_checks = [664, 1076]
    
    
solution_file = open(hackfile("solution.txt"), "r")
raw_solutions = solution_file.readlines()
solution_file.close()

if len(raw_solutions) == 0:
    print("\n" + bcolors.FAIL + "Something went wrong matching your solutions from \"{0}\"".format(raw_solutions)) 
    
    
for index in range(0,2):
        
    text_file = open(hackfile(content_files[index]), "r")
    data = text_file.read()
    text_file.close()

    for m in messages[index]:
        print(bcolors.HEADER + m)

    if len(raw_solutions) == index:
        sys.exit(1)
    solution = raw_solutions[index]
    print("trying " + bcolors.WARNING + solution)
    try:
        if solution[0] != '(':
            solution = "(" + solution + ")"
        solution_re = re.compile(solution)
        answer = solution_re.search(data)
        if answer is None:
            for m in fail_messages[index]:
                print(m)
            sys.exit(1)
    except Exception as ex:
        print("\n" + bcolors.FAIL + "Something went wrong matching your solution \"{0}\"".format(solution.replace('\n', '')))
        print("details " + str(ex))
        print('\nPlease try again :)')
        sys.exit(1)
        
    sum = 0
    for i in answer.group(1).replace('\n', ''):
        sum  = sum + ord(i)
        
    if (sum == solution_checks[index]):
        for m in success_messages[index]:
            print(bcolors.OKGREEN + m)
    else:
        print(bcolors.FAIL +  "Something went wrong matching your solution \"{0}\"".format(solution.replace('\n', '')))
        
        for m in fail_messages[index]:
            print(bcolors.OKGREEN + m)
        sys.exit(1)
    
sys.exit(0)