from flask import Flask, request, render_template, jsonify, send_file
from faker import Faker
import json
import os
import logging
from datetime import datetime
import io

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
fake = Faker()

def generate_data_from_mapping(mapping, num_records=10):
    data = []
    properties = mapping.get('properties', {})
    
    for _ in range(num_records):
        record = {}
        for field_name, field_config in properties.items():
            field_type = field_config.get('type', 'keyword')
            
            if field_type == 'text' or field_type == 'keyword':
                record[field_name] = fake.word()
            elif field_type == 'long' or field_type == 'integer':
                record[field_name] = fake.random_int()
            elif field_type == 'double' or field_type == 'float':
                record[field_name] = round(fake.random.uniform(0, 1000), 2)
            elif field_type == 'date':
                record[field_name] = fake.date()
            elif field_type == 'boolean':
                record[field_name] = fake.boolean()
            elif field_type == 'object':
                if 'properties' in field_config:
                    nested_data = generate_data_from_mapping({'properties': field_config['properties']}, 1)
                    record[field_name] = nested_data[0]
            elif field_type == 'nested':
                if 'properties' in field_config:
                    num_nested = fake.random_int(min=1, max=3)
                    record[field_name] = generate_data_from_mapping(
                        {'properties': field_config['properties']}, 
                        num_nested
                    )
        data.append(record)
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        logger.debug(f"Received request data: {data}")
        
        mapping = data['mapping']
        index_name = data['index_name']
        num_records = data.get('num_records', 10)
        action = data.get('action', 'download')  # 'download' or 'preview'
        
        logger.debug(f"Generating {num_records} records for index {index_name}")
        
        # Generate fake data based on the mapping
        generated_data = generate_data_from_mapping(mapping, num_records)
        
        # Create bulk data format
        bulk_data = []
        for doc in generated_data:
            bulk_data.append(json.dumps({"index": {"_index": index_name}}))
            bulk_data.append(json.dumps(doc))
        
        if action == 'preview':
            return jsonify({
                'status': 'success',
                'message': f'Generated {len(generated_data)} records',
                'sample_data': generated_data[:2],
                'bulk_sample': bulk_data[:4]  # Show 2 documents in bulk format
            })
        else:
            # Create bulk file
            bulk_content = '\n'.join(bulk_data) + '\n'  # Add final newline
            
            # Create in-memory file
            mem_file = io.BytesIO()
            mem_file.write(bulk_content.encode('utf-8'))
            mem_file.seek(0)
            
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"bulk_data_{index_name}_{timestamp}.json"
            
            return send_file(
                mem_file,
                mimetype='application/json',
                as_attachment=True,
                download_name=filename
            )
    
    except Exception as e:
        logger.error(f"Error in generate endpoint: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
