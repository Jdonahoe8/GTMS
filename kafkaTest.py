from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers=['broker1:1234'])

# Asynchronous by default
future = producer.send('my-topic', b'raw_bytes')

# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    # Decide what to do if produce request failed...
    log.exception()
    pass

# Successful result returns assigned partition and offset
print (record_metadata.topic)
print (record_metadata.partition)
print (record_metadata.offset)

# produce keyed messages to enable hashed partitioning
producer.send('my-topic', key=b'foo', value=b'bar')

# encode objects via msgpack
producer = KafkaProducer(value_serializer=msgpack.dumps)
producer.send('msgpack-topic', {'key': 'value'})

# produce json messages
producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'))
producer.send('json-topic', {'key': 'value'})

# produce asynchronously
for _ in range(100):
    producer.send('my-topic', b'msg')

def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)
    # handle exception

# produce asynchronously with callbacks
producer.send('my-topic', b'raw_bytes').add_callback(on_send_success).add_errback(on_send_error)

# block until all async messages are sent
producer.flush()

# configure multiple retries
producer = KafkaProducer(retries=5)


myDict = {'Coolant_Temperature' : 0, 'ECU_Battery_Voltage' : 0, 'Engine_Oil_Pressure' : 0, 'Engine_Oil_Temperature' : 0,'Engine_Speed' : 0, 'ABSMAP_raw' : 0, 'Vehicle_Speed' : 0,'Exhaust_Lambda' : 0, 'Fuel_Pressure_Sensor' : 0, 'Gear' : 'N','Wheel_Speed_FL': 0, 'Wheel_Speed_FR' : 0,'Wheel_Speed_RL' : 0, 'Wheel_Speed_RR' : 0,'Throttle_Position' : 0, 'Engine_State' : 0, 'Fuel_Pump_State' : 0,'Brake_Temp_FL' : 0, 'Brake_Temp_FR' : 0, 'Brake_Temp_RL' : 0,'Brake_Temp_RR' : 0}               
print(str(myDict))


