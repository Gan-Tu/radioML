from generate_data import *
import numpy as np
import pickle
import os

def make(k,p,e,l,r,n):
    try:
        message_seqs, encoded_seqs = generate_encode_random_sequences(l, k, n, r, p)
        noisy_seqs = simulate_bsc(encoded_seqs, p=e)
        viterbi_decoded_seqs = viterbi_decode_sequences(noisy_seqs, l, rate=r)

        dataset = {
            "message_seqs": message_seqs,
            "encoded_seqs": encoded_seqs,
            "noisy_seqs": noisy_seqs,
            "viterbi_decoded_seqs": viterbi_decoded_seqs
        }
        return dataset
    except Exception as e:
        print("failed on (k,p,e,l,r,n) = ", str((k,p,e,l,r,n)))
        print("error: ", e)

def save(dataset, filename):
    path = "data/dataset_02/{0}".format(filename)
    with open(path, 'wb') as output:
        pickle.dump(dataset, output)

def exist(filename):
    components = filename.split("/")
    directory, file = components[:-1], components[-1]
    directory = "/".join(directory)
    directory = "data/dataset_02/{0}".format(directory)
    return file in os.listdir(directory)


if __name__ == '__main__':
    n = 5000
    ks = np.hstack([np.arange(1, 21, 1), np.arange(50, 201, 50)])
    probs = [0.1, 0.5, 0.81]
    err = [0.05, 0.1, 0.15, 0.2, 0.3, 0.5, 0.8]
    Ls = np.arange(3, 10)
    rate = [1/2, 1/3]

    all_datasets = dict()

    # for experiments over different k (24 datasets)
    all_datasets["exp_k"] = dict()
    for k in ks:
        p = 0.5
        e = 0.5
        r = 0.5
        for l in [3, 5]:
            filename = "exp_k/data_n{0}_k{1}_p{2}_e{3}_l{4}_r{5:.2f}.pkl".format(n, k, p, e, l, r)
            if exist(filename):
                continue
            print("generating {0} data...".format(filename))
            all_datasets["exp_k"][(k,p,e,l,r)] = make(k,p,e,l,r,n)
            save(all_datasets["exp_k"][(k,p,e,l,r)], filename)

    # for experiments over different p (24 datasets)
    all_datasets["exp_p"] = dict()
    for k in [10, 50, 100, 200]: 
        for p in probs:
            e = 0.5
            r = 0.5
            for l in [3, 5]:
                filename = "exp_p/data_n{0}_k{1}_p{2}_e{3}_l{4}_r{5:.2f}.pkl".format(n, k, p, e, l, r)
                if exist(filename):
                    continue
                print("generating {0} data...".format(filename))
                all_datasets["exp_p"][(k,p,e,l,r)] = make(k,p,e,l,r,n)
                save(all_datasets["exp_p"][(k,p,e,l,r)], filename)

    # for experiments over different e (28 datasets)
    all_datasets["exp_e"] = dict()
    for k in [10, 100]: 
        for e in err:
            p = 0.5
            r = 0.5
            for l in [3, 5]:
                filename = "exp_e/data_n{0}_k{1}_p{2}_e{3}_l{4}_r{5:.2f}.pkl".format(n, k, p, e, l, r)
                if exist(filename):
                    continue
                print("generating {0} data...".format(filename))
                all_datasets["exp_e"][(k,p,e,l,r)] = make(k,p,e,l,r,n)
                save(all_datasets["exp_e"][(k,p,e,l,r)], filename)

    # for experiments over different r (8 datasets)
    all_datasets["exp_r"] = dict()
    for k in [10, 100]: 
        for r in rate:
            e = 0.5
            p = 0.5
            for l in [3, 5]:
                filename = "exp_r/data_n{0}_k{1}_p{2}_e{3}_l{4}_r{5:.2f}.pkl".format(n, k, p, e, l, r)
                if exist(filename):
                    continue
                print("generating {0} data...".format(filename))
                all_datasets["exp_r"][(k,p,e,l,r)] = make(k,p,e,l,r,n)
                save(all_datasets["exp_r"][(k,p,e,l,r)], filename)

    # for experiments over different l ( datasets)
    all_datasets["exp_l"] = dict()
    for k in [10, 100]: 
        r = 0.5
        e = 0.5
        p = 0.5
        for l in Ls:
            filename = "exp_l/data_n{0}_k{1}_p{2}_e{3}_l{4}_r{5:.2f}.pkl".format(n, k, p, e, l, r)
            if exist(filename):
                    continue
            print("generating {0} data...".format(filename))
            all_datasets["exp_l"][(k,p,e,l,r)] = make(k,p,e,l,r,n)
            save(all_datasets["exp_l"][(k,p,e,l,r)], filename)

    print("saving all datasets")
    with open("data/dataset_02_all_datasets_n{0}.pkl".format(n), 'wb') as output:
         pickle.dump(all_datasets, output)

