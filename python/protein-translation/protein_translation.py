# Proteins dictionary
protein = {}
protein['Methionine'] = ['AUG']
protein['Phenylalanine'] = ['UUU', 'UUC']
protein['Leucine'] = ['UUA', 'UUG']
protein['Serine'] = ['UCU', 'UCC', 'UCA', 'UCG']
protein['Tyrosine'] = ['UAU', 'UAC']
protein['Cysteine'] = ['UGU', 'UGC']
protein['Tryptophan'] = ['UGG']
protein['STOP'] = ['UAA', 'UAG', 'UGA']


def proteins(strand):
    proteins_list = []
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
    for codon in codons:
        for key in protein:
            if codon in protein.get(key):
                if key is 'STOP':
                    return proteins_list
                proteins_list.append(key)
    return proteins_list
