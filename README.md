# crypto_notifier
An extensible cryptocurrency price notification service

### Install dependencies

Create a virtual environment. Install requirements.

```
pip install -r requirements.txt
```

### Running script
* Notification service comes courtesy of IFTTT. Go to [their site](https://ifttt.com) and create an account. 
* Events triggered by our Python app which will consume the data from the Coinmarketcap API.
* You'll also need to install their mobile app if you wish to get notifications from your python app
* Next, you'll [create](https://ifttt.com/create) an IFTTT applet
* Choose the “webhooks” service and select the “Receive a web request” trigger
* Name the event bitcoin_price_emergency
* For the action select the “Notifications” service and select the “Send a rich notification from the IFTTT app” action
* Give it a title, like “Bitcoin price emergency!”
* Set the message to Bitcoin price is at ${{Value1}}. Buy or sell now!
* Optionally you could add a Link URL to the Coinmarketcap Bitcoin page: https://coinmarketcap.com/currencies/bitcoin/
* Create the action and finish setting up the applet
