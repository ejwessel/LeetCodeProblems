## Word Break 2

My first hard problem! woo

Runtime:O(mn^2)
- we only traverse on words in the dictionary - m
- we combine dictionary words with other words, but use precomputed solutions to create new words

Space: O(n^2)
- precomputed solutions only exist for solutions in the dictionary.
- The dictionary grows linearly for every solution added