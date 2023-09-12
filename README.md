# Gotham_earthquake_predictor
**About 98 percent Accurate prediction of the Earthquakes magnitude and depth, in the regions of the city Gotham.

Here's how it looks:

![Screenshot (191)](https://user-images.githubusercontent.com/72303641/139555022-f721d4e5-fef4-4fe4-9cd2-c65415d7f90b.png)



**Disaster suffered region has high chance of suffering from the disaster again! 
So, we are predicting the earthquake with date and time, latitude and longitude from previous data.**

## Importing necessary libraries
![image](https://user-images.githubusercontent.com/72303641/138644244-bc108d33-6e3a-4d19-95ee-222e9566d662.png)



## Feature selection:
**We are going to take main characteristics of earthquake data and create an object of these characteristics, namely, date, time, latitude, longitude, depth, magnitude:**

![image](https://user-images.githubusercontent.com/72303641/138644288-2bfebedd-65df-4f0b-aa6a-c9d60f42be08.png)


**Since the data is random, so we need to scale it based on the model inputs. In this, we convert the given date and time to Unix time which is in seconds and a number. This can be easily used as an entry for the network we have built:**

![image](https://user-images.githubusercontent.com/72303641/138644340-78065aeb-a94a-4f4c-874c-0a166ad735d5.png)


## Splitting the Dataset
**We are taking TImestamp, Latitude and Longitude as input, and the Magnitude and Depth as output. Then we are going to split the data into 80% train set, and rest 20% into test set.**

![image](https://user-images.githubusercontent.com/72303641/138644374-81088c60-22d5-4e98-a979-585127f71d3e.png)
![image](https://user-images.githubusercontent.com/72303641/138644405-188184a5-868a-43c0-87d5-cdea07cc8842.png)

 
## Neural Network for Earthquake Prediction
**Now we will create a neural network to fit the data from the training set. Our neural network will consist of three dense layers each with 16, 16, 2 nodes and reread. Relu and softmax will be used as activation functions:**

![image](https://user-images.githubusercontent.com/72303641/138644476-ec8accd3-29e5-40b1-88ce-ef41dfe659b6.png)
 
 
**Now we’ll define the hyperparameters with two or more options to find the best fit:**

![image](https://user-images.githubusercontent.com/72303641/138644507-762b91ef-f2c1-47ec-a7ee-006fa5afdae4.png)


**Now we need to find the best fit of the above model and get the mean test score and standard deviation of the best fit model:**

![image](https://user-images.githubusercontent.com/72303641/138644570-f422ebe5-c664-4609-8d5a-95707d33eb6b.png)

 
**Accuracy of 98 percent is not bad at all! **
