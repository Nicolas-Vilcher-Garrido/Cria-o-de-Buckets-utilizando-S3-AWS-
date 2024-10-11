Este projeto tem como objetivo utilizar a API do Amazon S3 para gerenciar buckets e arquivos relacionados à análise do mercado de criptomoedas. Através do uso da biblioteca boto3, o código permite a criação de buckets no S3, o upload de arquivos e a listagem de buckets e arquivos existentes. É uma ferramenta útil para quem deseja armazenar e gerenciar dados de forma eficiente na nuvem.

Funcionalidades
Listagem de Buckets: O código começa listando todos os buckets existentes no S3, permitindo que o usuário tenha uma visão geral dos dados já armazenados.

Criação de Buckets: O usuário pode criar um novo bucket fornecendo um nome via input. O código verifica se o bucket já existe e informa o usuário, evitando a criação de buckets duplicados.

Upload de Arquivos: Permite o upload de um arquivo especificado para o bucket criado ou selecionado, facilitando o gerenciamento de dados.

Listagem de Arquivos: Após o upload, o código lista todos os arquivos presentes no bucket, proporcionando uma visão clara do conteúdo armazenado.

Tecnologias Utilizadas
Python: Linguagem de programação utilizada para desenvolver o código.
boto3: Biblioteca Python para interagir com os serviços da AWS, incluindo o Amazon S3.
