#!/usr/bin/env python3
"""Download multiple resistance genes from NCBI"""

from Bio import Entrez, SeqIO

# IMPORTANT - CHANGE THIS
Entrez.email = "mantasharafiq2004@gmail.com"

def search_ncbi(query, db="protein", max_results=50):
    """Search NCBI"""
    handle = Entrez.esearch(db=db, term=query, retmax=max_results)
    result = Entrez.read(handle)
    handle.close()
    return result["IdList"]

def fetch_proteins(ids, output_file):
    """Fetch protein sequences"""
    if not ids:
        print(f"  No sequences found for {output_file}")
        return 0
    handle = Entrez.efetch(db="protein", id=ids, rettype="fasta", retmode="text")
    records = list(SeqIO.parse(handle, "fasta"))
    SeqIO.write(records, output_file, "fasta")
    handle.close()
    return len(records)

# List of resistance genes to download
queries = {
    "blaTEM": "blaTEM[Title] AND bacteria[Organism]",
    "blaCTX-M": "blaCTX-M[Title] AND bacteria[Organism]", 
    "mecA": "mecA[Title] AND Staphylococcus[Organism]",
    "KPC": "KPC[Title] AND Enterobacteriaceae[Organism]",
    "NDM-1": "NDM-1[Title] AND bacteria[Organism]",
}

print("="*50)
print("Downloading Multiple Resistance Genes from NCBI")
print("="*50)

# Download each gene type
for filename, query in queries.items():
    print(f"\n[{filename}] Searching: {query}")
    
    ids = search_ncbi(query, max_results=50)
    print(f"  Found: {len(ids)} sequences")
    
    count = fetch_proteins(ids, f"{filename}.fasta")
    print(f"  Saved: {count} sequences to {filename}.fasta")

print("\n" + "="*50)
print("DOWNLOAD COMPLETE!")
print("="*50)