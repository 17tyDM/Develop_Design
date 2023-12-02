from itertools import tee

my_list = [1, 2, 3, 4, 5]

# イテレータの作成
my_iterator = iter(my_list)

# 一番目の要素を取得
print(next(my_iterator))  # 1

# イテレータを複製する
iter1, iter2 = tee(my_iterator)

# 同じ要素を二回連続して取得する
print(next(iter1))  # 2
print(next(iter2))  # 2