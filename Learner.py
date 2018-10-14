import tensorflow as tf
from tensorflow import keras

def Decider():
    #given ratings from the classifier, use Machine Learning Magic to determine if fake news
    model = keras.models.Sequential()
    # Adds a densely-connected layer with 64 units to the model:
    #model.add(keras.layers.Dense(64, kernel_regularizer=keras.regularizers.l1(0.01))
    # Add another:
    model.add(keras.layers.Dense(64, input_shape=(5,), activation='sigmoid'))
    model.add(keras.layers.Dense(64, activation='sigmoid'))
    model.add(keras.layers.Dense(64, activation='sigmoid'))
    model.add(keras.layers.Dense(64, activation='relu'))
    model.add(keras.layers.Dense(64, activation='relu'))
    # Add a softmax layer with 1 output unit:
    model.add(keras.layers.Dense(1, activation='softmax')) 

    model.compile(optimizer=keras.optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    data = np.random.random((1000, 32))
    labels = np.random.random((1000, 1))

    val_data = np.random.random((100, 32))
    val_labels = np.random.random((100, 1))

    callbacks = [
        # Interrupt training if `val_loss` stops improving for over 2 epochs
        keras.callbacks.EarlyStopping(patience=5, monitor='val_loss'),
        # Write TensorBoard logs to `./logs` directory
        keras.callbacks.TensorBoard(log_dir='./logs')
    ]

    model.fit(data, labels, epochs=10, callbacks=callbacks, batch_size=32, validation_data=(val_data, val_labels))
    model.save('./FIND-model.h5')
    # model = keras.models.load_model('FIND-model.h5')
    # ^^^ to load a saved model

    return 0

print(Decider())