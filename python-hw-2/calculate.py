import sys

# print(len(sys.argv))
if len(sys.argv) !=4:
    print ('max arg len is 4')
    sys.exit()

j=sys.argv[1]

left_operand = sys.argv[1]
rigth_operand = sys.argv[3]

operation = sys.argv[2]

allower_operations =['+','-','*','/']

if operation !='+' and operation !='-':
    print('operation is not allowed')
    sys.exit()
try:
    left_operand=int(left_operand)
    rigth_operand=int(rigth_operand)
except ValueError:
    print('')

#print (eval(f'{left_operand}{operation}{rigth_operand}'))

print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])


print(sys.argv)