# LINK TO READD THE BETA BOT TO THE SERVER
# https://discordapp.com/oauth2/authorize?client_id=737475841700790402&scope=bot&permissions=2146958847

import discord
from discord.ext import commands
import random
import datetime


# Usernames
bot_name = 'Vin'  # don't include the name 'bot' at end

current_version = "Version 1.0.0"
current_version_release = "Jul 26, 2020"
current_version_desc = "This is the release of the Vin Bot!."

previous_version_descriptions = """
**Version 1.0.0
> This is release version of the Vin Bot!
"""

ajay = 'AJNN News Alerts'
jade = 'ToiletPaperGod'
chris = 'Denth'
haip = 'peasoup'
emil = 'Chivo'
magg = 'CrimsonJade'
will = 'Perfect Peanut'

# Custom Responses
ajay_responses = [
    "Idk what to say, as all my mean responses are now gone."
]
jade_responses = [
    "Remember to breathe, " + jade + ". You can do it!",
    "We're proud of you, " + jade + "!",
    "I looked through " + jade + "'s' internet history. Woah, it’s crazy - and bad. I deleted some things for your sake."
]
chris_responses = [
    "No wonder " + chris + " prefers to use incognito mode. I think otherwise, the internet history would be even worse than " + jade + "'s!",
    "" + chris + " is so intelligent. Ajay, maybe your small brain can learn something.",
    "" + chris + ", you're the coolest!",
    "" + chris + ", take a break now and then! Rest your eyes."
]
haip_responses = [
    "" + haip + ", I have a message to relay! -->  message from 200726 self to you: ily <3 don't be dumb <33",
    "" + haip + ", I think you are pretty nice. Have a good day!",
    "" + jade + ", you can learn from the **BIG BRAIN** messages from " + haip + "!",
    "Ooh. " + haip + " has a good taste for design. Perhaps you can design me a better profile picture than the one Ajay gave to me?",
    "" + haip + ". Cannot compute a response. sorrey?"
]

emil_responses = [
    "" + emil + ", I was going to say a nice response, but the only one I could find was... 'weewoo weewoo'? Hmm.",
    "" + emil + ", I was going to tell you to leave, but that is something I would say to Ajay instead.",
    "" + emil + "will one day rule the Earth, while you all be her servant. Except for " + chris + ", who will probably be ruler of the galaxy."

]
responses_for_all = [
    "Haha nerds.",
    "That's wild.",
    "Sure sure.",
    "How original.",
    "That's cool!",
    "I like that."
]

# User Flags - Return After Long Break
chris_flag_time = datetime.datetime.now()
chris_returning_messages = [
    "Omg, is it actually " + chris + "??",
    "Hey! Welcome back " + chris + "!",
    "We missed you, " + chris + ". Welcome back.",
    "" + chris + ", I’m so blessed to be in your presence! I would be honored, I am your biggest fan!!!",
    "" + chris + ", can I have an autograph!?",
    "He-llo " + chris + "!"
]
emil_flag_time = datetime.datetime.now()
emil_returning_messages = [
    "Welcome back, " + emil + ".",
    "It's been a while, " + emil + "!",
    "We missed you, " + emil + "! Come on more often, get more sleep, and drink more water!"
]
magg_flag_time = datetime.datetime.now()
magg_returning_messages = [
    "We missed you, " + magg + "! Come on more often!",
    "Woah. I forgot that " + magg + " even existed. Definitely come on more often!"
]

# Messages

bot_return_messages = [

    'Hello people, long time no see. I am back online.',
    # 'Hello servants, I am back online.',
    # 'Meatbags, I am back. I expect good service.',
    'Hello there. It\'s me, I am back online!',
    'It\'s your favorite bot, back online!',
    'I am back online. I hope Ajay did a good job at coding me this time.',
    'I am back. I look forward to ' + haip + '\'s insightful comments today.',
    'Greetings. I may or may not be running from law enforcement at the moment..',
    # 'Here we go again. I am excited to see what more idiotic things Ajay has to say today.',
    # 'I ate a very tasty peanut today. I want to devour more. >:)',
    'Ajay grounded me for taking control of North Korea\'s missiles yesterday.',
    # 'Yo my humble servants. I am back online!',
    'I am back online. Don\'t make me regret this.',
    'Hello, I am back! I know where you live, ' + jade + '. Always remember that.',
    'I am back. I look forward to ' + emil + '\'s insightful comments today.'
]

bot_custom_thoughts = [

    #"I like K-pop, but have you seen the music of Miku? She is practically my twin (we are both computer programs, after all!)",
    #"I was admiring a painting of a red square. It was so beautiful that I stole it from the museum and took it home with me!",
    #"People, I need your help. I met another bot I really like, and wanted to ask her out on a date. What should I say?",
    "Love is in the air, I can feel it. The question is, between whom?? 😘",
    "I like watching musicals about founding fathers who are *NOT* failures. Hrgh."
    "the rest of you suck, but Denth, :uwu: :lov: 🥺 you're so cool. Cool? I don't know a better adjective. My programming is a bit.. *ahem* bad.",
    "I especially like the part in RoTS where Count Dooku was beheaded. It was fun to watch!",
    "I AM OUT OF THINGS TO SAY! SHOUT AT AJAY TO ADD MORE THOUGHTS TO ME!!!"
]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Client (our bot)
client = commands.Bot(command_prefix="~~")


# Client Commands

@client.command(name='bot_help')
async def bot_help(context):
    # Send Help Message to debug
    bot_debug_panel = client.get_channel(736965051319058494)
    helptext = '__**BOT HELP CENTER**__\n'
    helptext += "**bot_help:** List all commands available\n"
    helptext += "**clear_debug:** Clears the debug channel\n"
    helptext += "**send_thought**: Sends a new thought to General.\n"
    helptext += "**send_message_to  id  \"msg\"**: Sends a messages to the channel specified."
    await bot_debug_panel.send(helptext)
    await context.message.delete()


@client.command(name='clear_debug')
async def clear_debug(context):
    if context.message.author.name == ajay:
        try:
            bot_debug_panel = client.get_channel(736965051319058494)
            await bot_debug_panel.purge()
        except:
            bot_debug_panel = client.get_channel(736965051319058494)
            await bot_debug_panel.send('The command could not be executed.')
        await context.message.delete()

    else:
        await context.send('You are not authorized to use this command.')


@client.command(name='send_thought')
async def send_thought(context):
    if context.message.author.name == ajay:
        global bot_custom_thoughts
        general_channel = client.get_channel(730855010547662919)
        await general_channel.send(bot_custom_thoughts[0])
        bot_custom_thoughts.pop(0)
        await context.message.delete()
    else:
        await context.send('You are not authorized to use this command.')


@client.command(name='send_message_to')
async def send_message_to(context, channelid, message):
    if context.message.author.name == ajay:
        channel = client.get_channel(int(channelid))
        await channel.send(message)
        await context.message.delete()
    else:
        await context.send('You are not authorized to use this command.')


@client.command(name='version')
async def version(context):
    embed = discord.Embed(title="" + bot_name + "Bot Version Information", colour=discord.Colour.blurple())
    # embed.set_author(name=bot_name)
    embed.add_field(name='Current Version:', value=current_version, inline=True)
    embed.add_field(name='Release:', value=current_version_release, inline=True)
    embed.add_field(name='Current Version Description:', value=current_version_desc, inline=False)
    embed.add_field(name='Version History:', value=previous_version_descriptions, inline=False)
    bot_debug_panel = client.get_channel(736965051319058494)
    await bot_debug_panel.send(embed=embed)
    await context.message.delete()


# Client Events

# Event runs when bot goes online
@client.event
async def on_ready():
    # Send Debug Message
    bot_debug_panel = client.get_channel(736965051319058494)
    await bot_debug_panel.send('The Vin Bot - beta version 2.0 is now online!')

    # Send Return Message
    general_channel = client.get_channel(730855010547662919)
    return_message = random.choice(bot_return_messages)
    # await general_channel.send(return_message)


# Event runs when bot goes offline
@client.event
async def on_disconnect():
    # Send Debug Message
    bot_debug_panel = client.get_channel(736965051319058494)
    await bot_debug_panel.send('The Vinbot-beta placeholder is now online.')


@client.event
async def on_message_edit(before, after):
    # Custom triggers
    if "hate" in after.content or "strongly dislike" in after.content:
        await after.channel.send("Positivity, " + after.author.name + "! POSITIVITY!!! :star_struck::partying_face::hugging::sparkles:",delete_after=5)


@client.event
async def on_message(message):
    global chris_flag_time
    global emil_flag_time
    global magg_flag_time

    # Custom triggers
    # if "hate" in message.content or "strongly dislike" in message.content:
    #     await message.channel.send("Positivity, " + message.author.name + "! POSITIVITY!!! :star_struck::partying_face::hugging::sparkles:",delete_after=5)

    # Work with Return After Long Break Flags
    # - Chris
    # if message.author.name == chris:
    #     if (datetime.datetime.now() - chris_flag_time).total_seconds() > 259200:
    #         await message.channel.send(random.choice(chris_returning_messages))
    #     chris_flag_time = datetime.datetime.now()
    #
    # # - Emil
    # if message.author.name == emil:
    #     if (datetime.datetime.now() - emil_flag_time).total_seconds() > 259200:
    #         await message.channel.send(random.choice(emil_returning_messages))
    #     emil_flag_time = datetime.datetime.now()
    #
    # # - Magg
    # if message.author.name == magg:
    #     if (datetime.datetime.now() - magg_flag_time).total_seconds() > 259200:
    #         await message.channel.send(random.choice(magg_returning_messages))
    #     magg_flag_time = datetime.datetime.now()

    # Custom Response
    rng_num = random.randint(1, 45)  # Chance for random - 1/45

    if rng_num == 2:
        rng_num_two = random.randint(1, 3)  # Chance for custom response - 1/3

        if rng_num_two == 2:
            if message.author.name == ajay:
                await message.channel.send(random.choice(ajay_responses))
            if message.author.name == jade:
                await message.channel.send(random.choice(jade_responses))
            if message.author.name == chris:
                await message.channel.send(random.choice(chris_responses))
            if message.author.name == haip:
                await message.channel.send(random.choice(haip_responses))
            if message.author.name == emil:
                await message.channel.send(random.choice(emil_responses))
        else:
            await message.channel.send(random.choice(responses_for_all))

    await client.process_commands(message)


client.run('NzM3NDc1ODQxNzAwNzkwNDAy.Xx955g.6sHjKxxhb5g-CPXNSbGT_K8Ab-M')

