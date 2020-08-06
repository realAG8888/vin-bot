# LINK TO READD THE BETA BOT TO THE SERVER
# https://discordapp.com/oauth2/authorize?client_id=737475841700790402&scope=bot&permissions=2146958847

import discord
from discord.ext import commands
import random
import pandas as pd
from profanity import profanity

## BOT INFORMATION

bot_name = 'Vin'

current_version = "Version 2.0.0"
current_version_release = "Aug 1, 2020"
current_version_desc = "**Many things have been added and changed in Vin Version 2.0.0!**\n"
current_version_desc += "- ***ACHIEVMENTS!*** **Earn secret achievments for completeing certain actions. Can you find them all?**\n"
current_version_desc += "- Run the **Vin command** to get a menu regarding your stats as a DM! Use ~~vin to run it.\n"
current_version_desc += "- Vin has been **COMPLETELY RECODED** for **ease of use and simplicity**.\n"
current_version_desc += "- The commands system has been **completely revamped** and **many commands have been added**.\n"
current_version_desc += "- The custom responses system has been recoded to **ensure a response to everyone**.\n"
current_version_desc += "- **Weightings** have been added to custom responses, so those who are online less will have more chance for a custom response.\n"
current_version_desc += "- Greetings, responses, etc are now part of csv files rather than Python arrays.\n"
current_version_desc += "- **Vin now plays various games when he is idle!**\n"
current_version_desc += "- Vin now **no longer responds in the school category**.\n"
current_version_desc += "- Vin now responds when users **join or leave** the server.\n"
current_version_desc += "- **Vin now responds to mentions! Mention Vin in a conversation to see!**\n"
current_version_desc += "- Vin now responds to mentions containing the word **'sorry' now!**\n"
current_version_desc += "- ***Added fun easter eggs! Which ones can you find?***\n"

previous_version_descriptions = """
**Version 1.0.0**
> This is release version of the Vin Bot!
"""

## USER INFORMATION

ajay = 645465167412461599
jade = 273203032743739392
chris = 540624764658647072
haip = 720026590167171205
emil = 284072515746136064
magg = 321039483577565187
will = 662710804696793089

devs = [ajay, haip, emil]


# Data Prep Function

def convertCsvToList(df):

    list = []
    for index, row in df.iterrows():
        list.append(row[0])

    return list

#######################################################################################################################

# INITIALIZE BOT

client = commands.Bot(command_prefix="~~")

#######################################################################################################################

# CONNECT BOT COMMANDS


## ~~COMMANDS
 # Provides a list of verified commands for users to call.
@client.command(name='commands')
async def commands(context):
    bot_debug_panel = context.channel
    hp = '__**BOT HELP CENTER**__\n'
    hp += "__**Legend:**__\n"
    hp += '🔹 - Normal Command   🔸 - Command Requires Admin Status.   🔧 - W.I.P.\n'
    hp += "__**General Commands:**__\n"
    hp += "🔹 **commands:** List all commands available\n"
    hp += "🔹 **version:** Display Vin Version Information\n"
    hp += "🔹 **vin:** Open Vin Menu\n"
    hp += "__**Vin Commands:**__\n"
    hp += "🔸 **v.changegameplaying \"Game Name\":** Changes the game Vin is currently playing as custom status\n"
    hp += "__**Greetings Commands:**__\n"
    hp += "🔸 **g.all:** View all greetings.\n"
    hp += "🔸 **g.send:** Sends a greeting to general.\n"
    hp += "🔸 **g.add \"new greeting here\":** Adds a new greeting.\n"
    hp += "🔸 **g.delete num:** Delete a greeting at specified number\n"
    hp += "__**Responses Commands:**__\n"
    hp += "🔸 **r.all \"irl name\":** View all responses. To see responses for everyone only, leave name blank. To see for person, but real life name in quotes.\n"
    hp += "🔸 **r.add \"irl name\" \"new greeting here\":** Adds a new response. NOTE: use 'all' as irl name to add a response for all\n"
    hp += "🔸 **r.delete \"irl name\" num:** Delete a greeting at specified number.\n"

    await bot_debug_panel.send(hp)
    await context.message.delete()

## VIN

@client.command(name='vin')
async def vincommand(context):

    text = "__**Vin Menu**__\n"
    text += "Hello! Please choose one of the following options to proceed!\n"
    text += "🎉 - View Achievments"

    message = await context.message.author.send(text)
    await message.add_reaction("🎉")


## ~~VIN STATUS
 # Changes Vin's Status

@client.command(name='v.changegameplaying')
async def vchangegameplaying(context, game):
    if context.message.author.id in devs:
        channel_to_send = client.get_channel(730855010547662919)
        await client.change_presence(activity=discord.Game(name=game))
        await channel_to_send.send("Hi! I am now playing " + game + "!")
        await context.message.delete()
    else:
        await context.message.channel.send("You do not have permission to use this command.")

## ~~GREETING
 # Provides options regarding greetings

@client.command(name="g.send")
async def sendgreeting(context):
    if context.message.author.id in devs:
        channel_to_send = client.get_channel(730873319741456435)
        greetings_df = pd.read_csv('data/randomized_greetings/greetings.csv', sep=',', header=None)

        greetings_list = convertCsvToList(greetings_df)

        await channel_to_send.send(random.choice(greetings_list))
        await context.message.channel.send("A random greeting has been sent!")
    else:
        await context.message.channel.send("You do not have permission to use this command.")

@client.command(name="g.add")
async def addgreeting(context, greeting):
    if context.message.author.id in devs:

        greetings_df = pd.read_csv('data/randomized_greetings/greetings.csv', sep=',', header=None)

        greetings_df = greetings_df.append([greeting])
        greetings_df.to_csv('data/randomized_greetings/greetings.csv', index=False, header=False)
        await context.message.channel.send("Your new greeting has been added!")

    else:
        await context.message.channel.send("You do not have permission to use this command.")

@client.command(name="g.all")
async def allgreetings(context):
    if context.message.author.id in devs:

        greetings_df = pd.read_csv('data/randomized_greetings/greetings.csv', sep=',', header=None)

        allgreetingstext = "__**All Greetings**__\n"

        for index, row in greetings_df.iterrows():
            allgreetingstext += (str(index + 1) + ". ")
            allgreetingstext += str(row[0])
            allgreetingstext += "\n"

        allgreetingstext += "**To Delete a Greeting, type the comand ~~g.delete followed by the number of greeting to delete.**\n"
        allgreetingstext += "**For example to delete item 2, type ~~g.delete 2 in chat.**"

        await context.message.channel.send(allgreetingstext)

    else:
        await context.message.channel.send("You do not have permission to use this command.")

@client.command(name="g.delete")
async def deletegreeting(context, num):
    if context.message.author.id in devs:

        greetings_df = pd.read_csv('data/randomized_greetings/greetings.csv', sep=',', header=None)

        greetings_df = greetings_df.drop([int(num)-1])

        print(greetings_df)

        greetings_df.to_csv('data/randomized_greetings/greetings.csv', index=False, header=False)

        await context.message.channel.send("The greeting has been deleted.")

    else:
        await context.message.channel.send("You do not have permission to use this command.")

## ~~RESPONSES
 # Provides options regarding greetings

@client.command(name="r.all")
async def allresponses(context, name=""):

    if context.message.author.id in devs:

        all_df = pd.read_csv('data/randomized_responses/random_responses_all.csv', sep=',', header=None)
        ajay_df = pd.read_csv('data/randomized_responses/ajay_custom_responses.csv', sep=',', error_bad_lines=False, header=None)
        chris_df = pd.read_csv('data/randomized_responses/chris_custom_responses.csv', sep=',', header=None)
        emil_df = pd.read_csv('data/randomized_responses/emil_custom_responses.csv', sep=',', header=None)
        haip_df = pd.read_csv('data/randomized_responses/haip_custom_responses.csv', sep=',', header=None)
        jade_df = pd.read_csv('data/randomized_responses/jade_custom_responses.csv', sep=',', header=None)
        will_df = pd.read_csv('data/randomized_responses/will_custom_responses.csv', sep=',', header=None)
        magg_df = pd.read_csv('data/randomized_responses/magg_custom_responses.csv', sep=',', header=None)

        allresponsestext = ""

        if name != None and name.lower() not in ['', 'ajay', 'christine', 'emily','haipei','jaden','william','maggie']:
            await context.message.channel.send("Name not found! Try again.")
            return

        if name == None or name == "":
            allresponsestext = "__**All Responses**__\n"
            for index, row in all_df.iterrows():
                allresponsestext += (str(index + 1) + ". ")
                allresponsestext += str(row[0])
                allresponsestext += "\n"
        if name.lower() == "ajay":
            allresponsestext = "__**Ajay Responses**__\n"
            for index, row in ajay_df.iterrows():
                allresponsestext += (str(index + 1) + ". ")
                allresponsestext += str(row[0])
                allresponsestext += "\n"
        if name.lower() == "christine":
            allresponsestext = "__**Christine Responses**__\n"
            for index, row in chris_df.iterrows():
                allresponsestext += (str(index + 1) + ". ")
                allresponsestext += str(row[0])
                allresponsestext += "\n"
        if name.lower() == "emily":
            allresponsestext = "__**Emily Responses**__\n"
            for index, row in emil_df.iterrows():
                allresponsestext += (str(index + 1) + ". ")
                allresponsestext += str(row[0])
                allresponsestext += "\n"
        if name.lower() == "haipei":
            allresponsestext = "__**Haipei Responses**__\n"
            for index, row in haip_df.iterrows():
                allresponsestext += (str(index + 1) + ". ")
                allresponsestext += str(row[0])
                allresponsestext += "\n"
        if name.lower() == "jaden":
            allresponsestext = "__**Jaden Responses**__\n"
            for index, row in jade_df.iterrows():
                allresponsestext += (str(index + 1) + ". ")
                allresponsestext += str(row[0])
                allresponsestext += "\n"
        if name.lower() == "william":
            allresponsestext = "__**William Responses**__\n"
            for index, row in will_df.iterrows():
                allresponsestext += (str(index + 1) + ". ")
                allresponsestext += str(row[0])
                allresponsestext += "\n"
        if name.lower() == "maggie":
            allresponsestext = "__**Maggie Responses**__\n"
            for index, row in magg_df.iterrows():
                allresponsestext += (str(index + 1) + ". ")
                allresponsestext += str(row[0])
                allresponsestext += "\n"

        allresponsestext += "**To Delete a Reponse, type the comand ~~r.delete followed by the irl name then number of greeting to delete.**\n"
        allresponsestext += "**For example to delete item 2 for Jaden, type ~~r.delete \"Jaden\" 2 in chat.**"

        await context.message.channel.send(allresponsestext)

    else:
        await context.message.channel.send("You do not have permission to use this command.")

@client.command(name="r.add")
async def addresponses(context, name, response):

    if context.message.author.id in devs:

        all_df = pd.read_csv('data/randomized_responses/random_responses_all.csv', sep=',', header=None)
        ajay_df = pd.read_csv('data/randomized_responses/ajay_custom_responses.csv', sep=',', error_bad_lines=False, header=None)
        chris_df = pd.read_csv('data/randomized_responses/chris_custom_responses.csv', sep=',', header=None)
        emil_df = pd.read_csv('data/randomized_responses/emil_custom_responses.csv', sep=',', header=None)
        haip_df = pd.read_csv('data/randomized_responses/haip_custom_responses.csv', sep=',', header=None)
        jade_df = pd.read_csv('data/randomized_responses/jade_custom_responses.csv', sep=',', header=None)
        will_df = pd.read_csv('data/randomized_responses/will_custom_responses.csv', sep=',', header=None)
        magg_df = pd.read_csv('data/randomized_responses/magg_custom_responses.csv', sep=',', header=None)

        allresponsestext = ""

        if name != None and name.lower() not in ['all', 'ajay', 'christine', 'emily','haipei','jaden','william','maggie']:
            await context.message.channel.send("Name not found! Try again Use 'all' as the name for this command to add a response for all!")
            return

        if name.lower() == "all":
            all_df = all_df.append([response])
            all_df.to_csv('data/randomized_responses/random_responses_all.csv', index=False, header=False)
            await context.message.channel.send("Your new response has been added for all people!")

        if name.lower() == "ajay":
            ajay_df = ajay_df.append([response])
            ajay_df.to_csv('data/randomized_responses/ajay_custom_responses.csv', index=False, header=False)
            await context.message.channel.send("Your new response has been added for Ajay!")
        if name.lower() == "christine":
            chris_df = chris_df.append([response])
            chris_df.to_csv('data/randomized_responses/chris_custom_responses.csv', index=False, header=False)
            await context.message.channel.send("Your new response has been added for Christine!")
        if name.lower() == "emily":
            emil_df = emil_df.append([response])
            emil_df.to_csv('data/randomized_responses/emil_custom_responses.csv', index=False, header=False)
            await context.message.channel.send("Your new response has been added for Emily!")
        if name.lower() == "haipei":
            haip_df = haip_df.append([response])
            haip_df.to_csv('data/randomized_responses/haip_custom_responses.csv', index=False, header=False)
            await context.message.channel.send("Your new response has been added for Haipei!")
        if name.lower() == "jaden":
            jade_df = jade_df.append([response])
            jade_df.to_csv('data/randomized_responses/jade_custom_responses.csv', index=False, header=False)
            await context.message.channel.send("Your new response has been added for Jaden!")
        if name.lower() == "william":
            will_df = will_df.append([response])
            will_df.to_csv('data/randomized_responses/will_custom_responses.csv', index=False, header=False)
            await context.message.channel.send("Your new response has been added for William!")
        if name.lower() == "maggie":
            magg_df = magg_df.append([response])
            magg_df.to_csv('data/randomized_responses/magg_custom_responses.csv', index=False, header=False)
            await context.message.channel.send("Your new response has been added for Maggie!")

    else:
        await context.message.channel.send("You do not have permission to use this command.")


@client.command(name="r.delete")
async def deleteresponses(context, name, num):

    if context.message.author.id in devs:

        all_df = pd.read_csv('data/randomized_responses/random_responses_all.csv', sep=',', header=None)
        ajay_df = pd.read_csv('data/randomized_responses/ajay_custom_responses.csv', sep=',', error_bad_lines=False, header=None)
        chris_df = pd.read_csv('data/randomized_responses/chris_custom_responses.csv', sep=',', header=None)
        emil_df = pd.read_csv('data/randomized_responses/emil_custom_responses.csv', sep=',', header=None)
        haip_df = pd.read_csv('data/randomized_responses/haip_custom_responses.csv', sep=',', header=None)
        jade_df = pd.read_csv('data/randomized_responses/jade_custom_responses.csv', sep=',', header=None)
        will_df = pd.read_csv('data/randomized_responses/will_custom_responses.csv', sep=',', header=None)
        magg_df = pd.read_csv('data/randomized_responses/magg_custom_responses.csv', sep=',', header=None)

        allresponsestext = ""

        if name != None and name.lower() not in ['all', 'ajay', 'christine', 'emily','haipei','jaden','william','maggie']:
            await context.message.channel.send("Name not found! Try again Use 'all' as the name for this command to add a response for all!")
            return

        if name.lower() == "all":
            all_df = all_df.drop([int(num)-1])
            all_df.to_csv('data/randomized_responses/random_responses_all.csv', index=False, header=False)
        if name.lower() == "ajay":
            ajay_df = ajay_df.drop([int(num)-1])
            ajay_df.to_csv('data/randomized_responses/ajay_custom_responses.csv', index=False, header=False)
        if name.lower() == "christine":
            chris_df = chris_df.drop([int(num)-1])
            chris_df.to_csv('data/randomized_responses/chris_custom_responses.csv', index=False, header=False)
        if name.lower() == "emily":
            emil_df = emil_df.drop([int(num)-1])
            emil_df.to_csv('data/randomized_responses/emil_custom_responses.csv', index=False, header=False)
        if name.lower() == "haipei":
            haip_df = haip_df.drop([int(num)-1])
            haip_df.to_csv('data/randomized_responses/haip_custom_responses.csv', index=False, header=False)
        if name.lower() == "jaden":
            jade_df = jade_df.drop([int(num)-1])
            jade_df.to_csv('data/randomized_responses/jade_custom_responses.csv', index=False, header=False)
        if name.lower() == "william":
            will_df = will_df.drop([int(num)-1])
            will_df.to_csv('data/randomized_responses/will_custom_responses.csv', index=False, header=False)
        if name.lower() == "maggie":
            magg_df = magg_df.drop([int(num)-1])
            magg_df.to_csv('data/randomized_responses/magg_custom_responses.csv', index=False, header=False)

        await context.message.channel.send("Response has been deleted!")

    else:
        await context.message.channel.send("You do not have permission to use this command.")


@client.command(name="cleardebugbeta")
async def clear_debug_beta(context):

    msgs = []
    number = 99

    async for x in client.get_user(645465167412461599).history(limit=number):
        if x.author.id == client.user.id:
            msgs.append(x)

    await context.message.channel.delete_messages(msgs)


@client.command(name='version')
async def version(context):
    embed = discord.Embed(title="" + bot_name + "Bot Version Information", colour=discord.Colour.blurple())
    # embed.set_author(name=bot_name)
    embed.add_field(name='Current Version:', value=current_version, inline=True)
    embed.add_field(name='Release:', value=current_version_release, inline=True)
    embed.add_field(name='Current Version Description:', value=current_version_desc, inline=False)
    embed.add_field(name='Version History:', value=previous_version_descriptions, inline=False)

    await context.message.channel.send(embed=embed)
    await context.message.delete()

@client.command(name='sendnewversioninfo')
async def sendnewversioninfo(context):

    await context.message.channel.send("Hello everyone! It is me, Vin! Ajay updated me, so I am back online with many new changes!")
    await context.message.channel.send("I am now on " + current_version + "!")
    await context.message.channel.send("__**CHANGELOG**__\n" + current_version_desc)


#######################################################################################################################


## CONNECT BOT EVENTS

# RUNS WHEN BOT GETS ONLINE
@client.event
async def on_ready():
    channel = client.get_channel(736965051319058494)
    await channel.send('The bot has been restarted!')
    await client.change_presence(activity=discord.Game(name=random.choice(['Minecraft', 'Stardew Valley', 'Terraria', 'Animal Crossing: New Horizons', 'Monopoly', 'Chess'])))

## RUNS WHEN MESSAGE SENT:

@client.event
async def on_message(message):

    # Achievments
    if "*dab" in message.content.lower():
        await earn_achievment(message, 0)
    if client.user in message.mentions:
        await earn_achievment(message, 1)
    if profanity.contains_profanity(message.content):
        await earn_achievment(message, 3)
    if ":fire:" in message.content.lower():
        await earn_achievment(message, 4)
    if message.mention_everyone:
        await earn_achievment(message, 6)
    if "genes" in message.content.lower():
        await earn_achievment(message, 7)
    if "dorime" in message.content.lower():
        await earn_achievment(message, 8)
    if ":hrcn:" in message.content.lower():
        await earn_achievment(message, 9)
    if "uwu" in message.content.lower():
        await earn_achievment(message, 10)

    # Easter eggs
    if ";D" in message.content and message.author.id != client.user.id:
        await earn_achievment(message, 5)
        await message.channel.send(";D")
    elif ":wink:" in message.content and message.author.id != client.user.id:
        await message.channel.send(";D")
        await earn_achievment(message, 5)
    elif "*dab" in message.content and message.author.id != client.user.id:
        await message.channel.send("You go! Dab on em haters!! :D")
    elif client.user in message.mentions:
        if "sorry" in message.content.lower():
            await message.channel.send("It's ok! No worries :upside_down:")
        else:
            await message.channel.send(random.choice(['Are you talking about me? :blush:', 'Hello! :grinning:', 'Hi, I am still here playing a game!!']))

    if message.channel.category_id != 733821799774552065:

        all_df = pd.read_csv('data/randomized_responses/random_responses_all.csv', sep=',', header=None)
        ajay_df = pd.read_csv('data/randomized_responses/ajay_custom_responses.csv', sep=',', error_bad_lines=False, header=None)
        chris_df = pd.read_csv('data/randomized_responses/chris_custom_responses.csv', sep=',', header=None)
        emil_df = pd.read_csv('data/randomized_responses/emil_custom_responses.csv', sep=',', header=None)
        haip_df = pd.read_csv('data/randomized_responses/haip_custom_responses.csv', sep=',', header=None)
        jade_df = pd.read_csv('data/randomized_responses/jade_custom_responses.csv', sep=',', header=None)
        will_df = pd.read_csv('data/randomized_responses/will_custom_responses.csv', sep=',', header=None)
        magg_df = pd.read_csv('data/randomized_responses/magg_custom_responses.csv', sep=',', header=None)

        rng_num = 0

        if message.author.id in [will]:
            rng_num = random.randint(1, 30)  # Chance for random - 1/30
        if message.author.id in [emil, magg]:
            rng_num = random.randint(1, 40)  # Chance for random - 1/40
        if message.author.id in [chris, jade, ajay, haip]:
            rng_num = random.randint(1, 45)  # Chance for random - 1/45

        if rng_num == 2:

            print('custom msg triggered')
            rng_num_two = 0

            if message.author.id in [will]:
                rng_num_two = random.randint(1, 2)  # Chance for random - 1/2
            if message.author.id in [emil, magg]:
                rng_num_two = random.randint(1, 2)  # Chance for random - 1/2
            if message.author.id in [chris, jade, ajay, haip]:
                rng_num_two = random.randint(1, 3)  # Chance for random - 1/3

            if rng_num_two == 2:
                if message.author.id == ajay:
                    await message.channel.send(random.choice(convertCsvToList(ajay_df)))
                if message.author.id == jade:
                    await message.channel.send(random.choice(convertCsvToList(jade_df)))
                if message.author.id == chris:
                    await message.channel.send(random.choice(convertCsvToList(chris_df)))
                if message.author.id == haip:
                    await message.channel.send(random.choice(convertCsvToList(haip_df)))
                if message.author.id == emil:
                    await message.channel.send(random.choice(convertCsvToList(emil_df)))
                if message.author.id == will:
                    await message.channel.send(random.choice(convertCsvToList(will_df)))
                if message.author.id == magg:
                    await message.channel.send(random.choice(convertCsvToList(magg_df)))
            else:
                await message.channel.send(random.choice(convertCsvToList(all_df)))

        await client.process_commands(message)

## RUNS WHEN MEMEBERS JOIN / QUIT:

@client.event
async def on_member_join(member):
    channel_to_send = client.get_channel(730855010547662919)
    await channel_to_send.send("Welcome to the Froptical Society, " + member.name + "! It is nice to meet you!")

@client.event
async def on_member_remove(member):
    channel_to_send = client.get_channel(730855010547662919)
    await channel_to_send.send("We will miss you, " + member.name + "! Please come back again soon!")

# ON INTERACT
@client.event
async def on_reaction_add(reaction, user):

    # Achievments
    if reaction.message.author.id == ajay and reaction.message.channel.id == 730856245598224535:
        await earn_achievment(reaction.message, 2)

    if user != client.user and reaction.message.content.startswith("__**Vin Menu**__"):
        if reaction.emoji == '🎉':

            ach_df = pd.read_csv('data/achievments/achievments.csv', sep=',')

            await user.send('__**Your Achievments**__')

            achievmenttext = ""

            for index, row in ach_df.iterrows():
                if user.id == ajay and row['ajay'] == 'y':
                    achievmenttext += "**:sparkles: " + row['Name'] + "** - " + row["Description"] + '\n'
                if user.id == jade and row['jaden'] == 'y':
                    achievmenttext += "**:sparkles: " + row['Name'] + "** - " + row["Description"] + '\n'
                if user.id == haip and row['haipei'] == 'y':
                    achievmenttext += "**:sparkles: " + row['Name'] + "** - " + row["Description"] + '\n'
                if user.id == chris and row['christine'] == 'y':
                    achievmenttext += "**:sparkles: " + row['Name'] + "** - " + row["Description"] + '\n'
                if user.id == emil and row['emily'] == 'y':
                    achievmenttext += "**:sparkles: " + row['Name'] + "** - " + row["Description"] + '\n'
                if user.id == will and row['william'] == 'y':
                    achievmenttext += "**:sparkles: " + row['Name'] + "** - " + row["Description"] + '\n'
                if user.id == magg and row['maggie'] == 'y':
                    achievmenttext += "**:sparkles: " + row['Name'] + "** - " + row["Description"] + '\n'

            if achievmenttext == "":
                achievmenttext = "*You have no achievments yet.*"

            await user.send(achievmenttext)


## ACHEIVMENT FUNC
async def earn_achievment(message, achievmentnum):

    ach_df = pd.read_csv('data/achievments/achievments.csv', sep=',')


    text = "**[:tada:] " + message.author.name + " Unlocked an Achievment!**\n"
    text += '-- :sparkles:' + str(ach_df['Name'][int(achievmentnum)]) + ':sparkles: --\n\n'
    text += "@everyone Send Congrats to " + message.author.name + " by tapping the reaction!\n"
    text += "*To see your acheivments, run the ~~vin command and follow the directions.*"

    if message.author.id == ajay:
        if ach_df['ajay'][int(achievmentnum)] == 'y':
            return
        else:
            ach_df['ajay'][int(achievmentnum)] = "y"

    if message.author.id == jade:
        if ach_df['jaden'][int(achievmentnum)] == 'y':
            return
        else:
            ach_df['jaden'][int(achievmentnum)] = "y"

    if message.author.id == haip:
        if ach_df['haipei'][int(achievmentnum)] == 'y':
            return
        else:
            ach_df['haipei'][int(achievmentnum)] = "y"

    if message.author.id == chris:
        if ach_df['christine'][int(achievmentnum)] == 'y':
            return
        else:
            ach_df['christine'][int(achievmentnum)] = "y"

    if message.author.id == emil:
        if ach_df['emily'][int(achievmentnum)] == 'y':
            return
        else:
            ach_df['emily'][int(achievmentnum)] = "y"

    if message.author.id == will:
        if ach_df['william'][int(achievmentnum)] == 'y':
            return
        else:
            ach_df['william'][int(achievmentnum)] = "y"

    if message.author.id == magg:
        if ach_df['maggie'][int(achievmentnum)] == 'y':
            return
        else:
            ach_df['maggie'][int(achievmentnum)] = "y"

    print(ach_df)

    ach_df.to_csv('data/achievments/achievments.csv', index=False)

    achievmentchannel = client.get_channel(739222630627803166)

    message = await achievmentchannel.send(text)
    await message.add_reaction('🎉')


client.run('NzM3NDc1ODQxNzAwNzkwNDAy.Xx955g.6sHjKxxhb5g-CPXNSbGT_K8Ab-M')
