import os
import sys
from dotenv import load_dotenv, find_dotenv


class Utils:
    def __init__(self) -> None:
        pass

    def create_dlai_index_name(self, index_name):
        openai_key = ""

        if self.is_colab(): # Google Colab
            from google.colab import userdata
            openai_key = userdata.get("OPENAI_API_KEY")
        else:  # jupyter notebook
            openai_key = os.getenv("OPENAI_API_KEY")
        
        return f'{index_name}-{openai_key[-36:].lower().replace("_", "-")}'

    def is_colab(self):
        return "google.colab" in sys.modules
    
    def get_openai_api_key(self):
        _ = load_dotenv(find_dotenv())

        return os.getenv("OPENAI_API_KEY")
    
    def get_pinecone_api_key(self):
        _ = load_dotenv(find_dotenv())

        return os.getenv("PINECONE_API_KEY")
