# RadioML
ML for software radios

[research group repo](https://github.com/jain-nikunj/radioML)

## Reports

**Error Correcting Code**

_Most Update to Date:_ [v4 notebook](https://github.com/Michael-Tu/radioML/blob/master/notebooks/ecc-v4.ipynb)


**Others**


- [v3 notebook](https://github.com/Michael-Tu/radioML/blob/master/notebooks/ecc-v3.ipynb) and [v3 results](https://github.com/Michael-Tu/radioML/blob/master/report/ecc-v3.md)

- [v2-2.0 notebook](https://github.com/Michael-Tu/radioML/blob/master/notebooks/ecc-v2-v2.0.ipynb) and [v2 results](https://github.com/Michael-Tu/radioML/blob/master/report/ecc-v2.md)

- [v2-1.0 notebook](https://github.com/Michael-Tu/radioML/blob/master/notebooks/ecc-v2-v1.0.ipynb) and [v2 results](https://github.com/Michael-Tu/radioML/blob/master/report/ecc-v2.md)

- [v1 notebook](https://github.com/Michael-Tu/radioML/blob/master/notebooks/ecc-v1.ipynb) and [v1 results](https://github.com/Michael-Tu/radioML/blob/master/report/ecc-v1.md)

## Model Downloads

### Error Correcting Code

You can download trained models from my [Dropbox](https://www.dropbox.com/sh/zathplg4fq6r0do/AABNcsxla8_kFQB3uWOyppf4a?dl=0)

## Generated Data Downloads

### Error Correcting Code

Each sequence is drawn at random from a Bernoulli distribution. These are convolutionally encoded, then subject to varying levels of noise from a binary symmetric channel. Finally, the corresponding Viterbi sequences are also recorded.

You can download all the data from my [Dropbox](https://www.dropbox.com/sh/crdjyolj318rzz3/AAANucpoWs_Uje73NDNTZSqKa?dl=0)

### Large 6GB dataset

Fixed: `n = 25000, rate = 0.5, p = 0.5, l = 3`

Variable:

- `k = [5,  10,  15,  20,  25,  30,  35,  40,  45,  50,  
        55,  65,  75, 85,  95, 105, 115, 125, 135, 145, 
        155, 165, 175, 185, 195]` 
- `(e, rate) = [(0.05, 0.5), (0.15, 1/3)]`

Fixed: `n = 25000, rate = 0.5, p = 0.5, l = 3`

Data: [download](https://www.dropbox.com/sh/6f13x0hqqqnzqsx/AADASLoeXiveXhRAqHnh3lk-a?dl=1)


### Small varying dataset

Data: [download all](https://www.dropbox.com/sh/bohme1mfhrfl34f/AADeR3Fhga5mKnKBc735p43va?dl=1)

---

Variable: `p = [0.1, 0.25, 0.5, 0.7, 0.81]`)

Fixed: `n = 2000, error = 0.05, rate = 0.5, l = 3`

Data: 

- [download `k = 10`](https://www.dropbox.com/sh/jmzy82qvkhm56i9/AAC0J6CTKYbe08OjCJHdzw7Ba?dl=1)
- [download `k = 100`](https://www.dropbox.com/sh/7rrsuyxsr3sgzcl/AABKUOhx7qIKH1FWIv2m8uV2a?dl=1)

---

Variable: `error = [0.01, 0.05, 0.09, 0.15, 0.19]`)

Fixed: `n = 2000, p = 0.5, l = 3`

Note, due to channel capacity: `rate = 0.5` for `0 < error < 0.1` and `rate = 1/3` for `0.1 <= error < 0.2`.

Data: 

- [download `k = 10`](https://www.dropbox.com/sh/mdixtols9gzipwp/AAD-te-dssQZgqTy-ur_cLeja?dl=1)
- [download `k = 100`](https://www.dropbox.com/sh/k07j3aq8yx76ero/AAAZa-BfwxttvDtoPTeb8RJQa?dl=1)

---

Variable: `l = [3, 4, 5, 6, 7]`

Fixed: `n = 2000, p = 0.05, error = 0.05, rate = 0.5`

Data: 

- [download `k = 20`](https://www.dropbox.com/sh/nx6dq2wwent9iag/AADgCYclfI69aw6WA4YpRyeZa?dl=1)
- [download `k = 100`](https://www.dropbox.com/sh/brlu9ojw4wcxbwa/AAD9la6CqyqPc4JBcMjJVOWUa?dl=1)

---

Variable: `k = [1, ..., 20, 50, 100, 150, 200]`

Fixed: `n = 2000, p = 0.05, error = 0.05, rate = 0.5, l = 3`

Data: 

- [download](https://www.dropbox.com/sh/e1jrbcgwusxdb9g/AABrl_K-ooXKYQNQ0-OFvjPIa?dl=1)

