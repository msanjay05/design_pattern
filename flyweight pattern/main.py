from flyweight import Tree, TreeFactory


def main() -> None:
    forest = []
    for x, y in [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]:
        tree_type = TreeFactory.get_tree_type("Oak", "green", "rough")
        forest.append(Tree(x, y, tree_type))

    for tree in forest[:2]:
        print(tree.draw())

    print(f"Trees in forest: {len(forest)}")
    print(f"Shared TreeType objects: {TreeFactory.pool_size()}")


if __name__ == "__main__":
    main()
