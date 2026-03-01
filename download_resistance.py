#!/usr/bin/env python3
"""Download multiple resistance genes from NCBI"""

import time
from Bio import Entrez, SeqIO

Entrez.email = "mantasharafiq2004@gmail.com"

def search_ncbi(query, max_results=50):
    handle = Entrez.esearch(db="protein", term=query, retmax=max_results)
    result = Entrez.read(handle)
    handle.close()
    return result["IdList"]

def fetch_proteins(ids, output_file):
    if not ids:
        return 0
    handle = Entrez.efetch(db="protein", id=ids, rettype="fasta", retmode="text")
    records = list(SeqIO.parse(handle, "fasta"))
    SeqIO.write(records, output_file, "fasta")
    handle.close()
    return len(records)

# Resistance genes to download
genes = {
    "blaTEM": "blaTEM[Title] AND bacteria[Organism]",
    "blaCTX-M": "blaCTX-M[Title] AND bacteria[Organism]", 
    "mecA": "mecA[Title] AND Staphylococcus[Organism]",
    "KPC": "KPC[Title] AND Enterobacteriaceae[Organism]",
    "NDM-1": "NDM-1[Title] AND bacteria[Organism]",
}

print("Downloading resistance genes from NCBI...")
print("="*50)

for name, query in genes.items():
    print(f"\n[{name}] Searching...")
    ids = search_ncbi(query)
    print(f"  Found {len(ids)} sequences")
    
    count = fetch_proteins(ids, f"{name}.fasta")
    print(f"  Saved {count} to {name}.fasta")
    
    time.sleep(1)  # Be nice to NCBI

print("\n" + "="*50)
print("DONE! Check your .fasta files")