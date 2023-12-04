def readcard(fname):
    with open(fname, 'r') as file:
        cards = []
        for line in file:
            parts = line.strip().split('|')
            if len(parts) != 2:
                continue 

            _, matches = parts[0].split(':', 1)
            nums = parts[1]

            mset = set(map(int, matches.split()))
            bset = set(map(int, nums.split()))
            cards.append((mset, bset))
        return cards

def matchingcards(cards):
    counts = [1] * len(cards)  
    for j, (matchcards, bcards) in enumerate(cards):
        matches = len(matchcards & bcards) 
        for i in range(1, matches + 1):
            if j + i < len(cards):
                counts[j + i] += counts[j]
    return sum(counts)

cards = readcard('input.txt')
total_count = matchingcards(cards)

print(total_count)
