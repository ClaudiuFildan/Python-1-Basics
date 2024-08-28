#two.py

import one

print("TOP LEVELIN TWO.PY")

one.func()

if __name__=='__main__':
	print('ONE.PY is being run direclty!')
else:
	print('ONE.PY has been imported!')

