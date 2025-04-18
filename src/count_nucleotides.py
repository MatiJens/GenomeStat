import os

from Bio import SeqIO


def count_nucleotides(file_name, file_dir="../data"):
    """Count nucleotides from specific DNA

    Args:
        file_name(str): name of file with DNA sequence
        file_dir(str): direction of file with DNA sequence (default: ../data)

    Returns:
        Counts: quantity of each nucleotide

    Raises:
        Exception: If the opening file failed
    """
    if not file_name.endswith((".fasta", ".fa", ".txt")):
        file_path = os.path.join(file_dir, f"{file_name}.fasta")
    else:
        file_path = os.path.join(file_dir, f"{file_name}")

    try:
        record = next(SeqIO.parse(file_path, "fasta"))
        seq = str(record.seq).upper()

        counts = {
            "A": seq.count("A"),
            "T": seq.count("T"),
            "C": seq.count("C"),
            "G": seq.count("G")
        }

    except Exception as e:
        print(f"Error during reading file: {str(e)}")
        counts = {"A": 0, "T": 0, "G": 0, "C": 0}

    return counts
