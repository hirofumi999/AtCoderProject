T = int(input())
for i in range(T):
    a, s = map(int, input().split())
    s -= 2 * a  # and はxもyも1で、それ以外の桁は多くても片側だけ1
    if s >= 0 and s & a == 0:  # sとaで共通のフラグは立ってはいけない
        print('Yes')
    else:
        print('No')