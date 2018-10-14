import tensorflow as tf
from tensorflow import keras

def Decider():
    inputs = keras.Input(shape=(5,))  # Returns a placeholder tensor

    # A layer instance is callable on a tensor, and returns a tensor.
    x = keras.layers.Dense(64, activation='sigmoid')(inputs)
    y = keras.layers.Dense(64, activation='relu')(x)
    z = keras.layers.Dense(64, activation='relu')(y)
    a = keras.layers.Dense(64, activation='relu')(z)
    predictions = keras.layers.Dense(1, activation='softmax')(a)

    # Instantiate the model given inputs and outputs.
    model = keras.Model(inputs=inputs, outputs=predictions)

    # The compile step specifies the training configuration.
    model.compile(optimizer=tf.train.RMSPropOptimizer(0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

    # Trains for 5 epochs
    model.fit(data, labels, batch_size=5, epochs=500)
    
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

    model.compile(optimizer=tf.train.AdamOptimizer(0.001)), loss='categorical_crossentropy', metrics=['accuracy'])

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