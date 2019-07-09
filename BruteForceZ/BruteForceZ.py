"""Brute Force zip file password cracker"""
import zipfile

def extractFile(target, passWord):
	try:
		target.extractall(pwd = passWord )
		return passWord
	except:
		return
		
		
def main(zFile, dFile):
	target = zipfile.ZipFile(zFile) 
	dictFile = open(dFile)
	
	for line in dictFile.readlines():
		passWord = line.strip('\n')
		guess = extractFile(target, passWord)
		
		if guess:
			print 'Password = ' +passWord+ '\n'
			exit(0)
		else:
			print passWord


if __name__=='__main__':
	zFile = raw_input("Enter file name>> ")
	dFile = raw_input("Enter dictionary name>> ")
	main(zFile, dFile)
	
