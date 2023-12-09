from collections import namedtuple
from pathlib import Path
import re
import math

Card = namedtuple('Card', ['card_number', 'winning_numbers', 'playing_numbers', 'matching_numbers', 'points'])

def read_file(filename: str) -> list[str]:
    current_script_path = Path(__file__).resolve()
    combined_path = Path.joinpath(current_script_path.parent,filename)
    file_contents: list[str] = []
    with open(combined_path, 'rt') as FILE:
        file_contents = FILE.readlines()
    return [line[:-1] for line in file_contents]

def setup_cards(lines: list[str]):
    cards: list[Card] = []
    for line in lines:
        card, rest = line.split(':')
        card_number = re.findall(r'Card\s+(\d+)', card)
        winning_numbers, playing_numbers = rest.strip().split('|')
        w = re.findall(r'\d+', winning_numbers)
        p = re.findall(r'\d+', playing_numbers)
        w_numbers = [int(wn) for wn in w]
        p_numbers = [int(pn) for pn in p]
        W = set(w_numbers)
        P = set(p_numbers)
        I = W.intersection(P)
        points = 0
        if len(I) > 0: points = math.pow(2,len(I) -1)
        cards.append(Card(card_number[0], W, P, I, int(points)))
    return cards

def sum_points(cards: list[Card]) -> int:
    total = 0
    for card in cards:
        total += card.points
    return total
def part1():
    lines = read_file('input.txt')
    cards = setup_cards(lines)
    total = sum_points(cards)
    return total

def recursive_traversal(cards, winning_cards, instance_count):
    for card in cards:
        # every card is counted at least once
        card_number = card.card_number
        instance_count[card.card_number] += 1
        next_round_winning_count = len(card.matching_numbers)
        cards_nums_to_check = [str(n) for n in list(range(int(card_number) + 1, int(card_number) + int(next_round_winning_count) + 1))]
        # need to separate the cards that are winners from those that are not, but were chosen based on the winner
        # the ones that are not get points in this cycle
        cards_to_check = [card for card in winning_cards if card.card_number in cards_nums_to_check]
        cards_nums = [card.card_number for card in cards_to_check]
        card_nums_to_check_future_not_winners = [nw for nw in cards_nums_to_check if nw not in cards_nums]
        for wc in card_nums_to_check_future_not_winners:
            instance_count[wc] += 1
        recursive_traversal(cards_to_check, winning_cards, instance_count)

def part2():
    lines = read_file('input.txt')
    cards = setup_cards(lines)
    instances_count = {}
    # '1': 1 etc
    winning_cards = [card for card in cards if card.points > 0]
    # initialize winning card instance count
    for card in cards:
        instances_count[card.card_number] = 0

    recursive_traversal(cards, winning_cards, instances_count)
    cards_count = 0
    for v in instances_count.values():
        cards_count += v
    return cards_count

def results():
    answer1 = part1()
    answer2 = part2()
    pass

results()