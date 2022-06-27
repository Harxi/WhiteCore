#WhiteCore 0.0.3 by Harxi
#Email: sup.harxi@gmail.com

import lexer

class Data():
	variables = []
	cache = {}
	# FOR CORE DON'T EDIT #
	libName = []
	libImp = []
	libFunc = []
	# FOR CORE DON'T EDIT #

class Tokens():	
	
	# FOR CORE DON'T EDIT #
	RESERVED = 'RESERVED'
	INT = 'INT'
	ID = 'ID'
	ARG = 'ARG'
	# FOR CORE DON'T EDIT #
	
	TokenSplits = [
    (r'[ \n\t]+', None),
    (r'#[^\n]*',  None),
    (r'[0-9]+', INT),
    (r'[A-Za-z][A-Za-z0-9_]*', ID),
    (r'[А-Яа-я][А-Яа-я0-9_]*', ID),
	]

	def imp(characters):
	    return lexer.lex(characters, Tokens.TokenSplits)

class Basic():
	__version__ = '0.0.3'
	Data = Data()
	Tokens = Tokens()

class Core():
	# FOR CORE DON'T EDIT #
	def run(cmd):
		token = Tokens.imp(cmd)
		
		if token == []:
			pass
		
		elif token[0][0] == 'use':
			with open(f'{token[1][0]}.py', 'r') as file:
				for n, line in enumerate(file, 1):
					if n == 1:
						version = line.replace('#', '')
						version = version.split(' ')[1]
						if version != Basic.__version__:
							print('Impossible to interpret the file, it uses an outdated core')
							exit()
						else:
							continue
					if n == 2:
						libname = line.replace('#', '')
						libname = libname.split(' ')[0]
						Data.libName += [libname]
					if n == 3:
						libimp = line.replace('#', '')
						libimp = libimp.split('/')
						
						Data.libImp += [libimp]
						libimp = libimp.pop(len(libimp)-1)
					if n == 4:
						libfunc = line.replace('#', '')
						libfunc = libfunc.split('/')
						Data.libFunc += [libfunc]
						libfunc = libfunc.pop(len(libfunc)-1)
						break
					else:
						pass
						
		else:
			lib = []
			
			for libs in Data.libName:
				lib.append(__import__(libs))
				
			for index, keyword in enumerate(Data.libImp):
				for ptdindex, method in enumerate(keyword):
					if token[0][0] == method:
						exec(f'lib[index].{Data.libFunc[index][ptdindex]}')
						print(Basic.Tokens.TokenSplits)
	# FOR CORE DON'T EDIT #
