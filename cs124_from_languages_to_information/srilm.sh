#!/usr/bin/env bash

#Download SRILM: http://www.speech.sri.com/projects/srilm/download.html

export SRILM=/srilm
export MACHINE_TYPE=cygwin
export PATH=$PATH:$pwd:$SRILM/bin/cygwin
export MANPATH=$MANPATH:$SRILM/man

# Induce classes:
ngram-class -vocab vocab_file                   \
            -text input_file                    \
            -numclasses num                     \
            -class-counts output.class-counts   \
            -classes output.classes

# Estimate a bigram language model using the classes generated in the previous step:
ngram-count -order 2                    \
            -read output.class-counts   \
            -write output.ngrams

ngram-count -order 2                \
            -read output.ngrams     \
            -lm  output.bo

# To calculate perplexity:
ngram -lm output.bo -classes output.classes -ppl test.txt

