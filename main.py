from dotenv import load_dotenv
from app.domain.data_repository import DataRepository
from app.domain.data import Data
import os 

def main():
    ok = load_dotenv()
    if not ok:
        print("Failed to load environment variables from .env file.")

    if not os.getenv('GOOGLE_API_KEY'):
        print("GOOGLE_API_KEY is not set in the environment variables.")

    data_repository = DataRepository()
    data = Data()

    embedding = False

    if embedding:
        print("Embedding data...")
        data.embedData(data_repository)


    generated_data = data.generate()

    print("Generated Data:")
    print(generated_data)



if __name__ == '__main__':
    main()
