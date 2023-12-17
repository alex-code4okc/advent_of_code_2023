import re
from pathlib import Path
from collections import namedtuple, Counter

Play = namedtuple('Play', ['hand', 'bid'])

def read_file(filename: str) -> list[str]:
    current_script_path = Path(__file__).resolve()
    combined_path = Path.joinpath(current_script_path.parent,filename)
    file_contents: list[str] = []
    with open(combined_path, 'rt') as FILE:
        file_contents = FILE.readlines()
    return file_contents

def setup():
    plays = []
    lines = read_file('input.txt')
    for line in lines:
        hand_bid = line.strip().split(' ')
        plays.append(Play(hand_bid[0], int(hand_bid[1])))
    return plays

# Ranks
# 5 of a kind (AAAAA)
# 4 of a kind (AAAA5)
# Full house (3 and 2 of a kind) (AAA55)
# 3 of a kind (AAA86)
# Two pair (2 and 2 of a kind (both different)) (AAKK2)
# One pair (2 of a kind) (AA234)
# High card (all distinc cards) (23456)
five_of_a_kind = Counter([5])
four_of_a_kind = Counter([4,1])
full_house = Counter([2,3])
three_of_a_kind = Counter([3,1,1])
two_pair = Counter([2,2,1])
one_pair = Counter([2,1,1,1])
high_card = Counter([1,1,1,1,1])

card_order = {
    'A': 12,
    'K': 11,
    'Q': 10,
    'J': 9,
    'T': 8,
    '9': 7,
    '8': 6,
    '7': 5,
    '6': 4,
    '5': 3,
    '4': 2,
    '3': 1,
    '2': 0,
}

second_card_order = {
    'A': 12,
    'K': 11,
    'Q': 10,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1,
    'J': 0,
}

def calculate_hand_rank(play: Play):
    card_count = Counter(play.hand)
    rank_count = Counter(card_count.values())
    return rank_count

def calculate_hand_rank_joker(play: Play):
    card_count = Counter(play.hand)
    card_counts = []
    for k,v in card_count.items():
        if k != 'J':
            card_counts.append([k,v])
    card_counts.sort(key=lambda d: d[1], reverse=True)
    if card_count['J'] == 5:
        # replace with highest ranking 'A'
        return five_of_a_kind
    elif card_count['J'] > 0:
        largest_count = card_counts[0]
        largest_count[1] += card_count['J']
    card_counts_values = [v[1] for v in card_counts]
    rank_count = Counter(card_counts_values)
    return rank_count



def sort_ranks(bucket, order):
    # sort by all 5 indices
    return bucket.sort(key=lambda d: [order[d.hand[0]], order[d.hand[1]], order[d.hand[2]], order[d.hand[3]], order[d.hand[4]]])

def part1():
    final_ranks = []
    plays = setup()
    fives = []
    fours = []
    full_houses = []
    threes = []
    twos = []
    ones = []
    highs = []
    for play in plays:
        rank = calculate_hand_rank(play)
        if rank == five_of_a_kind:
            fives.append(play)
        if rank == four_of_a_kind:
            fours.append(play)
        if rank == full_house:
            full_houses.append(play)
        if rank == three_of_a_kind:
            threes.append(play)
        if rank == two_pair:
            twos.append(play)
        if rank == one_pair:
            ones.append(play)
        if rank == high_card:
            highs.append(play)
    sort_ranks(fives, card_order)
    sort_ranks(fours, card_order)
    sort_ranks(full_houses, card_order)
    sort_ranks(threes, card_order)
    sort_ranks(twos, card_order)
    sort_ranks(ones, card_order)
    sort_ranks(highs, card_order)
    
    final_ranks += highs
    final_ranks += ones
    final_ranks += twos
    final_ranks += threes
    final_ranks += full_houses
    final_ranks += fours
    final_ranks += fives
    final_sum = 0
    for i, ranked in enumerate(final_ranks):
        multipler = i+1
        bid = ranked.bid
        final_sum += bid*multipler
    return final_sum

def part2():
    final_ranks = []
    plays = setup()
    fives = []
    fours = []
    full_houses = []
    threes = []
    twos = []
    ones = []
    highs = []
    for play in plays:
        rank = calculate_hand_rank_joker(play)
        if rank == five_of_a_kind:
            fives.append(play)
            continue
        if rank == four_of_a_kind:
            fours.append(play)
            continue
        if rank == full_house:
            full_houses.append(play)
            continue
        if rank == three_of_a_kind:
            threes.append(play)
            continue
        if rank == two_pair:
            twos.append(play)
            continue
        if rank == one_pair:
            ones.append(play)
            continue
        if rank == high_card:
            highs.append(play)
            continue
    sort_ranks(fives, second_card_order)
    sort_ranks(fours, second_card_order)
    sort_ranks(full_houses, second_card_order)
    sort_ranks(threes, second_card_order)
    sort_ranks(twos, second_card_order)
    sort_ranks(ones, second_card_order)
    sort_ranks(highs, second_card_order)
    
    final_ranks += highs
    final_ranks += ones
    final_ranks += twos
    final_ranks += threes
    final_ranks += full_houses
    final_ranks += fours
    final_ranks += fives
    final_sum = 0
    for i, ranked in enumerate(final_ranks):
        multipler = i+1
        bid = ranked.bid
        final_sum += bid*multipler
    return final_sum

def results():
    answer1 = part1()
    answer2 = part2()
    pass

results()