SECRET_KEY = 'wp=w39u1^bl6swsziv%4+oun1ae4mue2!&po*6dez1tfq2u6i-'

INSTALLED_APPS = (
    'pg_array_lookups',
    'tests',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': None,
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
