"""Exhaustive finite audit of the box reduction, using exact integer arithmetic.

All bounds are multiplied by four. No floating-point tolerances are used.
This checks the construction, not ETH or an asymptotic complexity theorem.
"""

from itertools import combinations, permutations, product


def audit():
    instances = tuples = 0
    for order in range(2, 5):
        vertices = range(1, order + 1)
        possible_edges = list(combinations(vertices, 2))
        for mask in range(1 << len(possible_edges)):
            edges = {e for bit, e in enumerate(possible_edges) if mask & (1 << bit)}
            for k in range(2, order + 1):
                cover = {(axis, t) for axis in range(k)
                         for t in [0, 4 * (order + 1)] +
                         [4 * v + delta for v in vertices for delta in (-1, 1)]}
                assert len(cover) == 2 * k * (order + 1)
                boxes = []
                for i, j in combinations(range(k), 2):
                    for u, v in product(vertices, repeat=2):
                        if u != v and tuple(sorted((u, v))) in edges:
                            continue
                        bounds = [(0, 4 * (order + 1)) for _ in range(k)]
                        bounds[i] = (4 * u - 1, 4 * u + 1)
                        bounds[j] = (4 * v - 1, 4 * v + 1)
                        assert all(lo < hi for lo, hi in bounds)
                        assert all((a, b) in cover for a, pair in enumerate(bounds) for b in pair)
                        boxes.append(bounds)
                geometric_feasible = False
                for x in product(vertices, repeat=k):
                    outside = not any(all(lo < 4 * value < hi
                                          for value, (lo, hi) in zip(x, box))
                                      for box in boxes)
                    clique_tuple = len(set(x)) == k and all(
                        tuple(sorted(pair)) in edges for pair in combinations(x, 2))
                    assert outside == clique_tuple, (order, mask, k, x)
                    geometric_feasible |= outside
                    tuples += 1
                clique_exists = any(all(tuple(sorted(pair)) in edges
                                        for pair in combinations(choice, 2))
                                    for choice in permutations(vertices, k))
                assert geometric_feasible == clique_exists
                instances += 1
    print(f"PASS: {instances} graph/target instances; {tuples} integer tuples; exact box and cover checks.")


if __name__ == "__main__":
    audit()
