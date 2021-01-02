def solution(genres, plays):
    answer = []
    album = {}
    genre_sum = {}
    for i in range(len(genres)):
        keys = list(album.keys())
        if(not(genres[i] in keys)):
            album[genres[i]] = [plays[i]]
            genre_sum[genres[i]] = plays[i]
        else:
            album[genres[i]].append(plays[i])
            genre_sum[genres[i]] += plays[i]

    genre_sum = sorted(genre_sum.items(), reverse=True, key=lambda item: item[1])
    #print(genre_sum)

    keys = list(album.keys())
    for i in range(len(keys)):
        album[keys[i]] = sorted(album[keys[i]], reverse=True)
    #print(album)

    for i in range(2):
        genre = genre_sum[i][0]
        temp = album[genre]
        idx0 = plays.index(temp[0])
        idx1 = plays.index(temp[1])
        if(temp[0] == temp[1]):
            if(idx0 < idx1):
                answer.append(idx0)
                answer.append(idx1)
            else:
                answer.append(idx1)
                answer.append(idx0)
            continue
        if(len(temp) > 1):
            answer.append(idx0)
            answer.append(idx1)
        else:
            answer.append(idx0)


    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))