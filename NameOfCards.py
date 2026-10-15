"""cardname"""
ranks = {"A": "Ace", "J": "Jack", "Q": "Queen", "K": "King"}
suits = {"D": "Diamonds", "H": "Hearts", "S": "Spades", "C": "Clubs"}
card = input().strip().upper()
rank = card[:-1]
suit = card[-1]
print(f"{ranks.get(rank, rank)} of {suits[suit]}")
