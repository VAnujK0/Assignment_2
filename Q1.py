import os
import csv
import spacy
import scispacy
from spacy import displacy
from collections import Counter
from transformers import AutoTokenizer
import pandas as pd

# Task 1: Extract text from CSV files and store in a single .txt file
csv_directory = r'C:\Users\LENOVO\Desktop\Shaheer_work'
txt_output_file = 'output_text.txt'

with open(txt_output_file, 'w', encoding='utf-8') as output_file:
    for filename in os.listdir(csv_directory):
        if filename.endswith('.csv'):
            with open(os.path.join(csv_directory, filename), 'r', encoding='utf-8') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    text = row['text']
                    output_file.write(text + '\n')

# Task 2: Install required libraries and models
# Task 2: Install required libraries and models
# Install spaCy and scispaCy
# !pip install spacy
# !pip install scispacy

# Install Transformers (Hugging Face) library
# !pip install transformers

# Task 3.1: Count occurrences of words and store Top 30 in a CSV file
def count_words_and_save_top_30(file_path):
    with open(file_path, 'r', encoding='utf-8') as text_file:
        text = text_file.read()
        tokens = text.split()
        word_counts = Counter(tokens)
        top_30_words = word_counts.most_common(30)
    
    df = pd.DataFrame(top_30_words, columns=['Word', 'Count'])
    df.to_csv('top_30_words.csv', index=False)

count_words_and_save_top_30('output_text.txt')

# Task 3.2: Count unique tokens using Auto Tokenizer and give Top 30 words
def count_unique_tokens(text_file_path):
    tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
    with open(text_file_path, 'r', encoding='utf-8') as text_file:
        text = text_file.read()
        tokens = tokenizer.tokenize(text)
        unique_tokens = list(set(tokens))
        token_counts = Counter(tokens)
        top_30_tokens = token_counts.most_common(30)

    df = pd.DataFrame(top_30_tokens, columns=['Token', 'Count'])
    df.to_csv('top_30_tokens.csv', index=False)

count_unique_tokens('output_text.txt')

# Task 4: Named-Entity Recognition (NER)
def extract_entities(text_file_path):
    # Load NER models
    nlp_sci = spacy.load('en_core_sci_sm')
    nlp_biobert = spacy.load('en_ner_bc5cdr_md')

    # Process text
    with open(text_file_path, 'r', encoding='utf-8') as text_file:
        text = text_file.read()
        doc_sci = nlp_sci(text)
        doc_biobert = nlp_biobert(text)

    # Extract entities
    diseases_sci = [ent.text for ent in doc_sci.ents if ent.label_ == 'DISEASE']
    drugs_sci = [ent.text for ent in doc_sci.ents if ent.label_ == 'CHEMICAL']
    diseases_biobert = [ent.text for ent in doc_biobert.ents if ent.label_ == 'DISEASE']
    drugs_biobert = [ent.text for ent in doc_biobert.ents if ent.label_ == 'DRUG']

    # Compare results
    print('Entities detected by en_core_sci_sm:')
    print('Diseases:', diseases_sci)
    print('Drugs:', drugs_sci)
    print('Total entities (en_core_sci_sm):', len(diseases_sci) + len(drugs_sci))
    print()
    print('Entities detected by en_ner_bc5cdr_md (BioBert):')
    print('Diseases:', diseases_biobert)
    print('Drugs:', drugs_biobert)
    print('Total entities (en_ner_bc5cdr_md):', len(diseases_biobert) + len(drugs_biobert))
    print()
    print('Difference in entities:', abs((len(diseases_sci) + len(drugs_sci)) - (len(diseases_biobert) + len(drugs_biobert))))
    print()

extract_entities('output_text.txt')
