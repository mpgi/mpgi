
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

    def __init__(self, id, code):
        """
	Args:
		param1 (int) : The slot id.
		param2 (code) : MPI C code in this slot.

        """
        self.id = id
        self.code = code

class Process:

    def __init__(self, id):
        """
		param1(int) : The process id.
        """
        self.id = id
        self.slots = []

    def addSlot(self, slot):
        """
		param1(Slot) : The slots to add to this process.
        """
        self.slots.append(slot)

