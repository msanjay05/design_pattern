from iterator import BookCollection


def main() -> None:
    library = BookCollection(["Clean Code", "Design Patterns", "Refactoring"])

    for book in library.create_iterator():
        print(book)


if __name__ == "__main__":
    main()
