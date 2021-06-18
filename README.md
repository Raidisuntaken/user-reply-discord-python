# user-reply-discord-python


#example 1
@client.command()
async def yourcommand(ctx):
 await ctx.send('➤ your messages')

#example 2
@client.command()
async def hello(ctx):
 await ctx.send (f"➤ HELLO, {ctx.author.name}")
