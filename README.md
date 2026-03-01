Comprehensive Antibiotic Resistance Gene Collection
Database Size
License
Platform

📊 Overview
This repository contains a comprehensive collection of antibiotic resistance genes downloaded from NCBI RefSeq for research and bioinformatics analysis purposes.

🔢 Statistics
Metric

Value

Total Sequences

48,000+

Gene Families

30+

Resistance Classes

15+

Data Source

NCBI RefSeq

📁 Repository Structure

Copy code
amr-project/
├── 📂 large_db/              # Main gene database (48K+ sequences)
│   ├── beta_lactamase.fasta
│   ├── blaTEM.fasta
│   ├── blaCTX-M.fasta
│   ├── blaNDM.fasta
│   ├── blaKPC.fasta
│   ├── mecA.fasta
│   ├── vanA.fasta
│   ├── tetM.fasta
│   └── ... (more genes)
│
├── 📄 all_resistance_genes.fasta    # Combined database
├── 📄 beta_lactamase.fasta          # Individual gene files
├── 📄 blaTEM.fasta
├── 📄 blaCTX-M.fasta
├── 📄 KPC.fasta
├── 📄 mecA.fasta
├── 📄 NDM-1.fasta
│
├── 📜 download_large_db.py           # Download script
├── 📜 download_ncbi.py              # NCBI fetcher
├── 📜 combine_genes.py              # Merge utility
│
└── 📖 README.md
🦠 Resistance Genes Included
β-Lactamases
Gene

Resistance To

blaTEM

Penicillins, Cephalosporins

blaCTX-M

Extended-spectrum Cephalosporins

blaSHV

Cephalosporins

blaOXA

Carbapenems, Cephalosporins

blaNDM

Carbapenems (all)

blaKPC

Carbapenems

blaVIM

Carbapenems

blaIMP

Carbapenems

Other Resistance Genes
Gene

Resistance To

mecA, mecC

Methicillin (MRSA)

vanA, vanB

Vancomycin

tetM, tetA

Tetracyclines

erm, mef

Macrolides

qnr

Quinolones

mcr

Colistin

aadA

Aminoglycosides

🚀 Quick Start
1. Clone the Repository
bash

Copy code
git clone https://github.com/itimantasha/amr-project.git
cd amr-project
2. Use for BLAST Analysis
bash

Copy code
# Create BLAST database
makeblastdb -in all_resistance_genes.fasta -dbtype prot -title AMR_DB

# Search for resistance genes
blastp -query your_sequence.fasta -db all_resistance_genes.fasta -out results.txt
3. Search for Specific Genes
bash

Copy code
# Find specific gene
grep -i "blaTEM" all_resistance_genes.fasta
📥 Download More Data
To update or expand the database:

bash

Copy code
# Update genes
python download_large_db.py

# Combine all into single file
python combine_genes.py
🎯 Use Cases
✅ BLAST against known resistance genes
✅ Gene detection in bacterial genomes
✅ Phylogenetic analysis of resistance genes
✅ Comparative genomics studies
✅ Machine learning training data
✅ Drug discovery research
📜 License
This database is distributed under the Open Database License (ODbL).

Attribution:

Data Source: NCBI RefSeq
Database: CARD
👨‍💻 Author
Name

Manta Sharifi

GitHub

@itimantasha

Email

mantasharafiq2004@gmail.com

🙏 Acknowledgments
NCBI RefSeq
CARD Database
Biopython
⭐ Show Your Support
If this project helped you, please give it a ⭐️!

Last Updated: March 2026


Copy code

---

## Save to Your Project

```powershell
# Create README.md
notepad README.md
Paste the content above, save it.

Then Push to GitHub
powershell

Copy code
cd C:\Users\manta\Desktop\amr

git add README.md
git commit -m "Add professional README"
git push
Result Will Look Like


Copy code

🧬 AMR Gene Database
📊 Comprehensive Antibiotic Resistance Gene Collection

⭐️ Star us on GitHub!
