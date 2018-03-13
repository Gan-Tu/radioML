# RadioML
ML for software radios

[research repo source](https://github.com/jain-nikunj/radioML)

## Reports

Error Correcting Code

- [v1 notebook](https://github.com/Michael-Tu/radioML/blob/master/ecc-v1.ipynb) and [v1 results](https://github.com/Michael-Tu/radioML/blob/master/report/ecc-v1.md)

- [v2 notebook](https://github.com/Michael-Tu/radioML/blob/master/ecc-v2.ipynb) and [v2 results](https://github.com/Michael-Tu/radioML/blob/master/report/ecc-v2.md)

## Model Downloads

### Error Correcting Code

- [k5-l3-fnn-model-[32,100].h5](https://www.dropbox.com/s/fkspgy0u1zsa5zk/k5-l3-fnn-model-%5B32%2C100%5D.h5?dl=0)
- [k5-l3-cnn-v1.h5](https://www.dropbox.com/sh/zathplg4fq6r0do/AABNcsxla8_kFQB3uWOyppf4a?dl=0)
- [k5-l3-cnn-v2.h5](https://www.dropbox.com/s/adzz0bhwm2bpi3x/k5-l3-cnn-v2.h5?dl=0)


- [ecc-fnn-128-128-100-relu.h5](https://www.dropbox.com/s/kea9sf8aosuetup/ecc-fnn-128-128-100-relu.h5?dl=0)
- [ecc-cnn1.h5](https://www.dropbox.com/s/lgm6dzu5dus47q3/ecc-cnn1.h5?dl=0)



## Generated Data Downloads

### Error Correcting Code

Each sequence is drawn at random from a Bernoulli distribution. These are convolutionally encoded, then subject to varying levels of noise from a binary symmetric channel. Finally, the corresponding Viterbi sequences are also recorded.



- [viterbi_dump_k1_n100.pk](https://www.dropbox.com/s/guqx8xyqt2njoug/viterbi_dump_k1_n100.pk?dl=0)
- [viterbi_dump_k2_n100.pk](https://www.dropbox.com/s/1t48qcpcfo1zri4/viterbi_dump_k2_n100.pk?dl=0)
- [viterbi_dump_k3_n100.pk](https://www.dropbox.com/s/zfwzqnbjj7nstfr/viterbi_dump_k3_n100.pk?dl=0)
- [viterbi_dump_k4_n100.pk](https://www.dropbox.com/s/86prpq51i542cd8/viterbi_dump_k4_n100.pk?dl=0)
- [viterbi_dump_k5_n100.pk](https://www.dropbox.com/s/ps2z0326qroqsms/viterbi_dump_k5_n100.pk?dl=0)
- [viterbi_dump_k6_n100.pk](https://www.dropbox.com/s/e75m0hzo3fnjq44/viterbi_dump_k6_n100.pk?dl=0)
- [viterbi_dump_k7_n100.pk](https://www.dropbox.com/s/d3p4x55if1qo7ca/viterbi_dump_k7_n100.pk?dl=0)
- [viterbi_dump_k8_n100.pk](https://www.dropbox.com/s/bji0sxqtmhgegb5/viterbi_dump_k8_n100.pk?dl=0)
- [viterbi_dump_k9_n100.pk](https://www.dropbox.com/s/a31a5gwoyew6wxm/viterbi_dump_k9_n100.pk?dl=0)
- [viterbi_dump_k10_n100.pk](https://www.dropbox.com/s/exglieng34k05pg/viterbi_dump_k10_n100.pk?dl=0)

- 300 binary sequences of 100-length, generated, convolutional codes with viterbi decoded sequences: [viterbi_dump_k100_n300.pk](https://www.dropbox.com/s/4su9r1iu7srvlzj/viterbi_dump_k100_n300.pk?dl=0)
- 100 binary sequences of 300-length, generated, convolutional codes with viterbi decoded sequences: [viterbi_dump_k300_n100.pk](https://www.dropbox.com/s/r33igmpe07q8704/viterbi_dump_k300_n100.pk?dl=0)


