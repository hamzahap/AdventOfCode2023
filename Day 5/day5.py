import numpy as np

def parse_map(lines):
    return np.array([list(map(int, line.split())) for line in lines if line.strip()], dtype=object)

def cnv_nums(nums, cmap):
    cnums = nums.copy()
    for m in cmap:
        if len(m) == 3:
            dst, src, rng = m
            mask = (nums >= src) & (nums < src + rng)
            cnums[mask] = dst + (cnums[mask] - src)
    return cnums

def parse_ranges(line):
    parts = list(map(int, line.split()))
    return [(parts[i], parts[i] + parts[i + 1]) for i in range(0, len(parts), 2)]

def update_ranges(rngs, cmap):
    new_rngs = []
    for dst, src, lng in cmap:
        src_end = src + lng
        for rng_start, rng_end in rngs:
            if rng_start < src_end and rng_end > src:
                incstrt = max(rng_start, src)
                incend = min(rng_end, src_end)
                newst = dst + (incstrt - src)
                newend = dst + (incend - src)
                new_rngs.append((newst, newend))
    return new_rngs

def process_file(filename):
    with open(filename, 'r') as file:
        content = file.read()

    parts = content.split('\n\n')

    p1 = np.array(list(map(int, parts[0].split(': ')[1].split())))
    maps = [parse_map(part.split('\n')[1:]) for part in parts[1:]]
    for m in maps:
        p1 = cnv_nums(p1, m)
    part1_res = np.min(p1)

    rngs = parse_ranges(parts[0].split(': ')[1])
    for m in maps:
        rngs = update_ranges(rngs, m)
    part2_res = min(st for st, en in rngs)

    return part1_res, part2_res

part1, part2 = process_file('input.txt')
print("Part 1:", part1)
print("Part 2:", part2)
