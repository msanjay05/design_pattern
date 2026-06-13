from composite import File, Folder


def main() -> None:
    root = Folder("project")
    root.add(File("README.md", 4))
    src = Folder("src")
    src.add(File("main.py", 12))
    src.add(File("utils.py", 8))
    root.add(src)

    print(root.display())
    print(f"Total size: {root.size()} KB")


if __name__ == "__main__":
    main()
