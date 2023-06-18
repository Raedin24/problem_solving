import time

def findWinners(matches: list[list[int]]) -> list[list[int]]:
    winners = []
    losers = []
    answer = [[], []]

    for match in matches:
        winners.append(match[0])
        losers.append(match[1])

    for winner in winners:
        if winner not in losers and winner not in answer[0]:
            answer[0].append(winner)
        elif winner in losers and losers.count(winner) == 1 and winner not in answer[1]:
            answer[1].append(winner)
    
    for loser in losers:
        if losers.count(loser) == 1 and loser not in answer[1]:
            answer[1].append(loser)

    answer[0].sort()
    answer[1].sort()
    return answer

def findWinners1(matches: list[list[int]]) -> list[list[int]]:
    from collections import Counter
    winners = []
    losers = []
    answer = [[], []]

    for match in matches:
        winners.append(match[0])
        losers.append(match[1])

    for winner in winners:
        if winner not in losers and Counter(answer[0])[winner] == 0:
            answer[0].append(winner)
        elif winner in losers and Counter(losers)[winner ]== 1 and Counter(answer[1])[winner] == 0:
            answer[1].append(winner)
    
    for loser in losers:
        if losers.count(loser) == 1 and loser not in answer[1]:
            answer[1].append(loser)

    answer[0].sort()
    answer[1].sort()
    return answer


from collections import defaultdict

# Optimal solution. 2 tries
def findWinners(matches: list[list[int]]) -> list[list[int]]:
    losses = defaultdict(int)
    winners = set()

    for winner, loser in matches:
        winners.add(winner)
        losses[loser] += 1

    answer = [[], []]

    for player in winners:
        if losses[player] == 0:
            answer[0].append(player)
        elif losses[player] == 1:
            answer[1].append(player)

    for player, loss_count in losses.items():
        if loss_count == 1 and player not in winners:
            answer[1].append(player)

    answer[0].sort()
    answer[1].sort()
    return answer
