# OpenSearch Bulk Data Generator from Mapping

A web-based tool to generate bulk data files based on OpenSearch mapping schemas. This tool helps you create test data that matches your index mapping structure.

## Features

- Generate data based on OpenSearch mapping schemas
- Support for various field types:
  - text/keyword
  - integer/long
  - float/double
  - date
  - boolean
  - object
  - nested
- Preview generated data before downloading
- Download data in OpenSearch bulk API format
- Configurable number of records

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd opensearch-bulk-generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open http://localhost:5008 in your browser

## Usage

1. Enter your index name
2. Specify the number of records you want to generate
3. Paste your OpenSearch mapping JSON
4. Click "Preview Data" to see sample generated data
5. Click "Generate & Download Bulk File" to download the complete dataset

### Example Mapping

```json
{
  "properties": {
    "title": { "type": "text" },
    "description": { "type": "text" },
    "price": { "type": "double" },
    "created_at": { "type": "date" },
    "in_stock": { "type": "boolean" },
    "category": { "type": "keyword" },
    "tags": {
      "type": "nested",
      "properties": {
        "name": { "type": "keyword" },
        "score": { "type": "float" }
      }
    }
  }
}
```

### Using the Generated File

The tool generates a file in the OpenSearch bulk API format. You can use this file with the OpenSearch bulk API:

```bash
curl -X POST "localhost:9200/_bulk" -H "Content-Type: application/x-ndjson" --data-binary "@bulk_data_file.json"
```

For OpenSearch:
```bash
curl -X POST "https://your-opensearch-endpoint/_bulk" -H "Content-Type: application/x-ndjson" --data-binary "@bulk_data_file.json" -u "username:password"
```

## Supported Field Types

- `text`: Generates random words
- `keyword`: Generates random words
- `long`/`integer`: Generates random numbers
- `double`/`float`: Generates random decimal numbers
- `date`: Generates random dates
- `boolean`: Generates random true/false values
- `object`: Generates nested objects based on the specified properties
- `nested`: Generates an array of nested objects based on the specified properties
