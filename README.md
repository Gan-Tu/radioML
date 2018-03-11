# RadioML
ML for software radios

[research repo source](https://github.com/jain-nikunj/radioML)

## Reports

- [ecc-v1](https://github.com/Michael-Tu/radioML/blob/master/report/ecc-v1.md)

## Generated Data Downloads

### Error Correcting Code

Each sequence is drawn at random from a Bernoulli distribution. These are convolutionally encoded, then subject to varying levels of noise from a binary symmetric channel. Finally, the corresponding Viterbi sequences are also recorded.

- 300 binary sequences of 100-length, generated, convolutional codes with viterbi decoded sequences: [viterbi_dump_k100_n300.pk](https://www.dropbox.com/s/4su9r1iu7srvlzj/viterbi_dump_k100_n300.pk?dl=0)
- 100 binary sequences of 300-length, generated, convolutional codes with viterbi decoded sequences: [viterbi_dump_k300_n100.pk](https://www.dropbox.com/s/r33igmpe07q8704/viterbi_dump_k300_n100.pk?dl=0)

## Model Downloads

### Error Correcting Code

- [ecc-ffn-128-128-100-relu.h5](https://www.dropbox.com/s/kea9sf8aosuetup/ecc-fnn-128-128-100-relu.h5?dl=0)
- [ecc-cnn1.h5](https://www.dropbox.com/s/lgm6dzu5dus47q3/ecc-cnn1.h5?dl=0)