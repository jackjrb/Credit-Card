# Derivando da imagem oficial do MySQL
FROM mysql:5.7

# Adicionando os scripts SQL para serem executados na criacao do banco
COPY ./db/ /docker-entrypoint-initdb.d/