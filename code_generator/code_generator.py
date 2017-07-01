
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
import json
from components import Slot
from components import Process

class CodeGenerator:

	def __init__(self, InputFile, OutputFile):
		"""
		IutputFile(filename) : input file.
		OutputFile(filename) : output file.
		"""
		self.inputFile = InputFile
		self.outputFile = OutputFile

	def generate(self):
		"""
		*** WARNING *** hard coded
		"""

		outputStream = open(self.outputFile, 'w')

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

		outputStream.write(MPIstart)
		 
		for i in range(0,3):
			outputStream.write('''	if(rank==''')
			outputStream.write(str(0))
			outputStream.write(''')
	{
''')
			outputStream.write('''		''')
			outputStream.write(p0.slots[i].code)
			outputStream.write('''	}
''')

			outputStream.write('''	else if(rank==''')
			outputStream.write(str(1))
			outputStream.write(''')
	{
''')
			outputStream.write('''		''')
			outputStream.write(p1.slots[i].code)
			outputStream.write('''	}

''')

		with open(self.inputFile) as data_file:
			data = json.load(data_file)

		num_process = data["num_process"]

		for timeslot in data["timeslots"]:
			for block in timeslot["blocks"]:
				for code in block["code"]:
					print(code)
			
		MPIend = '''
  MPI_Finalize();
}
'''
		outputStream.write(MPIend)
		outputStream.close()


gen = CodeGenerator("tutorial.json", "object_code.c")
gen.generate()

