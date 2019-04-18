#!/usr/bin/env python
from __future__ import with_statement
import sys
import os
import operator

from Bio import SeqIO, Seq
from Bio.SeqRecord import SeqRecord


def gene_to_protein(in_handle, out_handle):   
    seq = SeqIO.to_dict(SeqIO.parse(in_handle, "fasta"))
    with open(out_handle, "w") as out_f: 
        SeqIO.write(parse_record(seq), out_handle, "fasta")

def parse_record(coding_seq): 
    for ident, record in coding_seq.items():
        gene_seq = Seq.Seq(str(reduce(operator.add, record.seq, "")))
        protein_seq = gene_seq.translate()
        yield SeqRecord(protein_seq, record.id, "", "")

if __name__ == "__main__":
    gene_to_protein(*sys.argv[1:])