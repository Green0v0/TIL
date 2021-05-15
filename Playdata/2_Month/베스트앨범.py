# from collections import Counter
def psolution(genres, plays):
    # 장르별 총 재생횟수가 높은 장르
    # 장르내 재생횟수가 높은 순 (재생횟수가 같을 시 번호가 우선)

    # 노래들을 큰 순서대로 정렬 (장르 상관 x)
    idx = list(range(len(genres)))
    songs = sorted(list(zip(genres, plays, idx)), key=lambda x: x[1], reverse=True)

    new_songs = {}
    for i, j, idx in songs:
        new_songs[i] = new_songs.get(i,0) + j

    # 장르들의 총합 중 누가 더 큰지 파악
    sort_genres = sorted(new_songs, key=lambda x: x[1], reverse=True)

    result = []
    cnt = 2
    for g in sort_genres:
        for x, y, idx in songs:
            if x == g:
                result.append(idx)
            if len(result) == cnt:
                break
        cnt += 2 # 아 1개일 경우에는 그릏네... 각각 높은 애들을 리스트로 받아서 합쳐야 겠다!
    # print(result)
def ppsolution(genres, plays):
    songs = [[idx, key, value] for idx, (key, value) in enumerate(zip(genres, plays))]
    # [[0, 'classic', 500], [1, 'pop', 600], [2, 'classic', 150], [3, 'classic', 800], [4, 'pop', 2500]]

    # 장르들의 총합 중 누가 더 큰지 파악
    new_songs = {}
    for idx, i, j in songs:
        new_songs[i] = new_songs.get(i,0) + j
    sort_genres = sorted(new_songs, key=lambda x: x[1], reverse=True)

    answer = []
    for g in sort_genres:
        result = [x for x in songs if x[1] == g]
        result.sort()
        print(f'result : {result}')
        # 숫자가 같은 경우 처리해야한다..!
        # try:
        result = sorted(result, key=lambda x:x[2], reverse=True)[:2]
        # except:
        #     result = sorted(result, key=lambda x: x[2], reverse=True)[:]

        idx = [idx for idx, g, v in result]
        answer += idx
    print(answer)
    return answer
# return [4,1,3,0]

def solution(genres, plays):
    songs = [[idx, key, value] for idx, (key, value) in enumerate(zip(genres, plays))]
    print(songs)
    new_songs = {}
    for idx, i, j in songs:
        new_songs[i] = new_songs.get(i,0) + j

    # new_songs.items()에서 sorted였다!
    sort_genres = sorted(new_songs.items(), key=lambda x: x[1], reverse=True)

    answer = []
    for g, p in sort_genres:
        result = [x for x in songs if x[1] == g]
        result = sorted(result, key=lambda x: (-x[2], x[0]))[:2]

        answer += [idx for idx, g, v in result]

    print(answer)
    # return answer
# 정렬 기준으로 다중 조건을 넘겨줄 수도 있다
# 첫 번째 인자를 기준으로 오름차순 정렬을 먼저 한다.
# 그 결과를 가지고 두 번째 인자를 기준으로 내림차순 정렬(-를 붙이면 내림차순 정렬)
# e = sorted(a, key = lambda x : (x[0], -x[1]))
# print(e)    # [(1, 0), (2, 1), (3, 2), (4, 3), (4, 2), (4, 0)]
solution(["classic", "pop", 'classic', "classic", "pop"],[800, 600, 800, 800, 2500])
solution(["classic", "pop", 'classic', "classic", "pop"],[800, 600, 800, 800, 2500])
solution(["classic", "pop", 'classic', "classic", "pop"],[500, 600, 150, 800, 2500])
solution(["classic", "pop", 'acoustic', "classic", "pop"],[800, 600, 150, 800, 2500])
