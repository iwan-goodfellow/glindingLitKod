# Jadi kita disuru nyari berapa kali dia mecahin records terendah sama tertingginya kek gt
# misal input = 3 4 21 36 10 28 35 5 24 42 -> nah outnya berarti = 4 0

def breakingRecords(scores):
    min_score = max_score = scores[0]
    count_min_score = count_max_score = 0

    for score in scores[1:]: # jangan lupa kita mulai dari index kedua, karena yg 1 tadi uda diinitialize
        if score < min_score:
            min_score = score
            count_min_score+=1
        elif score > max_score:
            max_score = score
            count_max_score+=1
    return count_max_score, count_min_score
