#!/usr/bin/env python3
# 棍子游戏，
# 用户先选1-4根子，然后电脑选1-4根棍子；
# 谁选到最后一根棍子谁就输
# ------------特别说明：用户和电脑一次选的棍子总数只能是5-----------------
# 由于21/5=4...1，用户先手，
# 所以最后一定是用户选最后一根棍子，用户没有机会赢！
sticks = 21

print('There are 21 sticks, you can take 1-4 number of sticks at a time.')
print('Whoever will take the last stick will loose')

while True:
    print('Sticks left: ',sticks)
    if sticks == 1 :
        print('You took the last stick,you loose')
        break
    sticks_taken=int(input('Take sticks(1-4):'))
    if sticks_taken >=5 or sticks_taken <=0:
        print('Wrong choice')
        continue
    print('Computer took: ',(5-sticks_taken),'\n')
    sticks -=5
