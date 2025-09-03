# YouTube Transcript QA using LangChain

A lightweight Python application that enables question answering over YouTube video transcripts using **LangChain** and OpenAI.

##  Overview

This project demonstrates how to:
1. Load a YouTube video transcript using LangChain's document loading tools.  
2. Break the transcript into manageable chunks and embed them using OpenAI embeddings.  
3. Store and query those embeddings with a vector store.  
4. Answer user questions based solely on the transcript content.

LangChain components like YouTube loaders, text splitters, retrievers, and vector stores are leveraged to build an efficient retrieval-augmented question-answering (QA) system.

##  Features

- **Transcript Retrieval**: Load transcripts directly via YouTube URL using LangChain’s `YoutubeLoader`.  
  :contentReference[oaicite:1]{index=1}
- **Chunking**: Process transcripts in overlapping fragments ideal for embedding and retrieval.
- **Vector Database**: Store audio chunks as embeddings with FAISS or other vector stores.
- **QA System**: Retrieve relevant transcript segments for user queries and generate accurate answers with language models.
- **Graceful Handling**: Provide fallback responses like “I don’t know” when relevant transcript segments aren't found.

##  Requirements

- `python >= 3.8`
- `langchain` (LangChain framework)  
- `langchain_community` (for YouTube transcript loader)  
- `openai` or `langchain_openai` (for embeddings & responses)  
- `faiss` (for vector storage)  
- `python-dotenv` (for reading environment variables)

You can install dependencies via:

```bash
pip install langchain langchain_community openai faiss-cpu python-dotenv
