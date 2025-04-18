import time
from Bio import Entrez
import os
from dotenv import load_dotenv

load_dotenv()

Entrez.email = "mateuszjens14@gmail.com"
Entrez.api_key = os.getenv("NCBI_API_KEY")

def fasta_download(accession, file_dir="../data", file_name=None):
    """Download FASTA sequence from NCBI Nucleotide database.

    Args:
        accession(str): NCBI nucleotide accession number
        file_dir(str): output file direction (default: ../data)
        file_name(str): output file name (default: None)

    Returns:
        bool: True if the download is successful, False if an error occurs

    Raises:
        Exception: If the NCBI API request fails
    """
    try:
        # Create output file direction if it doesn't exist
        os.makedirs(file_dir, exist_ok=True)

        # Download FASTA file from nucleotide database
        handle = Entrez.efetch(db="nucleotide", id=accession, rettype="fasta", retmode="text")
        fasta_data = handle.read()
        handle.close()

        # Set default file name if it's not provided
        if not file_name:
            file_name = f"{accession}.fasta"

        # Save FASTA file to directory
        file_path = os.path.join(file_dir, file_name)
        with open(file_path, "w") as f:
            f.write(fasta_data)

        print(f"{accession} downloaded to {file_path}")

    except Exception as e:
        print(f"Error during downloading {accession}: {str(e)}")

    finally:
        # NCBI API rate limits
        time.sleep(0.5)
