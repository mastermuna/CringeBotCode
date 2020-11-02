import discord
import random
from discord.ext import commands
import json
import os


client = discord.Client()


@client.event
async def on_ready():

    general_channel = client.get_channel(769272368161619998)

    await general_channel.send('CringeBöt on paikalla taas!')
    print('Botti on valmis')





@client.event
async def on_message(message):
     if message.content == 'teke kutsu':
        general_channel = client.get_channel(769272368161619998)
        await general_channel.send('https://discord.gg/4NPtJ25 @everyone')
     if message.content == 'teke dm':
         
         await message.author.send('Moi, terveisiä CringeBötiltä!')

     if message.content == 'etsi ravintola':
         general_channel = client.get_channel(769272368161619998)
         await general_channel.send('Etsitään lähintä soppajonoa....')
         await general_channel.send('Soppajono löydetty! Tehdään varausta...')
         await general_channel.send('Varaus tehty!')
     if message.content == 'teke apua':
        general_channel = client.get_channel(769272368161619998)
       
        myEmbed = discord.Embed(Title="Apu on tullut!", description="Kaikki CringeBöt komennot!", color=0x00ff00)
        myEmbed.add_field(name='teke kutsu', value='tekee kutsun jonneliittoon.')
        myEmbed.add_field(name='etsi ravintola', value='etsii lähimmän ravintolan johon sinulla on varaa.')
        myEmbed.add_field(name='teke pokemon', value='tekee Pokemon imitaation.')
        myEmbed.add_field(name='teke dm', value='lähettää itselleen dm-viestin.')
        myEmbed.add_field(name='teke versio', value='näyttää botin tämänhetkisen version.')
        myEmbed.add_field(name='teke söpö', value='lähettää söpön kuvan.')
        myEmbed.add_field(name='teke meemu', value='lähettää meemun.')
        myEmbed.add_field(name='teke rickroll', value='tekee rickrollin.')
        myEmbed.add_field(name='teke voltti', value='botti vetää voltin.')
        myEmbed.add_field(name='ala hauku mun aiti', value='ALA HAUKU MUN AITI')
        myEmbed.add_field(name='teke credits', value='näyttää ketkä ovat tehneet botin.')
        myEmbed.add_field(name='teke peppu', value='näkyy jo nimestä.')
        myEmbed.add_field(name='teke mielipide', value='käytetään näin: teke mielipide (serveri)')
        myEmbed.add_field(name='teke kutsu tuva', value='tekee kutsun tuvaan')
        myEmbed.add_field(name='teke riisi',value='tekee töitä riisipellolla.')
        myEmbed.set_author(name='@Maisteri123')
        await general_channel.send(embed=myEmbed)
     if message.content == 'teke pokemon':
        general_channel = client.get_channel(769272368161619998)
        await general_channel.send('öööööhhh Pikachu?')
     if message.content == 'teke versio':
        general_channel = client.get_channel(769272368161619998)
        await general_channel.send('CringeBöt on versiossa 1.4')
     if message.content == 'teke peppu':
         general_channel = client.get_channel(769272368161619998)
         await general_channel.send(file=discord.File('tumblr_lk9ecfes0v1qi3fol.png'))
     if message.content == 'teke meemu':
         general_channel = client.get_channel(769272368161619998)
         await general_channel.send(file=discord.File('sike1.jpg'))
                

     if message.content == 'teke rickroll':
         general_channel = client.get_channel(769272368161619998)
         await general_channel.send('FREE DISCORD NITRO:https://bit.ly/FreeNitroJonne ')
     if message.content == 'teke söpö':
         general_channel = client.get_channel(769272368161619998)
         await general_channel.send(file=discord.File('2222601931.jpg'))
     if message.content == 'ala hauku mun aiti':
         general_channel = client.get_channel(769272368161619998)
         await general_channel.send('Sä kuuntele mun äiti ei o sun kaveri, t u o    s u    v i i m e n e    k e r t a    m a    s a n o    s u l e')
     if message.content == 'teke voltti':
         general_channel = client.get_channel(769272368161619998)
         await general_channel.send('ai mun olkapää!')
     if message.content == 'teke credits':
         general_channel = client.get_channel(769272368161619998)
         await general_channel.send('Botin on tehnyt @Maisteri123#0001')
     if message.content == 'teke mielipide tuva':
         general_channel = client.get_channel(769272368161619998)
         await general_channel.send('Hyvä servu')
     if message.content == 'teke mielipide kontula':
         general_channel = client.get_channel(769272368161619998)
         await general_channel.send('Paska servu')
     if message.content == 'teke mielipide jonne':
         general_channel = client.get_channel(769272368161619998)
         await general_channel.send('Hyvä servu')
     if message.content == 'teke mielipide kaarti':
         general_channel = client.get_channel(769272368161619998)
         await general_channel.send('Hyvä servu')
     if message.content == 'teke kutsu tuva':
         general_channel = client.get_channel(769272368161619998)
         await general_channel.send('https://discord.gg/c7YcBEW')
     if message.content == 'teke riisi':
         general_channel = client.get_channel(769272368161619998)
         await general_channel.send('mina olla riisifurmeri kiinasta')



@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('teke apua'))


client.run('NzY5MjgwMjIzNzk4NzU1MzM4.X5MuCQ.zz8uxUW4LScOh2pgTUOo9G_d04Y')
