***

                              ***
							  
							  
## PE Analysis with pefile

import pefile

pe = pefile.PE('c:\\windows\\notepad.exe')

pe

dir(pe)

import pprint

pprint.pprint(dir(pe))

pe.DOS_HEADER

pprint.pprint(dir(pe.DOS_HEADER))

pe.DOS_HEADER.e_magic

hex(pe.DOS_HEADER.e_magic)

hex(pe.DOS_HEADER.e_lfanew)

pprint.pprint(dir(pe.FILE_HEADER))

pe.FILE_HEADER.NumberOfSections

pe.sections

pprint.pprint(dir(pe.sections))


for section in pe.sections
    print section.name
	print section.SizeOfRawData
	print '\n'
	

pe.dump_info()

pprint.pprint(dir(pe.dump_info))

