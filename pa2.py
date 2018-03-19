'''
Automata Project 2 NFA sim
A simple python program to emulate a NFA based on the given input file
Matthew Roth: Mroth@sandiego.edu
Jack Miller: Jackmiller@sandiego.edu
3-16-2018
'''
import sys

#Our function that scans the input string and emulates the DFA symbol by symbol
def runMachine(dfa, start, accept, string):
    state = str(start)
    for symbol in string:
        try:
            state = dfa[state][symbol]
        except:
            print("Could not find key: ", symbol, " in state: ", state)
    return str(state)

#Declaring our dfa representation
dfa_dic = {}
#Opening the input
input = tuple(open(sys.argv[1], "r"))
#Pulling the number of states
num_states = int(input[0])
#Pulling and cleaning our alphabet
alphabet = input[1].strip()
#Getting the number of transitions in our DFA
num_transitions = num_states*len(alphabet)
#Creating an iterable so we can skip the first two lines
iterinput = iter(input)
next(iterinput)
next(iterinput)
#Count is used to stop taking in the transitions when we reach the start and accept states
count = 0
for line in iterinput:
    if(count < num_transitions):
        count+=1
        #Splitting the transition
        curState,symbol,nextState = line.split()
        #Cleaning our strings
        curState = curState.replace('\'', '')
        symbol = symbol.replace('\'', '')
        nextState = nextState.replace('\'', '')
        #Adding the transition to our 2d dictionary
        dfa_dic[curState] = dfa_dic.get(curState, {})
        dfa_dic[curState][symbol] = nextState
        continue
    else:
        #Setting the start state
        start_state = int(line)
        break
#Grabbing the accept states
accept_states = next(iterinput)
#Iterating through the strings
for string in iterinput:
    #Cleaning the input string
    string = string.strip()
    #Running our machine
    ans = runMachine(dfa_dic, start_state, accept_states, string)
    if ans in accept_states:
        print("Accept")
    else:
        print("Reject")
