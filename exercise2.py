#実行例) python exercise2.py 10000

import random
import time
import sys
# 0から1億までのランダムな整数要素を持つ100万個の要素を持つリストを生成
million_list = [random.randint(0, 100000000) for _ in range(1000000)]
print(f"リスト要素数：{len(million_list)}")
million_set = {random.randint(0, 100000000) for _ in range(1000000)}
while len(million_set) < 1000000:
    million_set.add(random.randint(0, 100000000))
print(f"セット要素数：{len(million_set)}")
# チェックするリストを生成
print("チェックリストの要素数を入力してください(半角数字)",end="")
check_list_num = int(sys.argv[1])
check_list = [random.randint(0, 100000000) for _ in range(check_list_num)]
# リストチェック
print("---------------List_Check---------------")
print(f"チェック要素数：1")
start_time = time.time()
if check_list[0] in million_list:
    print(f"重複数 : 「{check_list[0]}」")
end_time = time.time()
elapsed_time_list = end_time - start_time
print(f"リストチェック時間 : {elapsed_time_list}秒")
print("---------------Set_Check---------------")
print(f"チェック要素数：{len(check_list)}")
start_time = time.time()
for check_list_num in check_list:
    if check_list_num in million_set:
        print(f"重複数 : 「{check_list_num}」")
end_time = time.time()
elapsed_time_set = end_time - start_time
print(f"セットチェック時間 : {elapsed_time_set}秒")
print("---------------------------------------")
if elapsed_time_set < elapsed_time_list:
    result = elapsed_time_list - elapsed_time_set
elif elapsed_time_list < elapsed_time_set:
    result = elapsed_time_set - elapsed_time_list
print(f"時間差 : {round(result, 5)}")