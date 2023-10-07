# AwaDB - AI Native Database for embedding vectors

Easily Use - No boring database schema definition. No need to pay attention to vector indexing details.  

Realtime Search - Lock free realtime index keeps new data fresh with millisecond level latency. No wait no manual operation.  

Stability - AwaDB builds upon over 4 years experience at JD.com running production workloads at scale using a system called [Vearch](https://github.com/vearch/vearch), combined with best-of-breed ideas and practices from the community.

## Install
```bash
# 1. Pull AwaDB docker image
docker pull ljeagle/awadb:v0.08

# 2. Run AwaDB Server
docker run -itd -p 50005:50005 ljeagle/awadb:v0.08

# 3. Install AwaDB Client
pip3 install awadb-client
```

## Quick start using AwaDB:

### A simple example show usage
```bash
# Import the package and module
from awadb.client import Awa

# Initialize awadb client
client = Awa()

# Add dict with vector to table 'example1'
client.add("example1", {'name':'david', 'feature':[1.3, 2.5, 1.9]})
client.add("example1", {'name':'jim', 'feature':[1.1, 1.4, 2.3]})

# Search
results = client.search("example1", [1.0, 2.0, 3.0])

# Output results
print(results)

# '_id' is the primary key of each document
# It can be specified clearly when adding documents
# Here no field '_id' is specified, it is generated by the awadb server 
db_name: "default"
table_name: "example1"
results {
  total: 2
  msg: "Success"
  result_items {
    score: 0.860000074
    fields {
      name: "_id" 
      value: "64ddb69d-6038-4311-9118-605686d758d9"
    }
    fields {
      name: "name"
      value: "jim"
    }
  }
  result_items {
    score: 1.55
    fields {
      name: "_id"
      value: "f9f3035b-faaf-48d4-a947-801416c005b3"
    }
    fields {
      name: "name"
      value: "david"
    }
  }
}
result_code: SUCCESS
```

More detailed sdk usage you can read [here](https://github.com/awa-ai/awadb/blob/main/clients/awadb/client.py)

More detailed quick start examples you can find [here](https://github.com/awa-ai/awadb/blob/main/tests/test_awadb_client.py)


## Semantic Search
You can also directly use awadb to do the text semantic retrieval  
Here the text is embedded by SentenceTransformer which is supported by [Hugging Face](https://huggingface.co)  
Another example for 'pip3 install awadb', no AwaDB server is needed.
```bash
import awadb
# 1. Initialize awadb client!
awadb_client = awadb.Client()

# 2. Create table
awadb_client.Create("test_llm1") 

# 3. Add sentences, the sentence is embedded with SentenceTransformer by default
#    You can also embed the sentences all by yourself with OpenAI or other LLMs
awadb_client.Add([{'embedding_text':'The man is happy'}, {'source' : 'pic1'}])
awadb_client.Add([{'embedding_text':'The man is very happy'}, {'source' : 'pic2'}])
awadb_client.Add([{'embedding_text':'The cat is happy'}, {'source' : 'pic3'}])
awadb_client.Add([{'embedding_text':'The man is eating'}, {'source':'pic4'}])

# 4. Search the most Top3 sentences by the specified query
query = "The man is happy"
results = awadb_client.Search(query, 3)

# Output the results
print(results)
```

## What are the Embeddings?

Any unstructured data(image/text/audio/video) can be transferred to vectors which are generally understanded by computers through AI(LLMs or other deep neural networks).   
  
For example, "The man is happy"-this sentence can be transferred to a 384-dimension vector(a list of numbers `[0.23, 1.98, ....]`) by SentenceTransformer language model. This process is called embedding.

More detailed information about embeddings can be read from [OpenAI](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings)

Awadb uses [Sentence Transformers](https://huggingface.co/sentence-transformers) to embed the sentence by default, while you can also use OpenAI or other LLMs to do the embeddings according to your needs.


## Combined with LLMs(here use LLaMa and ChatGLM) By LangChain
Examples of combining LLaMa or quantized Alpaca with llama.cpp to do local knowledge database please see [here](./examples/llama.cpp)  
Examples of combining ChatGLM to do local knowledge database please see [here](./examples/chatglm)  


## Get involved

- [Issues and PR](https://github.com/awa-ai/awadb/issues)  
- [Roadmap and Contribution](https://github.com/awa-ai/awadb/blob/main/ROADMAP.md)


## License

[Apache 2.0](./LICENSE)


## Community

Join the AwaDB community to share any problem, suggestion, or discussion with us:

- [Discord](https://discord.gg/GP7QxRrDjB)
- [Slack](https://awadbhq.slack.com)
- [Reddit](https://www.reddit.com/r/Awadb/)
