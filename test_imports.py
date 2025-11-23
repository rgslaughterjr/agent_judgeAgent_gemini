
try:
    from langchain.retrievers.multi_query import MultiQueryRetriever
    print("SUCCESS: from langchain.retrievers.multi_query import MultiQueryRetriever")
except ImportError as e:
    print(f"FAILED: from langchain.retrievers.multi_query import MultiQueryRetriever ({e})")

try:
    from langchain.retrievers import MultiQueryRetriever
    print("SUCCESS: from langchain.retrievers import MultiQueryRetriever")
except ImportError as e:
    print(f"FAILED: from langchain.retrievers import MultiQueryRetriever ({e})")

try:
    from langchain_community.retrievers import MultiQueryRetriever
    print("SUCCESS: from langchain_community.retrievers import MultiQueryRetriever")
except ImportError as e:
    print(f"FAILED: from langchain_community.retrievers import MultiQueryRetriever ({e})")
