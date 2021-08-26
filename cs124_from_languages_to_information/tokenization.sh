less ./corpuses/shakespeare.txt
tr -sc 'A-Za-z' '\n' < ./corpuses/shakespeare.txt | less
tr -sc 'A-Za-z' '\n' < ./corpuses/shakespeare.txt | sort | less
tr -sc 'A-Za-z' '\n' < ./corpuses/shakespeare.txt | sort | uniq -c | less
tr -sc 'A-Za-z' '\n' < ./corpuses/shakespeare.txt | sort | uniq -c | sort -n -r | less
