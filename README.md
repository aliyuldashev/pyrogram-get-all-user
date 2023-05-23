# Pyrogram Telegram Bot

This Telegram bot built with Pyrogram retrieves user IDs and information when the user enters the command "/CHAT". It provides an easy way to fetch user IDs and access user information.

## Usage

1. Start the bot and add get into the group, channel or whatever chat you want.
2. Type command @CHAT" and chat id to trigger the bot.
3. The bot will retrieve the all user's IDs and information of all the participants in the group or channel.

## Important Note

Inside the code, there is a variable named `users_information` that contains all the users' information. By default, it is not returned as part of the bot's response. However, if you want to access this information within the script, you can access to this variable inside of script or modify the code as needed.

Please exercise caution when handling users' information and ensure compliance with privacy and data protection regulations.

Here the format of data this variable have 
```
users_information = {
    "_": "ChatMember",
    "status": "ChatMemberStatus.MEMBER",
    "user": {
        "_": "User",
        "id": *****,
        "is_self": False,
        # Hide other user information fields by removing or replacing them
        "first_name": "*****",
        "username": "*****",
        "photo": {
            "_": "ChatPhoto",
            "small_file_id": "*****",
            "small_photo_unique_id": "*****",
            "big_file_id": "*****",
            "big_photo_unique_id": "*****"
        }
    },
    "joined_date": "2023-02-10 11:48:49"
}
```
Please exercise caution when handling users' information and ensure compliance with privacy and data protection regulations.

## Requirements

- Python 3.7 or higher
- Pyrogram library

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies by running the following command: 
```
pip install pyrogram
```

3. clone repository 
``` 
git clone 
```
4. Get your application inforamtion from [telegram applications](https://my.telegram.org/apps)
5. Add your Application into script 
``` 
api_id = 'YOUR_ID'
api_hash = 'YOUR HASH'
app = Client('YOUR ACCOUNT TITLE', api_id, api_hash)
```
6. Run the code
7. Log into your telegram account
8. Give command and chat id that you want to get user's informations by the telegram in this format``` @CHAT ********* ```
