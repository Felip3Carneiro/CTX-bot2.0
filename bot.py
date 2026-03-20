#Feito por Felipe Carneiro
import discord
from discord.ext import commands
import defs

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f"Eu sou {bot.user}| ID {bot.user.id}")

@bot.command()
async def ajuda(ctx):
    embed = discord.Embed(title="Comandos disponíveis", description="Aqui estão os comandos que você pode usar:", color=discord.Color.green())
    embed.add_field(name="-x-", value="", inline=False)
    embed.add_field(name="!add <número1> <número2>", value="Soma dois números", inline=False)#inline -> não segue o que veio antes dele(pula de linha)
    embed.add_field(name="!sub <número1> <número2>", value="Subtrai dois números", inline=False)
    embed.add_field(name="!mult <número1> <número2>", value="Multiplica dois números", inline=False)
    embed.add_field(name="!div <número1> <número2>", value="Divide dois números", inline=False)
    embed.add_field(name="-x-", value="", inline=False)
    embed.add_field(name="!pato", value="Manda um pato aleatório", inline=False)
    embed.add_field(name="!animal", value="Manda um animal aleatório", inline=False)
    embed.add_field(name="!meme", value="Manda um meme aleatório", inline=False)
    embed.add_field(name="!acc <@nome>", value="Mostra a data em que o nome entrou no servidor", inline=False)
    embed.add_field(name="!pokemon <nome ou id>", value="Mostra informações sobre um Pokémon", inline=False)
    embed.add_field(name="!clima <cidade>", value="Mostra o clima atual de uma cidade", inline=False)
    await ctx.send(embed=embed) # dessa forma ficou muito mais bonita

#-x-x-x-x-x-x-x-x-
#Símbolos matemáticos
@bot.command()
async def add(ctx, left: int, right: int):
    result = left + right
    await ctx.send(f"resultado de {left} + {right} = {result}")

@bot.command()
async def sub(ctx, left:int, right:int):
    result = left - right
    await ctx.send(f"resultado de {left} - {right} = {result}")

@bot.command()
async def mult(ctx, left:int, right:int):
    result = left * right
    await ctx.send(f"resultado de {left} X {right} = {result}")

@bot.command()
async def div(ctx, left:int, right:int):
    result = left / right
    await ctx.send(f"resultado de {left} / {right} = {result}")
#-x-x-x-x-x-x-x-x-
#API
@bot.command()
async def pokemon(ctx, pokemon:str):
    data = defs.poke(pokemon)
    if data:
        embed = discord.Embed(title=f"{data['name'].title()} (ID: {data['id']})", color=discord.Color.red())
        embed.set_thumbnail(url=data["imagem"])
        embed.add_field(name="Tipo", value=data['type'].title(), inline=True)
        embed.add_field(name="Habilidade", value=data['ability'].title(), inline=True)
        embed.add_field(name="Altura", value=f"{data['height']} cm", inline=True)
        embed.add_field(name="Peso", value=f"{data['weight']} Kg", inline=True)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Erro nome ou índice")

@bot.command()
async def clima(ctx, *, loc:str):# * - Indica ao programa pegar tudo depois daquele ponto
    data = defs.clima(loc)
    if data:
        embed = discord.Embed(title=f"{data['location'].title()} (país: {data['country']})", color=discord.Color.blue())        
        embed.set_thumbnail(url=data["icon"])
        embed.add_field(name="Temperatura", value=f"{data['temp_c']}°C", inline=True)
        embed.add_field(name="Tempo", value=data["condition"].title(), inline=True)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Erro cidade")

@bot.command()
async def pato(ctx):
    imagem = defs.duck()
    embed = discord.Embed(title=f"Uma imagem de pato para você!")
    embed.set_image(url=imagem["url"])
    await ctx.send(embed=embed)
#-x-x-x-x-x-x-x-x-
#Arquivos e discord
@bot.command()
async def animal(ctx):
    dados = defs.animal()

    file = discord.File(dados["img"], filename=dados["filename"])

    embed = discord.Embed(title=f"Uma foto de {dados['name']}")
    embed.set_image(url=f"attachment://{dados['filename']}")

    await ctx.send(file=file, embed=embed)#Não me pergunte o do porque isso funciona(o discord é meio burrinho e precisa saber que tem que também enviar o file para oficialmente aparecer no embed)

@bot.command()
async def acc(ctx, member: discord.Member):
    await ctx.send(f"{member} entrou em: {discord.utils.format_dt(member.joined_at)}")

@bot.command()
async def meme(ctx):
    with open(defs.meme(), 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)  
#-x-x-x-x-x-x-x-x-
#Tratamento de erros
@div.error #outra estrutura expecífica que nunca saberia sozinho
async def div_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Estrutura errada, use: !div <número1> <número2>")

@mult.error
async def mult_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Estrutura errada, use: !mult <número1> <número2>")

@add.error 
async def add_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Estrutura errada, use: !add <número1> <número2>")

@sub.error
async def sub_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Estrutura errada, use: !sub <número1> <número2>")
#-x-x-x-x-x-x-x-x-

bot.run("---")
