#!/usr/bin/env python3
"""Download LARGE resistance gene database (50K-100K sequences)"""

import time
from Bio import Entrez, SeqIO
import os

Entrez.email = "mantasharafiq2004@gmail.com"

# Create folder
os.makedirs("large_db", exist_ok=True)

def search_ncbi(query, max_results=5000):
    """Search NCBI with high limit"""
    try:
        handle = Entrez.esearch(db="protein", term=query, retmax=max_results)
        result = Entrez.read(handle)
        handle.close()
        return result["IdList"]
    except Exception as e:
        print(f"  Error: {e}")
        return []

def fetch_proteins(ids, output_file):
    """Fetch protein sequences"""
    if not ids:
        return 0
    try:
        # Fetch in batches of 500
        all_records = []
        batch_size = 500
        for i in range(0, len(ids), batch_size):
            batch = ids[i:i+batch_size]
            handle = Entrez.efetch(db="protein", id=batch, rettype="fasta", retmode="text")
            records = list(SeqIO.parse(handle, "fasta"))
            all_records.extend(records)
            handle.close()
            time.sleep(0.3)
        
        if all_records:
            SeqIO.write(all_records, output_file, "fasta")
        return len(all_records)
    except Exception as e:
        print(f"  Fetch error: {e}")
        return 0

# BROADER QUERIES - More results!
genes = {
    # Beta-lactamases (broad search)
    "beta_lactamase": "beta-lactamase[Title] AND bacteria[Organism] AND srcdb_refseq[PROP]",
    "class_A_beta_lactamase": "class A beta-lactamase[Title] AND bacteria[Organism]",
    "class_B_beta_lactamase": "class B beta-lactamase[Title] AND bacteria[Organism]",
    "class_C_beta_lactamase": "class C beta-lactamase[Title] AND bacteria[Organism]",
    "class_D_beta_lactamase": "class D beta-lactamase[Title] AND bacteria[Organism]",
    
    # Aminoglycoside modifying enzymes
    "aminoglycoside": "aminoglycoside[Title] AND bacteria[Organism] AND srcdb_refseq[PROP]",
    "acetyltransferase": "acetyltransferase[Title] AND antibiotic resistance[Title] AND bacteria[Organism]",
    "phosphotransferase": "phosphotransferase[Title] AND antibiotic resistance[Title] AND bacteria[Organism]",
    "nucleotidyltransferase": "nucleotidyltransferase[Title] AND antibiotic resistance[Title] AND bacteria[Organism]",
    
    # Tetracycline resistance
    "tetracycline_resistance": "tetracycline resistance[Title] AND bacteria[Organism] AND srcdb_refseq[PROP]",
    "tet_gene": "tet[Title] AND bacteria[Organism] AND srcdb_refseq[PROP]",
    
    # Macrolide resistance
    "macrolide_resistance": "macrolide[Title] AND antibiotic resistance[Title] AND bacteria[Organism]",
    "erm_gene": "erm[Title] AND bacteria[Organism] AND srcdb_refseq[PROP]",
    
    # Quinolone resistance
    "quinolone_resistance": "quinolone resistance[Title] AND bacteria[Organism]",
    "qnr_gene": "qnr[Title] AND bacteria[Organism]",
    
    # Glycopeptide resistance
    "glycopeptide_resistance": "glycopeptide resistance[Title] AND bacteria[Organism]",
    "van_gene": "van[Title] AND bacteria[Organism] AND srcdb_refseq[PROP]",
    
    # Sulfonamide resistance
    "sulfonamide_resistance": "sulfonamide[Title] AND antibiotic resistance[Title] AND bacteria[Organism]",
    
    # MLS resistance
    "MLS_resistance": "MLS resistance[Title] AND bacteria[Organism]",
    
    # MRSA
    "MRSA": "MRSA[Title] AND Staphylococcus aureus[Organism]",
    "mec_gene": "mec[Title] AND Staphylococcus[Organism] AND srcdb_refseq[PROP]",
    
    # Carbapenem resistance
    "carbapenemase": "carbapenemase[Title] AND bacteria[Organism]",
    "carbapenem_resistance": "carbapenem resistance[Title] AND bacteria[Organism]",
    
    # Multi-drug resistance
    "multidrug_efflux": "multidrug efflux[Title] AND bacteria[Organism]",
    "multidrug_transporter": "multidrug transporter[Title] AND bacteria[Organism]",
    "RND_family": "RND efflux pump[Title] AND bacteria[Organism]",
    
    # Colistin resistance
    "colistin_resistance": "colistin resistance[Title] AND bacteria[Organism]",
    "mcr_gene": "mcr[Title] AND bacteria[Organism]",
    
    # Chloramphenicol resistance
    "chloramphenicol": "chloramphenicol[Title] AND antibiotic resistance[Title] AND bacteria[Organism]",
    
    # Rifampicin resistance
    "rifampicin_resistance": "rifampicin resistance[Title] AND bacteria[Organism]",
    
    # Fosfomycin resistance
    "fosfomycin_resistance": "fosfomycin resistance[Title] AND bacteria[Organism]",
    
    # Linezolid resistance
    "linezolid_resistance": "linezolid resistance[Title] AND bacteria[Organism]",
    
    # Extended spectrum
    "ESBL": "extended spectrum beta-lactamase[Title] AND bacteria[Organism]",
    
    # Metal resistance (linked to antibiotics)
    "mercury_resistance": "mercury resistance[Title] AND bacteria[Organism]",
    
    # Mobile genetic elements
    "integron": "integron[Title] AND antibiotic resistance[Title] AND bacteria[Organism]",
    "transposase": "transposase[Title] AND antibiotic resistance[Title] AND bacteria[Organism]",
}

print("="*60)
print("DOWNLOADING LARGE RESISTANCE DATABASE")
print("Target: 50,000 - 100,000 sequences")
print("="*60)

total_sequences = 0
count = 0

for name, query in genes.items():
    print(f"\n[{count+1}/{len(genes)}] {name}")
    print(f"  Query: {query[:50]}...")
    
    ids = search_ncbi(query, max_results=5000)
    print(f"  Found: {len(ids)} IDs")
    
    if ids:
        seq_count = fetch_proteins(ids, f"large_db/{name}.fasta")
        print(f"  Saved: {seq_count} sequences")
        total_sequences += seq_count
    else:
        print(f"  ✗ No sequences")
    
    count += 1
    print(f"  Running total: {total_sequences} sequences")
    
    time.sleep(1)

print("\n" + "="*60)
print(f"FINAL: {total_sequences} sequences downloaded!")
print("="*60)