"""
input source:
- file
    - markdown
    - html
- website

output type:
- epub
- pdf
"""

import markdown2
from ebooklib import epub
from typing import Literal, Union, Annotated, Generator, Tuple
from pydantic import BaseModel, Field, Discriminator, Tag
import os
from typing import NewType
from doc_crawl.darkmode import darkmode_css


class FileInput(BaseModel):
    folder_path: str = Field(
        ..., description="flat file path with markdown or html content"
    )
    file_type: Literal["markdown", "html"]


class WebsiteInput(BaseModel):
    url: str = Field(..., description="root url of the website to crawl")
    file_type: Literal["html"]


class PdfOutput(BaseModel):
    folder_path: str


class EpubOutput(BaseModel):
    book_path: str
    book_name: str
    author: str = "Author"


def get_discriminator_value(obj):
    if "folder_path" in obj:
        return "file"
    elif "url" in obj:
        return "website"
    else:
        raise ValueError("Invalid input")


class CrawlerConfig(BaseModel):
    input: Annotated[
        Union[
            Annotated[FileInput, Tag("file")],
            Annotated[WebsiteInput, Tag("website")],
        ],
        Discriminator(get_discriminator_value),
    ]
    output: Annotated[
        Union[
            Annotated[PdfOutput, Tag("pdf")],
            Annotated[EpubOutput, Tag("epub")],
        ],
        Discriminator(lambda obj: obj["book_path"].split(".")[-1]),
    ]


HtmlContent = NewType("HtmlContent", str)


class Converter:
    """
    Example Config:
        config = {
        "input": {
            "folder_path": "md",
            "file_type": "markdown",
        },
        "output": {
            "book_path": "epubook/mybook.epub",
            "book_name": "book_name",
        },
    }
    """

    def __init__(self, config: CrawlerConfig):
        self.config = config

    def convert(self):
        # create html content from input source
        match self.config.input:
            case FileInput():
                contents = self.read_folder(self.config.input.folder_path)
            case WebsiteInput():
                contents = self.read_website(self.config.input.url)

        # write to output type
        match self.config.output:
            case PdfOutput():
                self.write_pdf(contents)
            case EpubOutput():
                self.write_epub(contents)

    def read_folder(
        self, folder_path: str
    ) -> Generator[Tuple[HtmlContent, str], None, None]:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content: HtmlContent = f.read()
                    if self.config.input.file_type == "markdown":
                        content: HtmlContent = markdown2.markdown(content)
                    yield content, file

    def write_epub(self, contents: Generator[Tuple[HtmlContent, str], None, None]):
        # init epub book
        book = epub.EpubBook()
        book.set_identifier("id123456")
        book.set_title(self.config.output.book_name)
        book.set_language("en")

        # add metadata
        book.add_author(self.config.output.author)

        # create chapter
        for content, file in contents:
            chapter = epub.EpubHtml(title=file, file_name=file, lang="en")
            chapter.content = content
            book.add_item(chapter)
            book.toc.append(chapter)

        # add default NCX and Nav file
        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())

        # define CSS style in dark mode
        nav_css = epub.EpubItem(
            uid="style_nav",
            file_name="style/nav.css",
            media_type="text/css",
            content=darkmode_css,
        )

        # add CSS file
        book.add_item(nav_css)

        # spine
        book.spine = ["nav"] + book.toc

        # write to the file
        epub.write_epub(self.config.output.book_path, book)


if __name__ == "__main__":
    # go to parent folder of this file
    os.chdir(os.path.dirname(os.path.dirname(__file__)))
    
    config = {
        "input": {
            "folder_path": "artifacts/md",
            "file_type": "markdown",
        },
        "output": {
            "book_path": "artifacts/epubook/mybook_1.epub",
            "book_name": "book_name",
        },
    }

    config = CrawlerConfig(**config)
    converter = Converter(config)
    converter.convert()
