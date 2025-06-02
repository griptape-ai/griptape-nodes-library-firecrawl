# Firecrawl Node for Griptape Nodes 

This library provides a node for interacting with the Firecrawl API. Firecrawl is a popular service that provides web scraping and crawl capabilities. Learn more at [firecrawl.dev](https://firecrawl.dev).

## Features

* Crawl and scrape a single website to a configurable depth
* Output markdown for use by agents or other downstream nodes

### Installation

1. Clone this repository into your Griptape Nodes workspace directory:

```bash
# Navigate to your workspace directory
cd $(gtn config | grep workspace_directory | cut -d'"' -f4)

# Clone the repository
git clone https://github.com/griptape-ai/griptape-nodes-library-firecrawl.git
```

2. Install dependencies

```bash
cd griptape-nodes-library-firecrawl
uv sync
```

## API Key Setup

You will need a Firecrawl API key to use this node.

### Get your API Key

1. Visit [firecrawl.dev](https://firecrawl.dev)
2. Sign up for Firecrawl
3. Select *API Keys* in the left navigation menu, or visit https://www.firecrawl.dev/app/api-keys
4. Create a new key with the *+ Create API Key* button
5. Name your key and copy your credential using the clipboard icon next to the partially obscufacted API key in the API Key column

### Configure your API Key

Configure your API key through the Griptape Nodes IDE:

1. Open the *Settings* menu.
2. Navigate to the *API Keys & Secrets* panel.
3. Click *+ Add Secret* in the top right. Enter `FIRECRAWL_API_KEY` as the name of the new secret.
4. Paste the Firecrawl API key that you copied earlier into the new field named `FIRECRAWL_API_KEY`.

### Add the Firecrawl library to your installed Engine

If you haven't already installed your Griptape Nodes engine, follow the installation steps [HERE](https://github.com/griptape-ai/griptape-nodes). After you've completed those and you have your engine up and running: 

1. Navigate to *Engine Settings* in the Griptape Nodes *Settings* Menu 
2. Add the complete path to the `griptape_nodes_library.json` file within this `griptape-nodes-library-firecrawl/griptape_nodes_library_firecrawl` directory to the empty field at the bottom of the *Libraries To Register* section.
3. Exit out of settings. The new path will save automatically
4. Refresh the libraries in your editor by clicking *Refresh Libraries* at the bottom of the left hand Nodes panel.
5. You should see the Firecrawl category appear in the Nodes panel. Expand this category to see the Firecrawl node and drag the node onto the edit canvas to create and instance of this node.


## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
