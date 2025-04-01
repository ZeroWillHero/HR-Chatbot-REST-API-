# Python Chat Bot For the HR Managment System 
## please follow the instructions to setup and run the bot 

```bash
# Clone the repository
git clone https://github.com/your-username/chatbot-deployment.git

# Navigate to the project directory
cd chatbot-deployment

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install the required dependencies
pip install -r requirements.txt

# install NLTK at the local computer 
python -m nltk.downloader punkt_tab

# if it is not worked use this 
python
>> import nltk
>> nltk.download('punkt')
>> quite()

# Train the bot 
python train.py

# Run the chatbot
python app.py
```

### then you can see following output in the terminal
```bash
(venv) PS C:\Users\ASUS\Desktop\projects\chatbot-deployment> python app.py      
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 645-465-032

```

### use a client like postman for testing


```markdown
### Example API Request

To test the chatbot, you can send a POST request to the following endpoint:

```http
POST http://127.0.0.1:5000/apiV1/message
```

#### Example Request Body
```json
{
    "message": "Hello, how can I help you?"
}
```

You can use tools like Postman or curl to send the request and receive a response from the chatbot.




