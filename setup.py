from distutils.core import setup

setup(name='django-jwt-auth',
      version='0.1',
      description='Django JSON Web Token authentication backend',
      author='Jon Hill',
      author_email='jon@jonhill.ca',
      url='',
      license='MIT',
      packages = ['django_jwt_auth', 'django_jwt_auth.utils', 'django_jwt_auth.backends'],
      install_requires=[
          "jwcrypto",
          "django",
          "pytest"
      ],
)
