a = 10
b = 12

print('a berisi angka',a ,'desimal atau',bin(a),'biner')
print('b berisi angka',b ,'desimal atau',bin(b),'biner')

print('\n')

# operator AND (&) a x b
c = a & b
print(f'a & b  : {bin(c)} atau {c}')

# operator OR (|) a + b - (a x b)
c = a | b
print(f'a | b  : {bin(c)} atau {c}')

# operator XOR (^) (a + b) % 2
c = a ^ b
print(f'a ^ b  : {bin(c)} atau {c}')

# operator NOT (~) (a + 1)x -1
print('~a     :',bin(~a))

# operator Shift Left (<<)
print('a << 1 :',a << 1)

# operator Shift Right (>>)
print('a >> 1 :',a >> 1)