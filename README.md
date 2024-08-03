# textencoder
Encodes and decodes text.

## Disclaimer
Inspired by vgaj's [Plain Text Encoder](https://github.com/vgaj/ple).

## Usage
In command line:
> python code.py <encode|decode> dictionary input output

### dictionary
Filename that points to a list of words. You can use your own list. 
The repository contains two lists:
- dolch: Dolch's [Word List](https://en.wikipedia.org/wiki/Dolch_word_list)
- lorem: a list of Latin words inspired by Cicero's. See [this page](https://www.lipsum.com/) for more details.
### input 
Filename of the input text. 
### output
Filename of the output text. 

## Example

> python code.py encode lorem text out

Contents of 'text' (the input):

> Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the Government for a redress of grievances.

Contents of 'out' (the encoded output):

> elit, laboris laboriosam, ipsum libero ipsa Lorem Lorem consequat. Lorem irure in iusto iusto consequat. labore in iure ipsa consequat. laboriosam, laboris consequat. iusto in maiores consequat
. libero ipsa Lorem laborum ipsa incidunt magna iste laboriosam, ipsum consequat. in laboriosam, consequat. ipsa Lorem magna in incididunt iusto iste Lorem irure labore ipsa laboriosam, magna c
onsequat. laboris ipsam consequat. libero ipsa iusto iste ipsum iste laboris laboriosam, debitis consequat. laboris libero consequat. laborum libero laboris irure iste incididunt iste magna ist
e laboriosam, ipsum consequat. magna irure ipsa consequat. ipsam libero ipsa ipsa consequat. ipsa maxime ipsa libero incidunt iste Lorem ipsa consequat. magna irure ipsa libero ipsa laboris ips
am ducimus consequat. laboris libero consequat. in incididunt libero iste inventore ipsum iste laboriosam, ipsum consequat. magna irure ipsa consequat. ipsam libero ipsa ipsa inventore laboris 
labore consequat. laboris ipsam consequat. Lorem laborum ipsa ipsa incidunt irure debitis consequat. laboris libero consequat. laboris ipsam consequat. magna irure ipsa consequat. laborum liber
o ipsa Lorem Lorem ducimus consequat. laboris libero consequat. magna irure ipsa consequat. libero iste ipsum irure magna consequat. laboris ipsam consequat. magna irure ipsa consequat. laborum
 ipsa laboris laborum iusto ipsa consequat. laborum ipsa in incidunt ipsa in incididunt iusto minim consequat. magna laboris consequat. in Lorem Lorem ipsa labore incididunt iusto ipsa debitis 
consequat. in laboriosam, inventore consequat. magna laboris consequat. laborum ipsa magna iste magna iste laboris laboriosam, consequat. magna irure ipsa consequat. esse laboris magni ipsa lib
ero laboriosam, labore ipsa laboriosam, magna consequat. ipsam laboris libero consequat. in consequat. libero ipsa inventore libero ipsa Lorem Lorem consequat. laboris ipsam consequat. ipsum li
bero iste ipsa magni in laboriosam, incidunt ipsa Lorem deleniti consequat. aliquid

You can verify that the decoding process

> python code.py decode lorem out text

produces the same starting text.
