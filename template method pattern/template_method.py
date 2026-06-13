from abc import ABC, abstractmethod


class DataMiner(ABC):
    def mine(self, path: str) -> str:
        raw = self.open_file(path)
        data = self.parse(raw)
        analysis = self.analyze(data)
        return self.report(analysis)

    def open_file(self, path: str) -> str:
        return f"opened:{path}"

    @abstractmethod
    def parse(self, raw: str) -> str: ...

    @abstractmethod
    def analyze(self, data: str) -> str: ...

    def report(self, analysis: str) -> str:
        return f"Report -> {analysis}"


class PdfDataMiner(DataMiner):
    def parse(self, raw: str) -> str:
        return f"parsed-pdf({raw})"

    def analyze(self, data: str) -> str:
        return f"pdf-insights({data})"


class JsonDataMiner(DataMiner):
    def parse(self, raw: str) -> str:
        return f"parsed-json({raw})"

    def analyze(self, data: str) -> str:
        return f"json-insights({data})"
