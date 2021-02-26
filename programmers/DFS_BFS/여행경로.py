def solution(tickets):
    answer = []
    tickets.sort(reverse=True)
    routes = dict()

    for t1, t2 in tickets:
        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]
    print(routes)
    print("")
    state = ["ICN"]
    while state:
        top = state[-1]
        if top not in routes or len(routes[top])==0:
            answer.append(state.pop())
        else:
            state.append(routes[top].pop())

    answer.reverse()


    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))