## Python Wrapper for Facebook Send/Receive API

Wrapper for [Facebook's Messenger Platform](https://developers.facebook.com/docs/messenger-platform).

__Disclaimer__: This wrapper is __NOT__ an official wrapper and do not attempt to represent Facebook in anyway.

### About

This wrapper has the following functions:

* send_text_message(recipient_id, message)

The functions return the full JSON body of the actual API call to Facebook.

### Register for an Access Token

You'll need to setup a Facebook App, Facebook Page, get the Page Access Token and link the App to the Page before you can really start to use the Send/Receive service.

[This quickstart guide should help](https://developers.facebook.com/docs/messenger-platform/quickstart)

### Installation

```bash
$ pip install pymessenger
```

### Usage

```python
from pymessenger.bot import Bot

bot = Bot(<access_token>)
bot.send_text_message(recipient_id, message)
```

__Note__: From Facebook

> These ids are page-scoped. These ids differ from those returned from Facebook Login apps which are app-scoped. You must use ids retrieved from a Messenger integration for this page in order to function properly.


##### Sending a generic template message:

> [Generic Template Messages](https://developers.facebook.com/docs/messenger-platform/implementation#receive_message) allows you to add cool elements like images, text all in a single bubble.


```python
from pymessenger.bot import Bot
bot = Bot(<access_token>)
elements = []
element = Element(title="test", image_url="<arsenal_logo.png>", subtitle="subtitle", item_url="http://arsenal.com")
elements.append(element)

bot.send_generic_message(recipient_id, elements)
```

Output:

![Generic Bot Output](https://cloud.githubusercontent.com/assets/68039/14519266/4c7033b2-0250-11e6-81a3-f85f3809d86c.png)

### Todo

* Structured Messages
* Receipt Messages
* Tests!

### Example

![Screenshot of Echo Facebook Bot](https://cloud.githubusercontent.com/assets/68039/14516627/905c84ae-0237-11e6-918e-2c2ae9352f7d.png)

You can find an example of an Echo Facebook Bot in ```examples/```


