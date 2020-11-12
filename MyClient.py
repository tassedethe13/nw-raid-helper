import random
from discord.ext import commands

TOKEN = 'Nzc2MzUzNDIwMzI3NTE4MjM5.X6zpdw.E8gT02qGq-wWM7N-avmX1rBsniU'
bot = commands.Bot(command_prefix='!')

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)
    
bot.run(TOKEN)
