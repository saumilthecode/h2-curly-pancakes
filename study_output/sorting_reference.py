"""H2 promo sorting reference: ascending unless the function says otherwise.

Based on notes/LT12a through LT12e and their embedded promo/mock examples.
Read one function, cover it, then rebuild it from its memory phrase.

If an exam supplies pseudocode, follow its pivot, indexing, return value,
and requested algorithm. These are working reference implementations.
"""


# BUBBLE: passes -> adjacent pairs -> compare -> swap.
# Mutates the original list and returns that same list.
def bubble_sort(a):
    for end in range(len(a) - 1, 0, -1):
        swapped = False                  # reset at the START of each pass
        for j in range(end):
            if a[j] > a[j + 1]:          # > means ascending; < means descending
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:                  # only AFTER a whole pass
            break
    return a


# INSERTION, school swap version: next item -> walk left -> stop when it fits.
# Mutates the original list and returns it.
def insertion_sort(a):
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
            j -= 1
    return a


# INSERTION, shifting version: hold -> shift -> insert in the gap.
# Recognise this version when it appears in supplied pseudocode.
def insertion_sort_shift(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:      # index 0 is a valid position
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key                   # j stopped BEFORE the insertion slot
    return a


# MERGE helper: compare heads -> take smaller -> append leftovers.
# Both input lists must ALREADY be sorted.
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:          # left wins ties: preserves stability
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]


# MERGE SORT: base -> split -> recurse on BOTH halves -> merge.
# Returns a new sorted list; the input stays unchanged.
def merge_sort(a):
    if len(a) <= 1:                      # handles [] as well as a singleton
        return a.copy()
    mid = len(a) // 2
    # If the question puts an odd extra item on the LEFT, use:
    # mid = (len(a) + 1) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)            # left + right alone is NOT a merge


# QUICK, THREE LISTS: base -> pivot -> less/equal/greater -> recurse + join.
# First-element pivot, like the mock. Returns a new list.
def quick_sort_three_lists(a):
    if len(a) <= 1:
        return a.copy()
    pivot = a[0]
    less = []
    equal = []
    greater = []
    for value in a:                      # include pivot: it enters equal
        if value < pivot:
            less.append(value)
        elif value == pivot:
            equal.append(value)
        else:
            greater.append(value)
    return quick_sort_three_lists(less) + equal + quick_sort_three_lists(greater)


# QUICK, TWO LISTS: last pivot is handled separately.
# Recognise the difference from three lists: EXCLUDE the pivot in the loop.
def quick_sort_two_lists(a):
    if len(a) <= 1:
        return a.copy()
    pivot = a[-1]
    left = []
    right = []
    for value in a[:-1]:                 # not `a`, or the pivot is duplicated
        if value < pivot:
            left.append(value)
        else:
            right.append(value)
    return quick_sort_two_lists(left) + [pivot] + quick_sort_two_lists(right)


# QUICK, IN PLACE: school's LAST-pivot partition.
# L moves past values < pivot; H moves past values >= pivot.
# Swap misplaced values; when pointers cross, put the pivot at L.
def partition_last(a, start, end):
    pivot = a[end]
    low = start
    high = end - 1
    while low <= high:
        while low <= high and a[low] < pivot:
            low += 1
        while low <= high and a[high] >= pivot:
            high -= 1
        if low <= high:
            a[low], a[high] = a[high], a[low]
    a[low], a[end] = a[end], a[low]
    return low                          # pivot's final INDEX, not its value


def qsort_last(a, start, end):
    if start < end:
        mid = partition_last(a, start, end)
        qsort_last(a, start, mid - 1)    # exclude the fixed pivot
        qsort_last(a, mid + 1, end)
    return a


def quick_sort_in_place(a):
    return qsort_last(a, 0, len(a) - 1)


# FIRST-pivot variation, used in the 2025 promo pseudocode.
# Start low one past the pivot; finally place the pivot at HIGH.
def partition_first(a, start, end):
    pivot = a[start]
    low = start + 1
    high = end
    while low <= high:
        while low <= high and a[low] < pivot:
            low += 1
        while low <= high and a[high] >= pivot:
            high -= 1
        if low <= high:
            a[low], a[high] = a[high], a[low]
    a[start], a[high] = a[high], a[start]
    return high


def qsort_first(a, start, end):
    if start < end:
        mid = partition_first(a, start, end)
        qsort_first(a, start, mid - 1)
        qsort_first(a, mid + 1, end)
    return a


def quick_sort_first_in_place(a):
    return qsort_first(a, 0, len(a) - 1)


# SELECTION: optional in the notes. Find min INDEX -> swap ONCE per pass.
def selection_sort(a):
    for i in range(len(a) - 1):
        smallest = i
        for j in range(i + 1, len(a)):
            if a[j] < a[smallest]:
                smallest = j
        a[i], a[smallest] = a[smallest], a[i]
    return a


# EXAM PATTERN: records + descending + stable ties + counting swaps.
# Bubble/count/stability: 2026 mock Task 5.
# Numeric conversion: also tested in the 2023/2024 record-sort questions.
# Example records: [('A', '12'), ('B', '7'), ('C', '12')].
def bubble_records_desc_count(records):
    swaps = 0
    for end in range(len(records) - 1, 0, -1):
        for j in range(end):
            if int(records[j][1]) < int(records[j + 1][1]):
                records[j], records[j + 1] = records[j + 1], records[j]
                swaps += 1              # inside IF: count only actual swaps
    return swaps                        # list changes; return the requested count


# EXAM PATTERN: 2026 mock three-list quicksort on (species, count) records.
# Compare one FIELD; append the WHOLE record. Counts here are numeric already.
def partition_records(records):
    pivot = records[0][1]
    less = []
    equal = []
    greater = []
    for record in records:
        if record[1] < pivot:
            less.append(record)
        elif record[1] == pivot:
            equal.append(record)
        else:
            greater.append(record)
    return less, equal, greater


def quick_sort_records(records):
    if len(records) <= 1:
        return records.copy()
    less, equal, greater = partition_records(records)
    return quick_sort_records(less) + equal + quick_sort_records(greater)


# OTHER TRICKS FROM YOUR MATERIALS:
# - Comparison counter: increment immediately BEFORE the value comparison.
#   In insertion's while loop, a failed value comparison also counts, but an
#   index-boundary test is not a value comparison. Follow the stated convention.
# - Swap counter: increment only INSIDE the branch that swaps.
# - Ascending bubble/insertion: strict >; descending: strict <.
#   Using >= or <= would move equal keys past one another.
# - Merge ascending: use <= so LEFT wins ties. Descending: >=, left still wins.
# - Records: compare a[j][field], but move a[j] (the entire record).
# - CSV numeric strings: int(...) for whole numbers, float(...) for decimals.
# - a[:] / a.copy() makes a shallow list copy; b = a aliases the same list.
# - a[:mid] excludes mid; a[mid:] includes mid. Together they preserve every item.
# - Python list.pop(0) removes the front, shifting remaining values each time.
#   If translating supplied pop(0) pseudocode, follow it. The pointer-based
#   merge above avoids repeated shifts and gives a linear-time merge.
# - Test an empty list, one item, duplicates, sorted and reverse-sorted values.


if __name__ == '__main__':
    sample = [5, 2, 4, 1, 6, 3]
    print('Input:', sample)
    print('Bubble:', bubble_sort(sample.copy()))
    print('Insertion:', insertion_sort(sample.copy()))
    print('Merge:', merge_sort(sample))
    print('Quick (three lists):', quick_sort_three_lists(sample))
    print('Quick (in place):', quick_sort_in_place(sample.copy()))
    records = [('A', '12'), ('B', '7'), ('C', '12')]
    swaps = bubble_records_desc_count(records)
    print('Descending records:', records, '| swaps:', swaps)
