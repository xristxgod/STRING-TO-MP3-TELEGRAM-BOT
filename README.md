The talking bot
=======

> The bot converts your words into an audio file.

Run bot:
```shell
# <<<====================>>> CMD <<<=======================>>>

# Run the bot with a token from the .env file.
python3 ./app.py
# Run the bot with the token indication via the console.
python3 ./app.py --token yourBotToken
python3 ./app.py -t yourBotToken

# <<<====================>>> Docker <<<====================>>>

# Run by docker
docker-compose --file ./bot-docker-compose.yml up --build
# Stop docker
docker-compose --file ./bot-docker-compose.yml stop

# <<<====================>>> Bush <<<====================>>>

# Run by bush
bush ./run.sh
# Stop bush
bush ./stop.sh
```

                                        Example of work:

![test_message](https://user-images.githubusercontent.com/84931791/166212815-7221b5d7-efa8-4e68-9a14-98ae2be97cfc.png)