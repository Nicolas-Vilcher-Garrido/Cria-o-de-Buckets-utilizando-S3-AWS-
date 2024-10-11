Este código Python utiliza a biblioteca boto3 para interagir com o serviço Amazon S3, permitindo o gerenciamento de buckets e arquivos na nuvem. Abaixo está um resumo das principais funcionalidades implementadas:

Funcionalidades
Listagem de Buckets:

O código começa criando uma sessão com o serviço S3 e lista todos os buckets existentes na conta AWS do usuário. Isso permite que o usuário tenha uma visão clara dos buckets que já foram criados.
Criação de Buckets:

O usuário é solicitado a inserir um nome para o novo bucket. O código verifica se o nome fornecido já está em uso na conta. Se o bucket já existir, uma mensagem é exibida informando que o bucket já é de sua propriedade. Caso contrário, o código tenta criar o novo bucket na região us-east-2. Se a criação for bem-sucedida, uma mensagem de confirmação é exibida; caso 
contrário, um erro é impresso.

Upload de Arquivos:

Após a criação ou verificação do bucket, o código faz o upload de um arquivo especificado (neste caso, arquivo.txt) para o bucket criado ou selecionado. O caminho do arquivo deve ser ajustado conforme necessário. Se o upload for bem-sucedido, uma mensagem de confirmação é exibida; caso contrário, um erro é impresso.
Listagem de Arquivos no Bucket:

Finalmente, o código lista todos os arquivos armazenados no bucket. Se não houver arquivos no bucket, uma mensagem informando que nenhum arquivo foi encontrado é exibida.
