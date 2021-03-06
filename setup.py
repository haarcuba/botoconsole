from setuptools import setup, find_packages

README = 'a console for easily using AWS with boto3'

requires = [ 'ipython >= 5.2.2', 'boto3', 'myconsole' ]

setup(name='aws-console',
      version='0.3.0',
      description=README,
      long_description=README,
      url='https://github.com/haarcuba/aws_console',
      classifiers=[
          "Programming Language :: Python",
      ],
      author='Yoav Kleinberger',
      author_email='haarcuba@gmail.com',
      packages=find_packages(),
      keywords='AWS, boto, amazon',
      entry_points = {
          'console_scripts': [ 'aws-console = aws_console.main:main',
                               'aws-inspect = aws_console.inspect:main' ]

      },
      zip_safe=False,
      install_requires=requires,
      )
