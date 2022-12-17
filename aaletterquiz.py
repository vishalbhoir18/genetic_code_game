import streamlit as st

# List of amino acids and their codes
amino_acids = {
    'Alanine': ('A', 'Ala'),
    'Cysteine': ('C', 'Cys'),
    'Aspartic acid': ('D', 'Asp'),
    'Glutamic acid': ('E', 'Glu'),
    'Phenylalanine': ('F', 'Phe'),
    'Glycine': ('G', 'Gly'),
    'Histidine': ('H', 'His'),
    'Isoleucine': ('I', 'Ile'),
    'Lysine': ('K', 'Lys'),
    'Leucine': ('L', 'Leu'),
    'Methionine': ('M', 'Met'),
    'Asparagine': ('N', 'Asn'),
    'Proline': ('P', 'Pro'),
    'Glutamine': ('Q', 'Gln'),
    'Arginine': ('R', 'Arg'),
    'Serine': ('S', 'Ser'),
    'Threonine': ('T', 'Thr'),
    'Valine': ('V', 'Val'),
    'Tryptophan': ('W', 'Trp'),
    'Tyrosine': ('Y', 'Tyr'),
    'Stop': ('*', 'Stop')
}

st.title('Amino Acid Code Game')

# Select a random amino acid to guess
import random
amino_acid = random.choice(list(amino_acids.keys()))
one_letter_code, three_letter_code = amino_acids[amino_acid]

# Prompt the user to enter the one-letter or three-letter code
code_type = st.radio('Guess the one-letter or three-letter code?', ('One-letter', 'Three-letter'))
if code_type == 'One-letter':
    guess = st.text_input('Enter the one-letter code for {}:'.format(amino_acid))
elif code_type == 'Three-letter':
    guess = st.text_input('Enter the three-letter code for {}:'.format(amino_acid))

# Check if the guess is correct and display the result
if guess.upper() == one_letter_code or guess.upper() == three_letter_code:
    st.success('Correct!')
else:
    st.error('Incorrect. The correct code is {} ({}).'.format(one_letter_code, three_letter_code))
