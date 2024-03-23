from collections import defaultdict

def solution(genres, plays):
    answer = []
    plays_dict = defaultdict(int)
    genres_dict = defaultdict(list)

    for idx, (genre, play) in enumerate(zip(genres, plays)):
        plays_dict[genre] += play
        genres_dict[genre].append((idx, play))

    sorted_genres = sorted(plays_dict.keys(), key=lambda x: -plays_dict[x])

    for genre in sorted_genres:
        genres_dict[genre].sort(key=lambda x: (-x[1], x[0]))
      
        for idx, _ in genres_dict[genre][:2]:
            answer.append(idx)

    return answer
