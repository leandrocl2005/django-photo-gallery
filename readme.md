- Logue na sua conta da amazon
- Procure por s3
- Crie um bucket
-- Dê um nome para o bucket
-- Desbloqueie acesso público
-- Deixe o restante das informações default
- Após criar o bucket, entre no mesmo e altere as permissões.
```json
{
    "Version": "2008-10-17",
    "Statement": [
        {
            "Sid": "AllowPublicRead",
            "Effect": "Allow",
            "Principal": {
                "AWS": "*"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::yourbucketname/*"
        }
    ]
}
```
- Vá em IAM user
- Clique em adicionar usuário
- Dê o nome e marque *Acesso programático*
- Vá em anexar políticas existentes
- Escolha AmazonS3FullAcess
- Pule o passo *tags*
- Clique em criar usuário e pronto.

- Instale boto3: `pip install boto3`
- Instale storage: `pip install django-storages`

- Adicione *storages* em *INSTALED_APPS*.

- Em *settings.py*:
```python
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = 'YOUR_AWS_ACCESS_KEYID'
AWS_SECRET_ACCESS_KEY = 'YOUR_SECRET_ACCESS_KEY'
AWS_STORAGE_BUCKET_NAME = 'YOUR_AWS_STORAGE_BUCKET_NAME'
AWS_QUERYSTRING_AUTH = False
```