import sys
import os

import whs

def read(filename):
	with open(f'{filename}', 'r') as file:
		for n, line in enumerate(file, 1):
			line = line.rstrip('\n')
			try:
				whs.Core.run(line)
			except IndexError:
				print('Argument is not found')
args = sys.argv
if len(args) != 2:
	print('Usage: python start.py <filename>')
else:
	if not args[1].endswith('.whc'):
		args[1] += '.whc'
	if os.path.exists(args[1]):
		read(args[1])
	else:
		print(f'The {args[1]} file does not exist')
