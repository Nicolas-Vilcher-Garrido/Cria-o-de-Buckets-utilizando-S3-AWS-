import boto3

# Cria uma sessão com o S3
s3 = boto3.client('s3')

# Lista todos os buckets existentes
response = s3.list_buckets()
print("Buckets existentes:")
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

# Solicita ao usuário um nome para o novo bucket
bucket_name = input("Digite o nome do bucket que deseja criar: ")

# Verifica se o bucket já existe
existing_buckets = [bucket['Name'] for bucket in response['Buckets']]
if bucket_name in existing_buckets:
    print(f'O bucket {bucket_name} já existe e é de sua propriedade.')
else:
    # Tenta criar um novo bucket
    try:
        s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
        print(f'Bucket {bucket_name} criado com sucesso.')
    except Exception as e:
        print(f'Erro ao criar o bucket: {e}')

# Faz upload de um arquivo (substitua pelo caminho correto)
file_path = 'C:/Users/nicol/OneDrive/Desktop/aws/arquivo.txt'  # Ajuste o caminho e o nome do arquivo
try:
    s3.upload_file(file_path, bucket_name, 'arquivo.txt')
    print('Arquivo enviado para o bucket.')
except Exception as e:
    print(f'Erro ao enviar o arquivo: {e}')

# Lista os arquivos no bucket
response = s3.list_objects_v2(Bucket=bucket_name)
print(f'Arquivos no bucket {bucket_name}:')
if 'Contents' in response:
    for obj in response['Contents']:
        print(f'  {obj["Key"]}')
else:
    print('Nenhum arquivo encontrado no bucket.')
