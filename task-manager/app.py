from chalice import Chalice, BadRequestError
import boto3
from botocore.exceptions import ClientError
import uuid

app = Chalice(app_name='task-manager')
app.debug = True

# Conexión a DynamoDB
dynamodb = boto3.resource('dynamodb')
table_name = 'Tasks'
table = dynamodb.Table(table_name)

# Crear la tabla si no existe
def create_task_table():
    try:
        dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {'AttributeName': 'task_id', 'KeyType': 'HASH'},
            ],
            AttributeDefinitions=[
                {'AttributeName': 'task_id', 'AttributeType': 'S'},
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5,
            }
        )
        app.log.debug("Creating table...")
        table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
    except ClientError as e:
        if e.response['Error']['Code'] != 'ResourceInUseException':
            raise

create_task_table()

# Endpoints
@app.route('/tasks', methods=['POST'])
def create_task():
    request = app.current_request
    task_data = request.json_body
    task_id = str(uuid.uuid4())
    task_data['task_id'] = task_id
    task_data.update({
        'task_id': task_id,
        'complete': False
    })    
    table.put_item(Item=task_data)
    return {'message': 'Task created successfully!', 'task_id': task_id}

@app.route('/tasks', methods=['GET'])
def list_tasks():
    response = table.scan()
    return {'tasks': response.get('Items', [])}

@app.route('/tasks/{task_id}', methods=['GET'])
def get_task(task_id):
    try:
        response = table.get_item(Key={'task_id': task_id})
        if 'Item' not in response:
            raise KeyError
        return response['Item']
    except KeyError:
        return {'error': 'Task not found'}, 404

@app.route('/tasks/{task_id}', methods=['PUT'])
def update_task(task_id):
    request = app.current_request
    task_data = request.json_body

    # Validar entrada
    if not task_data:
        return {'error': 'Invalid request. Task data is required.'}, 400

    try:
        # Actualizar los campos en la tarea
        response = table.update_item(
            Key={'task_id': task_id},
            UpdateExpression="SET " + ", ".join(f"{k} = :{k}" for k in task_data.keys()),
            ExpressionAttributeValues={f":{k}": v for k, v in task_data.items()},
            ReturnValues="UPDATED_NEW"
        )
        return {'message': 'Task updated successfully!', 'updated_fields': response['Attributes']}
    except Exception as e:
        app.log.error(f"Error updating task {task_id}: {e}")
        return {'error': 'Failed to update task'}, 500


@app.route('/tasks/{task_id}', methods=['DELETE'])
def delete_task(task_id):
    table.delete_item(Key={'task_id': task_id})
    return {'message': 'Task deleted successfully!'}

@app.route('/tasks/{task_id}/complete', methods=['PATCH'])
def complete_task(task_id):
    try:
        table.update_item(
            Key={'task_id': task_id},
            UpdateExpression="SET complete = :complete",
            ExpressionAttributeValues={":complete": True},
            ReturnValues="UPDATED_NEW"
        )
        return {'message': 'Task marked as completed!'}
    except Exception as e:
        app.log.error(f"Error marking task {task_id} as completed: {e}")
        return {'error': 'Failed to mark task as completed'}, 500



@app.route('/')
def index():
    return {'message': 'Bienvenido a la API de Gestión de Tareas'}


##### TEST DE DOCUMENTACION ####

CITIES_TO_STATE = {
    'seattle': 'WA',
    'portland': 'OR',
}


@app.route('/cities/{city}')
def state_of_city(city):
    try:
        return {'state': CITIES_TO_STATE[city]}
    except KeyError:
        raise BadRequestError("Unknown city '%s', valid choices are: %s" % (
            city, ', '.join(CITIES_TO_STATE.keys())))