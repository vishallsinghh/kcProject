#AWS S3 Settings

AWS_ACCESS_KEY_ID = 'AKIAZBXKKADJRC757I3A'
AWS_SECRET_ACCESS_KEY = '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'
AWS_S3_REGION_NAME = "ap-south-1"


AWS_STORAGE_BUCKET_NAME = 'techneith-website'
AWS_S3_FILE_OVERWRITE = True
S3_USE_SIGV4 = True
AWS_QUERYSTRING_AUTH = False
AWS_DEFAULT_ACL = None
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# # s3 static settings
# STATIC_LOCATION = 'static'
# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# # s3 public media settings
# PUBLIC_MEDIA_LOCATION = 'media'
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
# DEFAULT_FILE_STORAGE = 'techneith.aws.utils.MediaRootS3BotoStorage'
