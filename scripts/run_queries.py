import click
from lib.models.author import Author
from lib.models.magazine import Magazine

@click.group()
def cli():
    pass

@cli.command()
@click.argument('author_id', type=int)
def author_articles(author_id):
    author = Author.find_by_id(author_id)
    if author:
        for article in author.articles():
            print(f"- {article.title} (Magazine: {article.magazine.name})")
    else:
        print("Author not found.")

@cli.command()
def top_publisher():
    mag = Magazine.top_publisher()
    if mag:
        print(f"Top publisher: {mag.name} (Category: {mag.category})")
    else:
        print("No magazines found.")

if __name__ == "__main__":
    cli()
