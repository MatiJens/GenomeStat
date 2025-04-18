from fasta_download import fasta_download
from src.count_nucleotides import count_nucleotides

fasta_download("NZ_CP186931.1")
counts = count_nucleotides("NZ_CP186931.1")
print(counts)