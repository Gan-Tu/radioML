# Bidirectional LSTM-RNN vs. Basic LSTM-RNN Convergence Rate

Fixed: `n = 25000, rate = 0.5, p = 0.5, l = 3`

error = 0.05

**K10**

Basic LSTM

![basic-k10-e0.05](img/v6/basic-k10-e0.05.png)

Bidirectional LSTM

![bidir-k10-e0.05](img/v6/bidir-k10-e0.05.png)

**K20**

Basic LSTM

![basic-k20-e0.05](img/v6/basic-k20-e0.05.png)

Bidirectional LSTM

![bidir-k20-e0.05](img/v6/bidir-k20-e0.05.png)

**K40**

Basic LSTM

![lstm-rnn-k40-e0.05-train](img/v6/lstm-rnn-k40-e0.05-train.png)

Bidirectional LSTM

![bidir-k40-e0.05](img/v6/bidir-k40-e0.05.png)

# Bidirectional LSTM-RNN on High Error Rate

Fixed: `n = 25000, rate = 0.5, p = 0.5, l = 3`

error = 0.15

**K10**

Basic LSTM

![lstm-rnn-k10-e0.15-train](img/v6/lstm-rnn-k10-e0.15-train.png)

Bidirectional LSTM

![bidir-k10-e0.15](img/v6/bidir-k10-e0.15.png)

**K20**

Basic LSTM

![lstm-rnn-k20-e0.15-train](img/v6/lstm-rnn-k20-e0.15-train.png)

Bidirectional LSTM

![bidir-k20-e0.15](img/v6/bidir-k20-e0.15.png)


### Normalization of Training Data

basic-normalization-train

![basic-normalization-train](img/v6/basic-normalization-train.png)

basic-normalization-val

![basic-normalization-val](img/v6/basic-normalization-val.png)