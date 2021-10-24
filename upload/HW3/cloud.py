import boto3
s3 = boto3.resource('s3', 
    aws_access_key_id='AKIAYQ6YHT4IHYVAJGOV', 
    aws_secret_access_key='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' 
) 

bucket = s3.Bucket("meiser-bucket") 

dyndb = boto3.resource('dynamodb', 
    region_name='us-east-2', 
    aws_access_key_id='AKIAYQ6YHT4IHYVAJGOV', 
    aws_secret_access_key='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' 
) 

table = dyndb.Table("DataTable") 

response = table.get_item( 
    Key={ 
        'PartitionKey': '1', 
        'RowKey': '-1' 
    } 
) 
item = response['Item'] 
print(item) 