import discord
from discord.ext import commands

# Set up the bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

TOP_CONTENT_CHANNEL_ID = 1329387814118363177  # Replace with the ID of your "top-content" channel

@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}')

@bot.command()
async def highlight(ctx, channel: discord.TextChannel, message_id: int):
    try:
        # Fetch the target message
        target_message = await channel.fetch_message(message_id)

        # Create an embed
        embed = discord.Embed(
            description=target_message.content,
            color=discord.Color.gold()
        )
        embed.set_author(name=target_message.author.display_name, icon_url=target_message.author.avatar.url)

        # Attach images if available
        if target_message.attachments:
            embed.set_image(url=target_message.attachments[0].url)

        # Send the embed to the "top-content" channel
        top_channel = bot.get_channel(TOP_CONTENT_CHANNEL_ID)
        await top_channel.send(embed=embed)
        await ctx.send(f'Message highlighted in {top_channel.mention}.')

    except Exception as e:
        await ctx.send(f'Error: {e}')

import os
bot.run(os.getenv("DISCORD_TOKEN"))

