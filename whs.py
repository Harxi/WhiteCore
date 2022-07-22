#WhiteCore 0.0.4 by Harxi
#Email: sup.harxi@gmail.com

import lexer

import js2py

class Data():
	variables = []
	cache = {}
	libName = []
	libImp = []
	libFunc = []
	libLang = None

class Tokens():
	RESERVED = 'RESERVED'
	INT = 'INT'
	ID = 'ID'
	ARG = 'ARG'
	
	
	TokenSplits = [
		(r'[ \n\t]+', None),
		(r'#[^\n]*',  None),
		(r'[0-9]+', INT),
		(r'[A-Za-z][A-Za-z0-9_]*', ID),
		(r'[А-Яа-я][А-Яа-я0-9_]*', ID),
		(r'.',  RESERVED),
	]
	@staticmethod
	def imp(characters):
		return lexer.lex(characters, Tokens.TokenSplits)

class Basic():
	__version__ = '0.0.4'
	Data = Data()
	Tokens = Tokens()

class Core():
	@staticmethod
	def run(cmd):
		token = Tokens.imp(cmd)
		
		if token == []:
			pass
			
		elif token[0][0] == 'use':
			with open(f'{token[1][0]}.{token[3][0]}', 'r') as file:
				for n, line in enumerate(file, 1):
					if token[3][0] == 'js':
						spl = ('//', '#')
					elif token[3][0] == 'py':
						spl = ('#', '/')
						
					if n == 1:
						version = line.replace(spl[0], '')
						version = version.split(' ')[1]
						if version != Basic.__version__:
							print('Impossible to interpret the file, it uses an outdated core')
							exit()
						else:
							continue
					if n == 2:
						libname = line.replace(spl[0], '')
						libname = libname.split(' ')[0]
						Data.libName += [libname]
					if n == 3:
						libimp = line.replace(spl[0], '')
						libimp = libimp.split(spl[1])
						
						Data.libImp += [libimp]
						libimp = libimp.pop(len(libimp)-1)
					if n == 4:
						libfunc = line.replace(spl[0], '')
						libfunc = libfunc.split(spl[1])
						Data.libFunc += [libfunc]
						libfunc = libfunc.pop(len(libfunc)-1)
						break
					else:
						pass
						
		else:
			lib = []
			
			for libs in Data.libName:
				if libs.split('.')[1] == 'js':
					lib.append([None, libs])
				elif libs.split('.')[1] == 'py':
					lib.append([__import__(libs.split('.')[0]), libs])
			
			for index, keyword in enumerate(Data.libImp):
				for ptdindex, method in enumerate(keyword):
					if token[0][0] == method:
						if lib[index][1].split('.')[1] == 'js':
							ctx = js2py.EvalJs()

							with open(f'{lib[index][1]}', 'r') as f:
								ctx.execute(f.read())
							exec(f'ctx.{Data.libFunc[index][ptdindex]}')
						elif lib[index][1].split('.')[1] == 'py':
							exec(f'lib[index][0].{Data.libFunc[index][ptdindex]}')
