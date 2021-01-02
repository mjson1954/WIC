#1. 주소의 복사 얕은 복사
old_list=[]
new_list=old_list

#2. 슬라이싱, 깊은 복
new_list=old_list[:]

#3. extend(): 리스트를 추가하는 함수, 깊은 복사
new_list=[]
new_list.extend(old_list)

#4. list(): 깊은 복사
new_list=list(old_list)

#5. copy 활용, 깊은 복사
import copy
new_list=copy.copy(old_list)

#6. 리스트함축, 깊은 복사
new_list=[i for i in old_list]

#7. 리스트 원소까지도 깊은 복사, 가장 느림, 깊은 복사
import copy
new_list=copy.deepcopy(old_list)
