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
    path = "../dataset_03/{0}".format(filename)
    with open(path, 'wb') as output:
        pickle.dump(dataset, output)

def exist(filename):
    components = filename.split("/")
    directory, file = components[:-1], components[-1]
    directory = "/".join(directory)
    directory = "../dataset_03/{0}".format(directory)
    return file in os.listdir(directory)

def data1():
    n = 2000
    ks = np.hstack([np.arange(1, 21, 1), np.arange(50, 201, 50)])
    probs = [0.1, 0.25, 0.5, 0.7, 0.81]
    err = [0.01, 0.05, 0.09, 0.15, 0.19]
    Ls = np.arange(3, 8)
    rate = lambda x: 0.5 if x < 0.1 else 1/3

    all_datasets = dict()

    # for experiments over different p (6 datasets)
    all_datasets["exp_p"] = dict()
    for k in [10, 100]: 
        for p in probs:
            e = 0.05
            r = rate(e)
            l = 3
            filename = "exp_p/k{1}/data_n{0}_k{1}_p{2}_e{3}_l{4}_r{5:.2f}.pkl".format(n, k, p, e, l, r)
            if exist(filename):
                continue
            print("generating {0} data...".format(filename))
            all_datasets["exp_p"][(k,p,e,l,r)] = make(k,p,e,l,r,n)
            save(all_datasets["exp_p"][(k,p,e,l,r)], filename)

    # for experiments over different e (10 datasets)
    all_datasets["exp_e"] = dict()
    for k in [10, 100]: 
        for e in err:
            p = 0.5
            r = rate(e)
            l = 3
            filename = "exp_e/k{1}/data_n{0}_k{1}_p{2}_e{3}_l{4}_r{5:.2f}.pkl".format(n, k, p, e, l, r)
            if exist(filename):
                continue
            print("generating {0} data...".format(filename))
            all_datasets["exp_e"][(k,p,e,l,r)] = make(k,p,e,l,r,n)
            save(all_datasets["exp_e"][(k,p,e,l,r)], filename)

    # for experiments over different l (16 datasets)
    all_datasets["exp_l"] = dict()
    for k in [20, 100]: 
        e = 0.05
        r = rate(e)
        p = 0.5
        for l in Ls:
            filename = "exp_l/k{1}/data_n{0}_k{1}_p{2}_e{3}_l{4}_r{5:.2f}.pkl".format(n, k, p, e, l, r)
            if exist(filename):
                continue
            print("generating {0} data...".format(filename))
            all_datasets["exp_l"][(k,p,e,l,r)] = make(k,p,e,l,r,n)
            save(all_datasets["exp_l"][(k,p,e,l,r)], filename)

    # for experiments over different k (24 datasets)
    all_datasets["exp_k"] = dict()
    for k in ks:
        p = 0.5
        l = 3
        e = 0.05
        r = rate(e)
        filename = "exp_k/data_n{0}_k{1}_p{2}_e{3}_l{4}_r{5:.2f}.pkl".format(n, k, p, e, l, r)
        if exist(filename):
            continue
        print("generating {0} data...".format(filename))
        all_datasets["exp_k"][(k,p,e,l,r)] = make(k,p,e,l,r,n)
        save(all_datasets["exp_k"][(k,p,e,l,r)], filename)

    # # for experiments over different r (8 datasets)
    # all_datasets["exp_r"] = dict()
    # for k in [10, 100]: 
    #     for r in rate:
    #         e = 0.5
    #         p = 0.5
    #         for l in [3, 5]:
    #             filename = "exp_r/data_n{0}_k{1}_p{2}_e{3}_l{4}_r{5:.2f}.pkl".format(n, k, p, e, l, r)
    #             if exist(filename):
    #                 continue
    #             print("generating {0} data...".format(filename))
    #             all_datasets["exp_r"][(k,p,e,l,r)] = make(k,p,e,l,r,n)
    #             save(all_datasets["exp_r"][(k,p,e,l,r)], filename)

    # print("saving all datasets")
    # with open("../dataset_03_all_datasets_n{0}.pkl".format(n), 'wb') as output:
    #      pickle.dump(all_datasets, output)


if __name__ == '__main__':
    all_datasets = dict()
    get_rate = lambda x: 0.5 if x < 0.1 else 1/3
    n = 100000
    l = 3
    p = 0.5
    for k in np.arange(5, 200, 5):
        for e in np.arange(0.05, 0.21, 0.05):
            r = get_rate(e)
            print("generating (k,p,e,l,r,n) = {0}".format((k,p,e,l,r,n)))
            all_datasets[(k,p,e,l,r,n)] = make(k,p,e,l,r,n)

    with open("../dataset_04_n{0}.pkl".format(n), 'wb') as output:
         pickle.dump(all_datasets, output)


