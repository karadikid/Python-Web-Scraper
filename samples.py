Sample Commands to run

Click tutorial for reference https://click.palletsprojects.com/en/7.x/  REMOVE FROM FINAL
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()

# def some_func():
#     print 'in test 1, unproductive'

# if __name__ == '__main__':
#     # test1.py executed as script
#     # do something
#     some_func()

# import test1

# def service_func():
#     print 'service func'

# if __name__ == '__main__':
#     # service.py executed as script
#     # do something
#     service_func()
#     test1.some_func()

# # Python 3 exec script
# exec(open("test2.py").read())


# import subprocess

# subprocess.call("test1.py", shell=True)

# #!/usr/bin/env python
# # coding: utf-8

# import runpy

# runpy.run_path(path_name='script-01.py')