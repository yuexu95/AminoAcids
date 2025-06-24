# AminoAcids
A Python data visualization project for creating publication-ready figures related to amino acid analysis.

Project Overview
This project generates visualizations for amino acid data analysis, focusing on the relationships between headgroups, amino acids, and tail structures. The visualizations include:

Sankey Diagram: Shows the flow relationships between headgroups, amino acids, and tails

Installation
This project uses Poetry for dependency management. To install:
# Clone the repository
git clone https://github.com/yourusername/AminoAcids.git
cd AminoAcids

# Install dependencies using Poetry
poetry install

Usage
To generate the visualizations:
# Generate Sankey diagram
poetry run python Sankey/import\ pandas\ as\ pd\ copy.py

The visualizations will be saved as SVG files in their respective directories:

- Sankey Diagram: `Sankey/figures/sankey_diagram.svg`
Data
The visualizations use a dataset of amino acid structures with the following attributes:

Rank: Position in ranking
Value: Numerical value associated with each structure
Headgroup: Type of headgroup (CHL or LHL)
Amino acid: Type of amino acid (Cha, Asn, Ser, etc.)
Tail: Tail structure classification
Dependencies
Python 3.12+
pandas
plotly
Molecule Data
The repository includes molecular structure data in SDF format (cleanup_failed.sdf) which can be viewed using molecular visualization software.

License is MIT License.