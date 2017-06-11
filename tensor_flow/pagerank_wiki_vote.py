import tensorflow as tf
import numpy as np
from data_sets.data_sets import DataSets


def ranked(x):
    # x will be a numpy array with the contents of the placeholder below
    return np.argsort(x, axis=0)


def main():
    steps = 20

    data_set = DataSets.get_followers()
    data_set -= 1
    n_raw = data_set.max(axis=0).max() + 1

    beta = tf.constant(0.85, tf.float32)
    n = tf.constant(n_raw, tf.float32)

    a = tf.Variable(tf.transpose(
        tf.scatter_nd(data_set.values.tolist(), data_set.shape[0] * [1.0],
                      [n_raw, n_raw])), tf.float64)

    v = tf.Variable(tf.fill([n_raw, 1], tf.pow(n, -1)))

    o_degree = tf.reduce_sum(a, 0)

    condition = tf.not_equal(o_degree, 0)

    transition = tf.transpose(
        tf.where(condition,
                 tf.transpose(beta * tf.div(a, o_degree) + (1 - beta) / n),
                 tf.fill([n_raw, n_raw], tf.pow(n, -1))))

    page_rank = tf.matmul(transition, v, a_is_sparse=True)

    run_iteration = tf.assign(v, page_rank)

    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)

        for step in range(steps):
            sess.run(run_iteration)

        print(sess.run(v))
        print(sess.run(tf.transpose(tf.py_func(ranked, [-v], tf.int64))[0]))
        tf.summary.FileWriter('logs/.', sess.graph)
        pass


if __name__ == '__main__':
    main()
