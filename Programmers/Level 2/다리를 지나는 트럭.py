def solution(bridge_length, weight, truck_weights):
    time = 0
    on_bridge = list()
    while True:
        time += 1

        on_truck_sum = 0
        del_list = list()
        for truck in range(len(on_bridge)):
            if on_bridge[truck][1] + 1 == bridge_length:
                del_list.append(truck)
            else:
                on_truck_sum += on_bridge[truck][0]
                on_bridge[truck][1] += 1

        del_list.sort()
        del_list.reverse()
        print(del_list)
        for i in del_list:
            del on_bridge[i]

        if len(truck_weights) > 0:
            if truck_weights[0] + on_truck_sum <= weight:
                tmp_list = list()
                tmp_list.append(truck_weights[0])
                tmp_list.append(0)
                on_bridge.append(tmp_list)
                del truck_weights[0]

        if len(truck_weights) == 0 and len(on_bridge) == 0:
            break
    answer = time
    return answer


print(solution(2, 10, [7, 4, 5, 6]))
