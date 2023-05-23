from pyrogram import Client, filters, enums
api_id = 'YOUR_ID'
api_hash = 'YOUR HASH'
app = Client('YOUR ACCOUNT TITLE', api_id, api_hash)
app.set_parse_mode(enums.ParseMode.HTML)


@app.on_message(filters.me & filters.command('CHAT',prefixes='@'))
async def history(client, message):
    # Split message to get id
    id_user = str(message.text).split('@history_group ')[-1]
    users_information = []
    user_id_str = 'This is all user\'s  id\n'
    async for member in app.get_chat_members(f'-100{id_user}'):
        user_id_str += f"{member.user.id}\n"
        users_information.append(member)

    await app.send_message(chat_id=message.chat.id, text=str(user_id_str))
    await app.send_message(chat_id=message.chat.id,text=f"Number of users: {len(users_information)}")

# This function is made in order to get some association to our session
@app.on_message(filters.incoming)
async def hello(client, message):
    print(message.text)
app.run()

