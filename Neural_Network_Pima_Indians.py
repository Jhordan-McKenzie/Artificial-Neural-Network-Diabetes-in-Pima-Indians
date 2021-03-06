
# Description: This program detects if a person has diabetes or not.

# Load the libraries
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# Load the data
from google.colab import files
uploaded = files.upload()

# Store the data set
df = pd.read_csv('diabetes.csv')

# Print the first 7 rows of data
df.head(7)

# Show the shape ( number of rows and columns)
df.shape

# check for duplicates and remove them.
df.drop_duplicates(inplace= True)

# Show the shape after removal of duplicates
df.shape

# Show the number of missing data for each column
df.isnull().sum()

# Convert the data into an array
dataset = df.values
dataset

# Get all of the rows from the first eight columns of the data set
X = dataset[:, 0:8]
y = dataset[:, 8]

# Process the data
from sklearn import preprocessing
min_max_scalar = preprocessing.MinMaxScaler()
X_scale = min_max_scalar.fit_transform(X)
X_scale

# Split the data into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X_scale, y, test_size= 0.2, random_state = 4)

# Build the model
model = Sequential([
    Dense(12, activation='relu', input_shape=(8,)),            
    Dense(15, activation='relu'),
    Dense(1, activation='sigmoid')     
])

# Compile the model
model.compile(
    optimizer = 'sgd',
    loss = 'binary_crossentropy',
    metrics=['accuracy']
)

# Train the model

hist = model.fit( X_train, y_train, batch_size = 57, epochs = 1000, validation_split = 0.2)

# Visualize the training loss and the validation loss to see if the model is overfitting
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Val'], loc = 'upper right')
plt.show

# Visualize the training accuracy and the validation accuracy to see if the model is overfitting
plt.plot(hist.history['acc'])
plt.plot(hist.history['val_acc'])
plt.title('Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Val'], loc = 'lower right')
plt.show

# Make a prediction and print the actual values
prediction = model.predict(X_test)
prediction = [1 if y>= 0.5 else 0 for y in prediction]
print(prediction)
print(y_test)

# Evaluate the model on the training data set
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

pred = model.predict(X_train)
pred = [1 if y >= 0.5 else 0 for y in pred]
print(classification_report(y_train, pred))
print('Confusion Matrix: \n', confusion_matrix(y_train, pred))
print()
print('Accuracy: ', accuracy_score(y_train, pred) )

# Evaluate the model on the test data set
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

pred = model.predict(X_test)
pred = [1 if y >= 0.5 else 0 for y in pred]
print(classification_report(y_test, pred))
print('Confusion Matrix: \n', confusion_matrix(y_test, pred))
print()
print('Accuracy: ', accuracy_score(y_test, pred))
