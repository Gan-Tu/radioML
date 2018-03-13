
# Results

**Viterbi Decoding Accuracy**

![Viterbi Decoding Accuracy](img/viterbi-accuracy-l3-l5-vs-k.png)


**FNN (32-100) Accuracy vs. Message Length K**

Constraint Length of 3

![Constraint Length of 3](img/[32,100]-fnn-model-l3-vs-k.png)

Constraint Length of 5

![Constraint Length of 5](img/[32,100]-fnn-model-l5-vs-k.png)

**FNN (32-64-100) Accuracy vs. Message Length K**

Constraint Length of 3

![Constraint Length of 3](img/[32,64,100]-fnn-model-l3-vs-k.png)

Constraint Length of 5

![Constraint Length of 5](img/[32,64,100]-fnn-model-l5-vs-k.png)

# Example Results

Below are some results for the `[32,100]-fnn-model-l3` model

```
Expected:  [0, 0, 1, 1, 0]
Deocde:    [0, 0, 1, 1, 0]

Expected:  [1, 1, 0, 1, 1]
Deocde:    [1, 1, 0, 0, 1]

Expected:  [1, 0, 1, 1, 1]
Deocde:    [0, 0, 0, 1, 1]

Expected:  [0, 1, 1, 0, 0]
Deocde:    [0, 0, 0, 0, 0]

Expected:  [0, 0, 0, 0, 0]
Deocde:    [0, 0, 1, 1, 0]
```

# FNN Architectures Search Space:

```
FNN_ARCHITECTURE = [
    [32, 100],
    [64, 100],
    [128, 100],
    [256, 100],
    [32, 32, 100],
    [32, 64, 100],
    [64, 64, 100],
    [64, 128, 100],
    [128, 128, 100],
    [128, 256, 100],
    [256, 256, 100],
    [32,128,128,100],
    [32,128,256,100],
    [32,256,256,100],
    [32,128,256,128,100],
    [32,128,128,128,100],
    [1024,512,100],
    [512,256,100],
    [256,128,100],
    [128,100,100]
]
```


## Hyperparameters

```
BATCH_SIZE = 64
EPOCHS = 50
ACTIVATION = "relu"
l2_reg_strength = 0.001
LR = 0.015
optimizer = "adam"
```

