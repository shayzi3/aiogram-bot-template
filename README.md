<<<<<<< HEAD
### Aiogram bot template with Webhook, SQLAlchemy, Admin, Logging

#### Why this template?
- Database SQLAlchemy
- Webhook for speed and scalability
- Ability to add an admin
- Logging for monitoring bot events


## Setup

Create a directory, open terminal and enter
```
cd your-directory
git clone https://github.com/shayzi3/aiogram-bot-template.git
```

Create `.env` file in `bot/core` and add this variables
```
BOT_TOKEN=""
SQL_URL=""
WEBHOOK_DOMAIN=""
SECRET_WEBHOOK_TOKEN=""
LOGGING_FORMAT=""
ALERT_CHAT=""
SERVER_ERROR_MESSAGE=""
UVICORN_PORT=8083
UVICORN_HOST="0.0.0.0"
```

> [!IMPORTANT]
> Basic env variables for the first start bot
> ```
> BOT_TOKEN=""
> WEBHOOK_DOMAIN=""
> SECRET_WEBHOOK_TOKEN=""
> UVICORN_PORT=8083
> UVICORN_HOST="0.0.0.0"
> ```


### First start

Type this commands
```
cd aiogram-bot-template
python -m venv venv
venv/Scripts/activate
```

Install requirements
```
pip install -r requirements.txt
```

Start bot
```
python main.py
```

## About this template
**All, that connected with bot in directory bot, everything else in directory infrastructure.**

#### Alert System
Alert is a notification about something sent to a channel.

[!NOTE]
> Example: After executing the handler with an error, an alert 
> occurs.


#### Database models
You can make interaction with database models by using pattern `Repository` or `mixins`.

> [!NOTE]
> You should create a folder in `bot/infrastructure/db` with name 
> `repository or mixins`.

#### Infrastructure
In folder `infrastructure` must be third party integrations.

[!NOTE]
> If you want to add cache with Redis, you create
> folder in infrastructure with name `cache`.
> Also in directory infrastructure must be folder `brokers` for
> RabbitMQ/Kafka.

In directory `http` must be integrations with other APIs. Also
folder `http` having `webhook`.

#### Logging
For every service, which you want logging you must be
create new `property` in class `FactoryBaseLogger`.

For example. How right create `property`. Let's imagine, if you want
add logging for `webhook`.

```python
class FactoryBaseLogger:

    @property
    def webhook(self) -> BaseLogger:
        return BaseLogger(
            name="WEBHOOK",
            filename=f"data/logs/webhook/{self.__current_day()}.txt"
        )
```
=======
Aiogram bot template with Webhook, SQLAlchemy, Admin, Logging
>>>>>>> ce19421d4bc71257ca1e8f482af7fca0f8011de5
