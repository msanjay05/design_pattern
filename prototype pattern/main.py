from documents import Report


def main() -> None:
    original = Report("Q1 Report", ["Revenue", "Costs", "Forecast"])
    copy_report = original.clone()
    copy_report.title = "Q1 Report (Draft)"
    copy_report.sections.append("Notes")

    print(original.show())
    print(copy_report.show())


if __name__ == "__main__":
    main()
