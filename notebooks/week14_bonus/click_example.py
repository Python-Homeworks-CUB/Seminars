import click

@click.command()
@click.option('--name', prompt='Your name', help='The name of the user.')
@click.option('--age', prompt='Your age', help='The age of the user.', type=int)
def greet(name, age):
    click.echo(f"Hello, {name}!")
    click.echo(f"You are {age} years old.")

if __name__ == '__main__':
    greet()
