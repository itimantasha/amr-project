# Combine all into one file
from Bio import SeqIO

files = ["beta_lactamase.fasta", "blaTEM.fasta", "blaCTX-M.fasta", 
         "mecA.fasta", "KPC.fasta", "NDM-1.fasta"]

all_records = []
for f in files:
    try:
        records = list(SeqIO.parse(f, "fasta"))
        all_records.extend(records)
        print(f"{f}: {len(records)} sequences")
    except:
        print(f"{f}: NOT FOUND")

SeqIO.write(all_records, "all_resistance_genes.fasta", "fasta")
print(f"\nTotal: {len(all_records)} sequences saved to all_resistance_genes.fasta")