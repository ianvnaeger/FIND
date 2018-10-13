import tensorflow as tf
from tensorflow import keras
import numpy as np

#def hello_world(request):
#    """Responds to any HTTP request.
#    Args:
#        request (flask.Request): HTTP request object.
#    Returns:
#        The response text or any set of values that can be turned into a
#        Response object using
#        `make_response <http://flask.pocoo.org/docs/0.12/api/#flask.Flask.make_response>`.
#    """
#    request_json = request.get_json()
#    if request.args and 'message' in request.args:
#        return request.args.get('message')
#    elif request_json and 'message' in request_json:
#        return request_json['message']
#    else:
#        return f'Hello World!'


#def Parser(request): 
    #given a link to an article, the function can find information about the article
        #information to be found: author, source of article, title, etc.
#    return

#def Classifier():
    #take the parsed info, make classifiers based on the validity of the info
#   return

def Decider():
    #given ratings from the classifier, use Machine Learning Magic to determine if fake news
    model = keras.models.Sequential()
    # Adds a densely-connected layer with 64 units to the model:
    #model.add(keras.layers.Dense(64, kernel_regularizer=keras.regularizers.l1(0.01))
    # Add another:
    model.add(keras.layers.Dense(64, activation='sigmoid'))
    # Adds another
    model.add(keras.layers.Dense(64, activation='relu'))
    # Add another:
    model.add(keras.layers.Dense(64, activation='relu'))
    # Add a softmax layer with 1 output unit:
    model.add(keras.layers.Dense(1, activation='softmax')) 

    model.compile(optimizer=tf.train.AdamOptimizer(0.001), loss='categorical_crossentropy', metrics=['accuracy'])

    data = np.random.random((1000, 32))
    labels = np.random.random((1000, 10))

    val_data = np.random.random((100, 32))
    val_labels = np.random.random((100, 10))

    callbacks = [
        # Interrupt training if `val_loss` stops improving for over 2 epochs
        keras.callbacks.EarlyStopping(patience=5, monitor='val_loss'),
        # Write TensorBoard logs to `./logs` directory
        keras.callbacks.TensorBoard(log_dir='./logs')
    ]

    model.fit(data, labels, epochs=10, callbacks=callbacks, batch_size=32, validation_data=(val_data, val_labels))
    model.save('FIND-model.h5')
    # model = keras.models.load_model('FIND-model.h5')
    # ^^^ to load a saved model

    return 0

#def FIND():
    #call Parser
    #call Classifier
    #call Decider

print("starting")
x = Decider()
print("we did it")