import argparse
from Bio import SeqIO

def subset_fasta(input_fasta, output_fasta, names_list):
    with open(names_list, 'r') as names_file:
        names = set([line.strip() for line in names_file.readlines()])

    input_sequences = SeqIO.parse(input_fasta, 'fasta')
    filtered_sequences = (seq for seq in input_sequences if seq.id in names)
    SeqIO.write(filtered_sequences, output_fasta, 'fasta')

def main():
    parser = argparse.ArgumentParser(description='Subset a fasta file using a list of sequence names.')
    parser.add_argument('-i', '--input', required=True, help='Input fasta file')
    parser.add_argument('-o', '--output', required=True, help='Output fasta file')
    parser.add_argument('-l', '--list', required=True, help='List of sequence names')

    args = parser.parse_args()
    subset_fasta(args.input, args.output, args.list)

if __name__ == '__main__':
    main()
