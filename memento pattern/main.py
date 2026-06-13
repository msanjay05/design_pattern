from memento import History, TextEditor


def main() -> None:
    editor = TextEditor()
    history = History()

    editor.write("First draft")
    history.push(editor.save())

    editor.write("Revised draft")
    print(f"Current: {editor.show()}")

    editor.restore(history.pop() or editor.save())
    print(f"Restored: {editor.show()}")


if __name__ == "__main__":
    main()
