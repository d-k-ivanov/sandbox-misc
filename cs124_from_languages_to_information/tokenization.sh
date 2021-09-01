less ./corpuses/shakespeare.txt
tr -sc 'A-Za-z' '\n' < ./corpuses/shakespeare.txt | less
tr -sc 'A-Za-z' '\n' < ./corpuses/shakespeare.txt | sort | less
tr -sc 'A-Za-z' '\n' < ./corpuses/shakespeare.txt | sort | uniq -c | less
tr -sc 'A-Za-z' '\n' < ./corpuses/shakespeare.txt | sort | uniq -c | sort -n -r | less
tr -sc 'A-Za-z' '\n' < ./corpuses/shakespeare.txt | sort | uniq -c | sort -n -r | less
tr 'A-Z' 'a-z' < ./corpuses/shakespeare.txt | tr -sc 'A-Za-z' '\n' | sort | uniq -c | sort -n -r | less

# Subword tokenization:
# Byte-Pair Encodinf (BPE)
# Unigram language modeling tokenization
# WordPiece

tr 'A-Z' 'a-z' < ./corpuses/low-low-bpe.txt | tr -sc 'A-Za-z' '\n' | sort | uniq -c | sort -n -r | less
tr 'A-Z' 'a-z' < ./corpuses/shakespeare.txt | sed -r 's/[[:blank:]]+/_/g' | less
tr 'A-Z' 'a-z' < ./corpuses/shakespeare.txt | sed -r 's/[[:blank:]]+/_/g' | sed 's/./&\n/g' | sort | uniq -c
tr 'A-Z' 'a-z' < ./corpuses/low-low-bpe.txt | sed -r 's/[[:blank:]]+/_/g' | sed 's/./&\n/g' | sort | uniq -c
tr 'A-Z' 'a-z' < ./corpuses/low-low-bpe.txt | sed -r 's/[[:blank:]]+/_/g' | sed 's/./&\n/g' | sort | uniq -c | awk '{print $1,$2}'
tr 'A-Z' 'a-z' < ./corpuses/low-low-bpe.txt | sed -r 's/[[:blank:]]+/_/g' | sed 's/./&\n/g' | sort | uniq -c | awk '{print $2}'

function bpe()
{

}

split -l 17 sonnets.txt
