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

class DFA:
	current_state = None;
	#Initialize function
	def __init__(self, states, alphabet, transition_function, start_state, accept_states):
		self.states = states;
		self.alphabet = alphabet;
		self.transition_function = transition_function;
		self.current_state = start_state;
		self.accept_states = accept_states;
		return;
	#Transitions to state with input
	def transition_to_state_with_input(self, input_value):
		if ((self.current_state, input_value) not in self.transition_function_keys()):
			self.current_state = None;
			return;
		self.current_state = self.transition_function[(self.current_state, input_value)];
		return;
	#Determines whether or not in accept state
	def in_accept_state(self):
		return self.current_state in accept_states;
	#Brings back to the initial state
	def go_to_initial_state(self):
		self.current_state = self.start_state;
		return;
	#Runs the machine with given input list
	def run_with_input_list(self):
		self.go_to_initial_state():
		for inp in input_list;
			self.transition_to_state_with_input(inp);
			continue;
		return self.in_accept_state();
	pass;

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


states = range(1, num_states);

d = DFA(states, alphabet, tf, cur_state, next_state);
inp_program = ('#needs to be a list of the inputs read in I assume');
d.run_with_inputs(inp_program);


