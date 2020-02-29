import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '?')

@client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Welcoming People'))
    print ('UwU')

@client.event
async def on_member_join(member):
    channel = client.get_channel(682294687234916420)
    welcome = await channel.send(f'Welcome to the server, {member.mention}')
    await welcome.add_reaction("👋")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=["menu"])
async def help(ctx):
        embed = discord.Embed(title="What Information Do You Require?",
                                description="React with 💬 for a list of user commands and 🛑 for a list of moderation commands", color=0xffd500)
        startmsg = await ctx.send(embed=embed)
        await startmsg.add_reaction('💬')
        await startmsg.add_reaction('🛑')
        while True:
            chatemoji = ['💬']
            blockemoji = ['🛑']
            xemoji = ['❌']
            timeout = 120
            reaction, user = await client.wait_for('reaction_add')
            timeout
        if reaction.message.id == startmsg.id and user.client is not True:
            if str(reaction.emoji) in chatemoji:
                await reaction.message.remove_reaction('💬', user)
                await startmsg.add_reaction('❌')
                embed = discord.Embed(
                    title="Help Menu", description="This is a help menu", colour=0xffd500)
                embed.add_field(
                    name="?help", value="Displays this message", inline=False)
                embed.add_field(
                    name="?ping", value="Pings the bot", inline=False)
                embed.add_field(
                    name="?clear", value="Clears messages", inline=False)
                embed.set_footer(text=f"Request by {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
                await startmsg.edit(embed=embed)
                await startmsg.add_reaction('❌')
            if str(reaction.emoji) in blockemoji:
                await reaction.message.remove_reaction('🛑', user)
                await startmsg.add_reaction('❌')
                embed = discord.Embed(
                    title="Help Menu", description="This is a help menu", colour=0xffd500)
                embed.add_field(
                    name="test", value="test", inline=False)
                embed.set_footer(text=f"Request by {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
                await startmsg.edit(embed=embed)
                await startmsg.add_reaction('❌')
            if str(reaction.emoji) in xemoji:
                    await startmsg.remove_reaction('❌', user)
                    await startmsg.delete()

@client.command(aliases=["purge"])
@commands.has_role(682292585439428628)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def martin(ctx):
    channel = client.get_channel(683003298122563640)
    await ctx.channel.send('martin martin AMrtin MArTin')

client.run('NjY1NjExNDE1MzU2NDQwNjA2.XlQGYg.zlntNC3VMqjSS7U00LkT87746rw')

