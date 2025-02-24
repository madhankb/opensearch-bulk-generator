# OpenSearch Bulk Generator

A web-based tool to generate bulk data files based on OpenSearch mapping schemas. This tool helps you create test data that matches your index mapping structure, making it perfect for testing and development purposes.

## Features

- Generate synthetic data based on OpenSearch mapping schemas
- Interactive web interface
- Preview generated data before downloading
- Download data in OpenSearch bulk API format
- Configurable number of records
- Real-time data preview
- Downloadable bulk files with timestamp

## Installation

1. Clone the repository:
```bash
git clone https://github.com/madhankb/opensearch-bulk-generator.git
cd opensearch-bulk-generator
```

2. Install dependencies:
```bash
pip3 install -r requirements.txt
```

3. Run the application:
```bash
python3 app.py
```

4. Open http://localhost:5000 in your browser

## Usage

1. Access the web interface at http://localhost:5000
2. Enter your index name in the "Index Name" field
3. Specify the number of records you want to generate (default is 10)
4. Paste your OpenSearch mapping JSON in the mapping field
5. Choose your action:
   - Click "Preview" to see sample generated data
   - Click "Generate & Download" to download the complete dataset in bulk format

### Example Mapping

```json
{
  "properties": {
    "name": {
      "type": "text"
    },
    "age": {
      "type": "integer"
    },
    "email": {
      "type": "keyword"
    },
    "is_active": {
      "type": "boolean"
    },
    "registration_date": {
      "type": "date"
    },
    "profile": {
      "type": "object",
      "properties": {
        "address": {
          "type": "text"
        },
        "phone": {
          "type": "keyword"
        }
      }
    }
  }
}
```

### Output Format

The tool generates data in OpenSearch bulk format:

```json
{"index": {"_index": "your_index_name"}}
{"name": "example", "age": 25, "email": "test@example.com", "is_active": true, "registration_date": "2024-02-11", "profile": {"address": "123 Main St", "phone": "555-0123"}}
```

## File Structure

- `app.py`: Main Flask application with data generation logic
- `templates/index.html`: Web interface template
- `requirements.txt`: Python dependencies
- `README.md`: Documentation

## Dependencies

- Flask: Web framework
- Faker: Synthetic data generation
- python-dotenv: Environment variable management

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
