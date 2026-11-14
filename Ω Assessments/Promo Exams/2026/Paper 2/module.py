"""Functional Queue and BinarySearchTree ADTs supplied for the examination."""

__all__ = [
    "make_empty_queue",
    "is_empty_queue",
    "queue_size",
    "make_empty_tree",
    "make_tree",
    "entry",
    "left_branch",
    "right_branch",
    "is_empty",
    "print_tree",
]


# Queue ADT
def make_empty_queue():
    return []


def is_empty_queue(queue):
    return queue == []


def queue_size(queue):
    return len(queue)


# BinarySearchTree ADT
# Constructors
def make_empty_tree():
    return []


def make_tree(entry, left, right):  # [entry, [], []]
    return [entry, left, right]


# Accessors
def entry(tree):
    return tree[0]


def left_branch(tree):
    return tree[1]


def right_branch(tree):
    return tree[2]


# Predicate
def is_empty(tree):
    return tree == []


def print_tree(tree, print_output=True):
    """Print the tree one level at a time, with the root at the top."""

    def get_elements_at_level(current_tree, level):
        def helper(current_tree, target_level, current_level):
            if is_empty(current_tree) and current_level < target_level:
                dummy = make_tree(
                    " ",
                    make_empty_tree(),
                    make_empty_tree(),
                )
                return helper(
                    left_branch(dummy),
                    target_level,
                    current_level + 1,
                ) + helper(
                    right_branch(dummy),
                    target_level,
                    current_level + 1,
                )

            if current_level == target_level:
                if is_empty(current_tree):
                    return (" ",)
                return (entry(current_tree),)

            return helper(
                left_branch(current_tree),
                target_level,
                current_level + 1,
            ) + helper(
                right_branch(current_tree),
                target_level,
                current_level + 1,
            )

        return helper(current_tree, level, 0)

    def height(current_tree):
        if is_empty(current_tree):
            return 0
        return 1 + max(
            height(left_branch(current_tree)),
            height(right_branch(current_tree)),
        )

    tree_height = height(tree)
    output_string = ""

    for level in range(tree_height):
        indent = 2 ** (tree_height - (level + 1)) - 1
        spacing = 2 ** (tree_height - level) - 1
        output = " " * indent

        for index, item in enumerate(get_elements_at_level(tree, level)):
            if level == 0 or index == 0:
                output += str(item)
            else:
                output += " " * spacing + str(item)

        if print_output:
            print(output)
        else:
            output_string += output + "/"

    if not print_output:
        return output_string
