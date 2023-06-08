#!/usr/bin/python3
for alphabet in range(ord('z'), ord('A') - 1, -1):
    print('{:c}'.format(alphabet), end='')
    if alphabet != ord('z'):
        alphabet -= 1
        print('{:c}'.format(alphabet), end='')
