def solution(bridge_length, weight, truck_weights):
    answer = 0 # 걸리는 시간
    bridge = [] # 다리
    count = 0 # 지나간 트럭의 수
    n = len(truck_weights) # 지나가야할 트럭의 수
    del_list = []
    while(count < n): # 모든 트럭이 다 지나갈 때까지
        for i in range(len(bridge)):
            bridge[i][1] += 1 # 다리에 있는 트럭에 대해 이동거리를 1씩 더해준다
            if(bridge[i][1] == bridge_length): # 다리 길이와 이동거리가 같아지면
                del_list.append(i) 
                count += 1
        for i in range(len(del_list)):
            del bridge[del_list[i]] # 다리 탈출
        del_list = []

        if(len(truck_weights) > 0):
            temp = truck_weights[0] 
            bridge_sum = 0 # 현재 다리위에 있는 트럭의 무게 합
            for i in range(len(bridge)):
                bridge_sum += bridge[i][0]
            if(temp + bridge_sum <= weight): # 트럭이 들어갈 수 있으면
                bridge.append([temp, 0]) # [트럭무게, 이동거리]
                del truck_weights[0] # 대기 리스트에서 삭제
        # print(bridge)
        answer += 1 # 1초 지나감

    return answer

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length, weight, truck_weights))