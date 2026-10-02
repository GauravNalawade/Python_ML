import numpy as np

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding,SimpleRNN, Dense

# Step 1: Load the data
train_sentences = [
    "food was good",
    "food was bad",
    "food was excellent",
    "food was terrible",
    "service was good",
    "service was bad",
    "service was excellent",
    "service was terrible",
    "ambience was good",
    "ambience was bad",
    "ambience was excellent",
    "ambience was terrible"

]

train_labels = [
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
]

# Step 2:  Tokenization

tokenizer = Tokenizer(oov_token="<oov>")

tokenizer.fit_on_texts(train_sentences)

# Step 3: Convert Training Data into Sequence 

train_sequence = tokenizer.texts_to_sequences(train_sentences)
print("Training sequences : ")

for sentence , sequence in zip(train_sentences,train_sequence):
    print(sentence,"->",sequence)

# Step 4: Applying padding

max_length = 4

X_train = pad_sequences(
    train_sequence,
    maxlen=max_length,
    padding ="pre"
)

Y_train = np.array(train_labels)

print("Padded Training Data")
print(X_train)

print("Training labels :")
print(Y_train)

# Step 5: CAlculate Vocablary size

vocab_size = len(tokenizer.word_index)+1

print("vocablary size is :",vocab_size)

# Step 6: build the model

model = Sequential()

model.add(
    Embedding(
        input_dim=vocab_size,
        output_dim=8,
        input_length=max_length
    )
)

model.add(
    SimpleRNN(
        units =8,
        activation ="tanh",
    )
)

model.add(
    Dense(
        units=1,
        activation="sigmoid"
    )
)
# Step 7: Complie the model

model.compile(
    optimizer ="adam",
    loss="binary_crossentropy",
    metrices=["accuracy"]
)

# Step 8 : Display model

model.build(input_shape =(None,max_length))

print("model architecturer")
model.summary()

# Step 9: Train the model
history=model.fit(
    X_train,
    Y_train,
    epochs=50,
    verbose=1
)

print("Model Training completed")

# Step 10 : Create unseen data

test_sentances = [
    "service was amazing",
    "service was horrible",
    "experience was excellent",
    "experience was terrible"
]

# Step 11 : convert text to sequences

test_sequences = tokenizer.text_to_sequences(test_sentances)

X_test = pad_sequences(
    test_sequences,
    maxlen=max_length,
    padding="pre"
)

# step 12 :predicct the sentiment 

for text, sequence , padded in zip(test_sentances,test_sequences,X_test):
    input_data = np.aaray([padded])

    prediction = model.predict(input_data,verbose=0)

    probabiltity = float(prediction[0][0])

    print("sentence : ",text)
    print("Sequence : ",sequence)
    print("Padded Sequence :",padded)
    print("prediction :",prediction)

    if probabiltity >= 0.5 :
        print("Positive")
    else:
        print("Negative")
