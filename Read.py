file = open('SampleFile.txt', 'r')
content = file.read()
file.close()
print(f"Content of 'SampleFile.txt': {content}")