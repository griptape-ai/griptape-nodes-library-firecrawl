from firecrawl import FirecrawlApp, ScrapeOptions
from typing import Callable, Generator
from textwrap import dedent

from firecrawl.firecrawl import CrawlStatusResponse, FirecrawlDocument
from griptape_nodes.exe_types.core_types import Parameter, ParameterMode, ParameterGroup
from griptape_nodes.exe_types.node_types import DataNode


class FirecrawlCrawler(DataNode):
    app: FirecrawlApp

    def __init__(self, name: str, metadata: dict | None = None) -> None:
        super().__init__(name, metadata)
        self.app = FirecrawlApp(
            api_key=self.get_config_value("Firecrawl", "FIRECRAWL_API_KEY")
        )

        self.add_parameter(
            Parameter(
                name="website",
                input_types=["str"],
                type="str",
                output_type="str",
                default_value=None,
                tooltip="The website to crawl",
                ui_options={"placeholder_text": "Website URL"},
            )
        )

        self.add_parameter(
            Parameter(
                name="output",
                type="str",
                output_type="str",
                default_value=None,
                allowed_modes={ParameterMode.OUTPUT},
                tooltip="The crawled data",
                ui_options={"multiline": True, "placeholder_text": "Scraped data"},
            )
        )

        with ParameterGroup(name="Logs") as logs_group:
            Parameter(
                name="include_details",
                type="bool",
                default_value=False,
                tooltip="Include extra details.",
            )

            Parameter(
                name="logs",
                type="str",
                tooltip="Displays processing logs and detailed events if enabled.",
                ui_options={"multiline": True, "placeholder_text": "Logs"},
                allowed_modes={ParameterMode.OUTPUT},
            )

        logs_group.ui_options = {"hide": True}  # Hide the logs group by default.

        self.add_node_element(logs_group)

    def process(self) -> Generator[Callable, CrawlStatusResponse, None]:
        self.append_value_to_parameter("logs", "Crawling...\n")
        crawl_result = yield lambda: self.app.crawl_url(
            self.parameter_values["website"],
            limit=10,
            scrape_options=ScrapeOptions(formats=["markdown"]),
        )
        self.append_value_to_parameter("logs", "Crawling completed.\n")

        # Set the output
        text = "\n\n".join([self._format_data(data) for data in crawl_result.data])

        self.parameter_output_values["output"] = text

    def _format_data(self, document: FirecrawlDocument) -> str:
        if not document.markdown:
            raise ValueError("No markdown data found in the document.")

        if not document.metadata:
            raise ValueError("No metadata found in the document.")

        text = dedent(f"""
        ---
        Title: {document.metadata.get("title", "No title available.")}
        Source: {document.metadata.get("sourceURL", "Unknown")}
        Description: {document.metadata.get("description", "No description available.")}
        ---
        Text: {document.markdown}
        """)

        return text
