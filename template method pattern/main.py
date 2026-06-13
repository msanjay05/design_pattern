from template_method import JsonDataMiner, PdfDataMiner


def main() -> None:
    print(PdfDataMiner().mine("report.pdf"))
    print(JsonDataMiner().mine("metrics.json"))


if __name__ == "__main__":
    main()
