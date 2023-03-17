"""Data Connectors for GPT Index.

This module contains the data connectors for GPT Index. Each connector inherits
from a `BaseReader` class, connects to a data source, and loads Document objects
from that data source.

You may also choose to construct Document objects manually, for instance
in our `Insert How-To Guide <../how_to/insert.html>`_. See below for the API
definition of a Document - the bare minimum is a `text` property.

"""

from llama_index.readers.chroma import ChromaReader
from llama_index.readers.discord_reader import DiscordReader
from llama_index.readers.faiss import FaissReader

# readers
from llama_index.readers.file.base import SimpleDirectoryReader
from llama_index.readers.github_readers.github_repository_reader import (
    GithubRepositoryReader,
)
from llama_index.readers.google_readers.gdocs import GoogleDocsReader
from llama_index.readers.make_com.wrapper import MakeWrapper
from llama_index.readers.mbox import MboxReader
from llama_index.readers.mongo import SimpleMongoReader
from llama_index.readers.notion import NotionPageReader
from llama_index.readers.obsidian import ObsidianReader
from llama_index.readers.pinecone import PineconeReader
from llama_index.readers.qdrant import QdrantReader
from llama_index.readers.schema.base import Document
from llama_index.readers.slack import SlackReader
from llama_index.readers.string_iterable import StringIterableReader
from llama_index.readers.twitter import TwitterTweetReader
from llama_index.readers.weaviate.reader import WeaviateReader
from llama_index.readers.web import (
    BeautifulSoupWebReader,
    RssReader,
    SimpleWebPageReader,
    TrafilaturaWebReader,
)
from llama_index.readers.wikipedia import WikipediaReader
from llama_index.readers.youtube_transcript import YoutubeTranscriptReader

__all__ = [
    "WikipediaReader",
    "YoutubeTranscriptReader",
    "SimpleDirectoryReader",
    "SimpleMongoReader",
    "NotionPageReader",
    "GoogleDocsReader",
    "DiscordReader",
    "SlackReader",
    "WeaviateReader",
    "PineconeReader",
    "QdrantReader",
    "ChromaReader",
    "FaissReader",
    "Document",
    "StringIterableReader",
    "SimpleWebPageReader",
    "BeautifulSoupWebReader",
    "TrafilaturaWebReader",
    "RssReader",
    "MakeWrapper",
    "TwitterTweetReader",
    "ObsidianReader",
    "GithubRepositoryReader",
    "MboxReader",
]
