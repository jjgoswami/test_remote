file_content=open('test_code.py', 'r')

line_content=file_content.readlines()
for line in line_content:
            print( line.strip())