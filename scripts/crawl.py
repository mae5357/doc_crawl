from doc_crawl.converter import CrawlerConfig, Converter
import click
import os

# assume paths are from the parent directory of this file
os.chdir(os.path.dirname(os.path.dirname(__file__)))


@click.command()
@click.option(
    "--folder_path", type=str, help="flat file path with markdown or html content"
)
@click.option(
    "--file_type", type=click.Choice(["markdown", "html"]), help="type of file content"
)
@click.option("--book_path", type=str, help="path to save the book")
@click.option("--book_name", type=str, help="name of the book")
def convert(folder_path, file_type, book_path, book_name):
    config = {
        "input": {
            "folder_path": folder_path,
            "file_type": file_type,
        },
        "output": {
            "book_path": book_path,
            "book_name": book_name,
        },
    }
    config = CrawlerConfig(**config)
    converter = Converter(config)
    converter.convert()


if __name__ == "__main__":
    convert()
