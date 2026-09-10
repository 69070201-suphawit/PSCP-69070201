"""card44"""
card = input().strip()
rank_text = card[:-1].upper()
suit_text = card[-1].upper()

rank_name = {
    "A" : "ace","J" : "jack","Q" : "queen","K" : "king"
}
suit_name = {
    "D": "diamonds","H": "hearts","S": "spades","C": "clubs"
}
rank = rank_name.get(rank_text, rank_text)
suit = suit_name[suit_text]
print(f"{rank} of {suit}")
