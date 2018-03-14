import spacy
import nltk
import sys

nlp = spacy.load('en')

def getFirstSent(para):
    doc = nlp(para)
    return list(doc.sents)[0].text

def main():
    argument_list = sys.argv
    inputfile = argument_list[1]
    outputfile = argument_list[2]
    #Input string

    document = open(inputfile,'r',encoding='utf-8').read()

    #split paragraph
    para_list = document.split('\n')

    final_res = ''
    for para in para_list:
        final_res = final_res + getFirstSent(para) + '\n'

    with open(outputfile, 'w' , encoding= 'utf-8') as f:
        f.write(final_res)


if __name__ == "__main__":
    main()