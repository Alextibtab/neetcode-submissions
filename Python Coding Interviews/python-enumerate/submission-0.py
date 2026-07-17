from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    for idx, ele in enumerate(nums):
        if ele == 7:
            return idx
    return -1


def get_dist_between_sevens(nums: List[int]) -> int:
    first_idx = None
    last_idx = None
    for idx, ele in enumerate(nums):
        if ele == 7 and first_idx is None:
            first_idx = idx
        elif ele == 7 and last_idx is None:
            last_idx = idx
    return last_idx - first_idx 

# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
