import numpy as np
from sklearn.datasets import fetch_mldata
import matplotlib.pyplot as plt
from tensorflow.contrib import keras


def add_bias_feature(X):
    return np.c_[np.ones(len(X)), X]


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def hypotheses(W, X):
    result = X @ W
    return sigmoid(result)


def cost(W, X, Y, eps=0.01):
    h = hypotheses(W, X)
    result = Y * np.log(h + eps) + (1 - Y) * np.log(1 - h + eps)
    result = result.mean()
    result *= -1
    return result


def gradient_step(W, X, Y, learning_rate=0.01):
    H = hypotheses(W, X)
    errors = H - Y
    epsilons = (X.T.dot(errors)) / len(errors)
    return W - epsilons * learning_rate


def prepare_lin_reg():
    mnist_dir = './../../../data/mnist'
    mnist = fetch_mldata('MNIST original', data_home=mnist_dir)

    examples_count = mnist.data.shape[0]
    labels = mnist.target.astype(int)
    normalized_pixels_nobias = mnist.data / 255
    one_hot_labels = np.zeros((examples_count, 10))
    one_hot_labels[np.arange(examples_count), labels] = 1
    print(one_hot_labels[0])

    def display_mnist_elem(index):
        img = mnist.data[rand_no]
        pixels = img.reshape(28, 28) / 255
        plt.imshow(pixels, cmap='gray')
        plt.show()
        print('label:', labels[rand_no])
        print('label as a one-hot vector:', one_hot_labels[rand_no])

    normalized_pixels = add_bias_feature(normalized_pixels_nobias)

    rand_numbers = np.arange(examples_count)
    np.random.shuffle(rand_numbers)

    train_count = 60000
    train_numbers = rand_numbers[:train_count]
    X_train = np.array([normalized_pixels[i] for i in range(examples_count) if i in train_numbers])
    Y_train = np.array([one_hot_labels[i] for i in range(examples_count) if i in train_numbers])

    X_test = np.array([normalized_pixels[i] for i in range(examples_count) if i not in train_numbers])

    Y_test = np.array([mnist.target[i] for i in range(examples_count) if i not in train_numbers])

    W = np.random.random((785, 10))  # 784 + bias feature
    # costs = []
    steps = 1000

    for i in range(steps):
        print(i)
        W = gradient_step(W, X_train, Y_train)
        # print(cost(W, X_train, Y_train))

    rand_no = np.random.randint(0, examples_count)
    display_mnist_elem(rand_no)
    img_pixels = normalized_pixels[rand_no]
    predicted_H = hypotheses(W, img_pixels)
    predicted_class = np.argmax(predicted_H)

    print('predicted hypotheses:', predicted_H)
    print('predicted_class:', predicted_class)

    np.save('mnist_linear_reg.weights', W)


def prepare_nn():
    mnist_dir = './../../../data/mnist'
    print('fetching')
    mnist = fetch_mldata('MNIST original', data_home=mnist_dir)

    examples_count = mnist.data.shape[0]
    labels = mnist.target.astype(int)
    normalized_pixels_nobias = mnist.data / 255
    one_hot_labels = np.zeros((examples_count, 10))
    one_hot_labels[np.arange(examples_count), labels] = 1
    normalized_pixels = normalized_pixels_nobias

    # normalization is important
    normalized_pixels = normalized_pixels


    rand_numbers = np.arange(examples_count)
    np.random.shuffle(rand_numbers)

    train_count = 60000
    train_numbers = rand_numbers[:train_count]
    X_train = np.array([normalized_pixels[i] for i in range(examples_count) if i in train_numbers])
    Y_train = np.array([one_hot_labels[i] for i in range(examples_count) if i in train_numbers])

    X_test = np.array([normalized_pixels[i] for i in range(examples_count) if i not in train_numbers])

    Y_test = np.array([one_hot_labels[i] for i in range(examples_count) if i not in train_numbers])

    model = keras.models.Sequential([
        keras.layers.Dense(100, activation='relu', input_shape=(784,)),

        keras.layers.Dense(10, activation='softmax')  # input shape inferred automatically, yaay!
    ])
    model.compile(loss='categorical_crossentropy',
                  optimizer=keras.optimizers.Adam(),  # dać nowy optimajzer? A dam! (hehe)
                  metrics=['accuracy'])

    model.fit(X_train, Y_train, epochs=10)

    model.save('mnist.keras')


# prepare_nn()