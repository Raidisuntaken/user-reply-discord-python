# user-reply-discord-python


#example 1
@client.command()
async def yourcommand(ctx):
 await ctx.send('➤ your messages')

#example 2
@client.command()
async def hello(ctx):
 await ctx.send (f"➤ HELLO, {ctx.author.name}")

 
 
 #with startwith event
 @client.event
async def on_message(ctx):
    await client.process_commands(ctx)
    if ctx.content == 'hello':
        await ctx.channel.send(f'➤ Hello, {ctx.author.name}')
     
     
   #use elif new command
