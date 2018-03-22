'''
Automata Project 2 NFA sim
A simple python program to emulate a NFA based on the given input file
Matthew Roth: Mroth@sandiego.edu
Jack Miller: Jackmiller@sandiego.edu
3-16-2018
'''
import sys

class DFA:
	#Initialize function
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.current_state = start_state
        self.start_state = start_state
        self.accept_states = accept_states
        return

    def printDFA(self):
        output = open(sys.argv[2], "w")
        output.write(str(self.states) + "\n")
        output.write(str(self.alphabet) + "\n")
        for i in range(1, self.states):
            for x in range(0, len(self.alphabet)):
                # TODO
                curState = self.states
                symbol = self.alphabet[x]
                nextState = self.transition_function.get(str(i), {}).get(str(x), {})
                s = str(curState) + " \'" + str(symbol) + "\' " + str(nextState) + "\n"
                # print(s)
                # s = str(dfa.states[i]) + ' \'' + str(dfa.alphabet[x]) + '\' ' + str(dfa.transition_function[dfa.states[i]][x]) + "\n
                output.write(s)
    # writing the start state

    for l in range(0, len(self.start_state)):
        output.write(str(self.start_state[l]))
    output.write("\n")
    # output.write(str(self.start_state)+"\n")
    # writing all of the accept states to a single line
    # for j in self.accept_states:
    for j in range(0, len(self.accept_states)):
        output.write(self.accept_states[j])
    output.write("\n")


def runMachine(self, string):
    state = str(self.start_state)
    for symbol in string:
        try:
            state = self.transition_function([self.current_state, symbol])
        except:
            print("Could not find key: ", symbol, " in state: ", state)
    return str(state)


class NFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.current_state = start_state
        self.accept_states = accept_states
        return

    def getnextState(self, i, x):
        return self.transition_function[i][x]

    def convertToDFA(self):
        dfadict = {}
        reject_flag = False
        # numstates = len(self.states)*len(self.alphabet)
        for i in range(1, self.states):
            for x in self.alphabet:
                temp = self.transition_function.get(str(i), {}).get(str(x), {})
                if type(temp) is dict:
                    reject_flag = True
                    dfadict[i] = dfadict.get(i, {})
                    dfadict[i][x] = "reject"
                else:
                    dfadict[i] = dfadict.get(i, {})
                    # temp = self.transition_function[i][x]
                    dfadict[i][x] = temp

        if reject_flag:
            states = self.states + 1
        else:
            states = self.states
        alphabet = self.alphabet
        start_state = self.start_state
        accept_states = self.accept_states
        return DFA(states, alphabet, dfadict, start_state, accept_states)



#Transitions to state with input
def parseInput():
    # Declaring our dfa representation
    dfa_dic = {}
    nfa_dic = {}
    # Opening the input
    input = tuple(open(sys.argv[1], "r"))
    # Pulling the number of states
    num_states = int(input[0])
    # Pulling and cleaning our alphabet
    alphabet = input[1].strip()
    # Getting the number of transitions in our DFA
    # num_transitions = num_states*len(alphabet)
    # Creating an iterable so we can skip the first two lines
    iterinput = iter(input)
    next(iterinput)
    next(iterinput)

    states = range(1, num_states)
    num_transitions = len(alphabet) * num_states
    end_trans = False
    start_flag = False
    start_state = 0
    accept_states = 0
    for line in iterinput:
        if not line.strip():
            end_trans = True
        if not end_trans and not start_flag:
            curState, symbol, nextState = line.split()
            curState = curState.replace('\'', '')
            symbol = symbol.replace('\'', '')
            #nextState = nextState('\'', '')
			if nfa_dic[curState][symbol] is not None:
				 = nfa_dic.get(curState, {}).get(symbol, {})
				if temp is List:
					nfa_dic[curState

            nfa_dic[curState] = nfa_dic.get(curState, {})
            nfa_dic[curState][symbol] = nextState

        elif end_trans and not start_flag:
            start_flag = True
            start_state = line
            print("START STATE IN parse: type = ", str(type(start_state)), "contents = ", start_state)
            #start_state = start_state.replace('\'', '')
        elif end_trans and start_flag:
            accept_states = line.split()
            #accept_states = accept_states.replace('\'', '')
    return NFA(num_states, alphabet, nfa_dic, start_state, accept_states)


def main():
    if sys.argv is None:
        print("Usage: \n$> python pa2.py <input> <output> ")
    else:
        a = parseInput()
        print("NFAdict: \n", a.transition_function)
        b = a.convertToDFA()
        print("DFAdict: \n", b.transition_function)
        b.printDFA()


if __name__ == "__main__":
    sys.exit(main())



'''
TO BE USED maybe:

#Our function that scans the input string and emulates the DFA symbol by symbol
def runMachine(dfa, start, accept, string):
    state = str(start)
    for symbol in string:
        try:
            state = dfa[state][symbol]
        except:
            print("Could not find key: ", symbol, " in state: ", state)
    return str(state)
	def transition_to_state_with_input(self, input_value):
		if ((self.current_state, input_value) not in self.transition_function.keys()):
			self.current_state = None
			return
		self.current_state = self.transition_function[(self.current_state, input_value)]
		return

#Determines whether or not in accept state
def in_accept_state(self):
    return self.current_state in self.accept_states
#Brings back to the initial state
def go_to_initial_state(self):
    self.current_state = self.start_state
    return
#Runs the machine with given input list
def run_with_input_list(self):
    self.go_to_initial_state()
    for inp in input_list:
        self.transition_to_state_with_input(inp)
        continue
    return self.in_accept_state()

