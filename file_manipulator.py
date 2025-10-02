import sys

command = sys.argv[1]
lenArgv = len(sys.argv)
content = ''


def isTxt(filename):
    fileExtension = filename[-4:]
    if fileExtension == ".txt":
        return True
    else:
        return False


if command == 'reverse':
    print('reverse') 
    if lenArgv == 4:
        if isTxt(sys.argv[2]) and isTxt(sys.argv[3]):
            with open(sys.argv[2]) as fInput:
                content = fInput.read()
                reversedContent = ''
                for char in content:
                    reversedContent = char + reversedContent

            with open(sys.argv[3], 'w') as fOutput:
                fOutput.write(reversedContent)
        else:
          print('Please ensure that the specified file is in text format.')  
    else:
        print('There is an error in your input.')

            
elif command == 'copy':
    print('copy')
    if lenArgv == 4:
        if isTxt(sys.argv[2]) and isTxt(sys.argv[3]):
            with open(sys.argv[2]) as fInput:
                content = fInput.read()
            
            with open(sys.argv[3], 'w') as fOutput:
                fOutput.write(content)
        else:
          print('Please ensure that the specified file is in text format.')  
    else:
        print('There is an error in your input.')


elif command == 'duplicate-contents':
    print('duplicate-contents')
    if lenArgv == 4:
        if isTxt(sys.argv[2]):
            with open(sys.argv[2], 'r') as f:
                content = f.read()
                print(content)
                for i in range(int(sys.argv[3])-1):
                    content += content
                    print(content)

            with open(sys.argv[2], 'w') as f:
                f.write(content)
        else:
          print('Please ensure that the specified file is in text format.')          
    else:
        print('There is an error in your input.')


elif command == 'replace-string':
    print('replace-string')
    if lenArgv == 5:
        if isTxt(sys.argv[2]):
            with open(sys.argv[2], 'r') as f:
                content = f.read()
                content = content.replace(sys.argv[3], sys.argv[4])

            with open(sys.argv[2], 'w') as f:
                f.write(content)
        else:
          print('Please ensure that the specified file is in text format.')  
    else:
        print('There is an error in your input.')


else:
    print('There is an error in your input.')



