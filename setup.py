from distutils.core import setup

setup(name='django-jwt-auth',
      version='0.5',
      description='Django JSON Web Token authentication backend',
      author='Jon Hill',
      author_email='jon@jonhill.ca',
      url='https://github.com/jonhillmtl/django-jwt-auth',
      license='MIT',
      packages = ['django_jwt_auth', 'django_jwt_auth.backends'],
      install_requires=[
          "jwcrypto",
          "django",
          "pytest"
      ],
      dependency_links=[
          'git+https://github.com/jonhillmtl/django-jwt-utils',
          'git+https://github.com/jonhillmtl/django-key-gen'
      ]
)
