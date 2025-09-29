def get_kmers(sequence, size=3):
    """
    Convert a nucleotide sequence into k-mers (default: 3-mers).
    Example: 'ATGC' -> 'ATG TGC'
    """
    if not isinstance(sequence, str):
        return ""
    return " ".join([sequence[i:i+size] for i in range(len(sequence) - size + 1)])
