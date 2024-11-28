## Marley-and-Me-pet-adoption-software
In this project, we have created a software that helps animal shelters to better potential adopters. The functions and methods written for this project are mainly in Python. However, there are some HTML/CSS files uploaded that are aimed to also provide an interface. For this project, these packages should be installed beforehand: Flask, Transformers, Sacremoses, Dash, and Cohere. The required codes for installing these packages are provided in each model's Jupyter Notebook.  
The functions and methods used in the software are tested thoroughly and the testing process can be viewed in the testing directory of this repository.  
We have also trained an OpenNMT model using the Tatoeba dataset. However, due to the limitations of this dataset, we have decided to not use this trained model for our software. Unfortunately, we did not have enough necessary computational resources to train another model based on a bigger and more inclusive dataset. That is the reason we decided to use the pre-trained MarianNMT model for our software.  
Both MT and the description generator models are accessed and implemented through three types of users. Firstly, an interface user that gets input from the user. Then, the given input is passed onto the orchestrator server which then passes the information to the server that contains the AI model. This server will use that information and the implemented model to produce an output. This output is again passed to the orchestrator which will send this information further to the interface output. Thus, the user will be able to view the workings of the AI model.  
Contributors:  
  -Python programming: Korosh Rajaei  
  -HTML/CSS and design of the interface: Emre Uysal, Amirhossein Shahsavari  
  -OpenNMT training: Korosh Rajaei, Emre Uysal, Amirhossein Shahsavari  
  -Finding and the choice of the dataset for OpenNMT training: Linda Selles, Sterre Zwart  
Screenshots of interfaces and servers are also uploaded to the repository.
