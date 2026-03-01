# Comprehensive Antibiotic Resistance Gene Collection 🧬

## 📊 Overview
This repository contains a comprehensive collection of **antibiotic resistance genes** downloaded from **NCBI RefSeq** for research and bioinformatics analysis purposes.

## 🔢 Statistics
| Metric | Value |
|--------|-------|
| Total Sequences | 48,000+ |
| Gene Families | 30+ |
| Resistance Classes | 15+ |
| Data Source | [NCBI RefSeq](https://www.ncbi.nlm.nih.gov/refseq/) |


## 🦠 Resistance Genes Included

### β-Lactamases
| Gene | Resistance To |
|------|---------------|
| blaTEM | Penicillins, Cephalosporins |
| blaCTX-M | Extended-spectrum Cephalosporins |
| blaSHV | Cephalosporins |
| blaOXA | Carbapenems, Cephalosporins |
| blaNDM | Carbapenems (all) |
| blaKPC | Carbapenems |
| blaVIM | Carbapenems |
| blaIMP | Carbapenems |

### Other Resistance Genes
| Gene | Resistance To |
|------|---------------|
| mecA, mecC | Methicillin (MRSA) |
| vanA, vanB | Vancomycin |
| tetM, tetA | Tetracyclines |
| erm, mef | Macrolides |
| qnr | Quinolones |
| mcr | Colistin |
| aadA | Aminoglycosides |

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/itimantasha/amr-project.git
cd amr-project

# Create BLAST database
makeblastdb -in all_resistance_genes.fasta -dbtype prot -title AMR_DB

# Search for resistance genes
blastp -query your_sequence.fasta -db all_resistance_genes.fasta -out results.txt

# Find specific gene
grep -i "blaTEM" all_resistance_genes.fasta
# Update genes
python download_large_db.py

# Combine all into single file
python combine_genes.py
```

🎯 Use Cases
✅ BLAST against known resistance genes

✅ Gene detection in bacterial genomes

✅ Phylogenetic analysis of resistance genes

✅ Comparative genomics studies

✅ Machine learning training data

✅ Drug discovery research


###📜 License
This database is distributed under the Open Database License (ODbL).

🙏 Acknowledgments
NCBI RefSeq

CARD Database

Biopython
