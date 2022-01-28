
Overview:

To assess people with communication disorders clinicians need better insights into their daily life and it is a laborious and time-consuming task. We have created an API extract features from conversation such as average percentage spoke in conversation, taking turns in conversation, total pauses during a conversation, and many other speaker metrics. The goal of this API is to integrate into a user-friendly system so that users can easily analyze a conversation and have an intuition of individuals' involvement in communication and daily life.

Tool installment:

Pre-requisites:

•	Programming language : Python (3.8 or above) - https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe - windows , https://www.python.org/ftp/python/3.8.10/python-3.8.10-macosx10.9.pkg - MacOS.

•	Packages : Pandas,numpy,nltk
•	IDE : Any python supported IDE(we used PyCharm).
•	API Testing Tools : Postman
•	A file with 'wav','awb','m4a','mp3','mp4' format.
Steps to do before executing the app:
•	Update the file location of the input file with your local directory in app.py
![image](https://user-images.githubusercontent.com/43305644/151613082-eb35f75f-1889-4b01-b829-2767e7cd89de.png)

•	Google Speech API:
1.	Go to your google cloud console.
2.	Enable google speech to text api.
3.	Get the credential json file by creating the key in service accounts(IAM & ADMIN -> service accounts) and replace the code in client_secret.json (Conversation-Moderator-API->resources->client_secret.json).

•	Create the virtual environment(if not created) for the application as below:

pip install virtualenv
virtualenv my_env

Then install the requiremnents

pip install -r requirements.txt

Execution:

•	Execute the python application in the virtual environment that is created.
•	The application will be running in the local host.  

Output:

•	Try hitting the local url in postman by importing the following collection - https://www.getpostman.com/collections/8246194f7189bdfc8072 
•	Upload the file in the body of the postman as below -  
![image](https://user-images.githubusercontent.com/43305644/151613634-7838e5b7-2ade-4103-a5d7-e345dc3bfae3.png)

•	We can observe a successful run of the API which returns a JSON with the detailed output in the postman dashboard.  
•	The required result will be shown in the terminal. 
