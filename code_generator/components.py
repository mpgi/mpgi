
'''
MPGI Code Generator version 0.01
code writer : Wonpyo Jang
last modified : Jan. 31, 2017  

code history : 


In this simple code,
we purpose to generate mpi code.

Finally application user don't need to consider mpi grammmer.
Therefore, they only consider each process's code at certain time.

T
'''

class Slot:

    def __init__(self, number, code):
        """
	Args:
		param1 (int) : The slot id.
		param2 (code) : MPI C code in this slot.

        """
        self.num = number
        self.code = code

class Process:

    def __init__(self, number):
        """
		param1(int) : The process id.
        """
        self.num = number
        self.slots = []

    def addSlot(self, slot):
        """
		param1(Slot) : The slots to add to this process.
        """
        self.slots.append(slot)

