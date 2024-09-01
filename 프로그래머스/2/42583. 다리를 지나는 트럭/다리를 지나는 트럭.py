from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)  # 다리 위에 올라간 트럭들의 상태를 나타내는 큐
    total_weight_on_bridge = 0  # 현재 다리 위에 있는 트럭들의 무게
    time = 0  # 경과 시간

    for truck in truck_weights:
        while True:
            # 한 칸 전진, 다리 위에 있는 트럭들이 움직임
            time += 1
            total_weight_on_bridge -= bridge.popleft()
            
            # 다음 트럭이 다리에 올라갈 수 있는지 확인
            if total_weight_on_bridge + truck <= weight:
                bridge.append(truck)
                total_weight_on_bridge += truck
                break
            else:
                bridge.append(0)  # 트럭을 올리지 못하면 다리에서 0을 추가하여 공간 확보
    
    # 마지막 트럭이 다리를 완전히 건너기까지 걸리는 시간 추가
    time += bridge_length
    
    return time
