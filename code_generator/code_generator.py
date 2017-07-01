
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
from components import Slot
from components import Process
import json

class codeGenerator:

    def __init__(self, process1, process2, OutputFile):
        """
		param1(Process) : The process included in object code.
		param2(process) : The process included in object code.
		OutputFile(File stream) : output file.
        """
        self.proc0 = process1
        self.proc1 = process2
        self.f = OutputFile

    def generate(self):
        """
	    *** WARNING *** hard coded
        """
        for i in range(0,3):
            self.f.write('''	if(rank==''')
            self.f.write(str(0))
            self.f.write(''')
	{
''')
            self.f.write('''		''')
            self.f.write(self.proc0.slots[i].code)
            self.f.write('''	}
''')

            self.f.write('''	else if(rank==''')
            self.f.write(str(1))
            self.f.write(''')
	{
''')
            self.f.write('''		''')
            self.f.write(self.proc1.slots[i].code)
            self.f.write('''	}

''')

f = open('object_code.c', 'w')

MPIstart = '''/* program skeleton*/

#include "mpi.h"
#include <stdio.h>
#include <stdlib.h>

void main(int argc, char * argv[])
{
	int rank, size;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_rank(MPI_COMM_WORLD, &size);
	
'''

s00 = Slot(0, '''Process 0, slot0
''')

s01 = Slot(0, '''Process 0, slot1
''')

s02 = Slot(0, '''Process 0, slot2
''')

s10 = Slot(1, '''Process 1, slot0
''')

s11 = Slot(1, '''Process 1, slot1
''')

s12 = Slot(1, '''Process 1, slot2
''')

p0 = Process(0)
p0.addSlot(s00)
p0.addSlot(s01)
p0.addSlot(s02)

p1 = Process(0)
p1.addSlot(s10)
p1.addSlot(s11)
p1.addSlot(s12)

MPIend = '''
	MPI_Finalize();
}
'''

f.write(MPIstart)
gen = codeGenerator(p0, p1, f)
gen.generate()

f.write(MPIend)
f.close()
