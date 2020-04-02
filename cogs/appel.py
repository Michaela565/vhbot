import discord 
from discord.ext import commands 
from colorama import Fore 
import rmh_constants
from asyncio import sleep
import rmh_constants


class Appel(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.nicknames = list()  
        self.raise_your_hand_message = None 
        self.raised_hand_user = list()
        self.state = False
        self.listeEleve = list()

    @commands.command()
    async def appel(self,ctx):
        """ : Make a list of people in the server that did not press the button """ 
        print(Fore.CYAN + "[APPEL] : " + Fore.RESET + "starting appel") 
        self.listeEleve = ctx.message.guild.get_role(rmh_constants.eleve_role).members
        self.raise_your_hand_message = await ctx.send(rmh_constants.raise_your_hand_text)
        await self.raise_your_hand_message.add_reaction(rmh_constants.raised_hand_emoji)
        await ctx.message.add_reaction("👍")
        for eleve in ctx.message.author.voice.channel :
            self.nicknames.append(user.display_name)
            print(Fore.CYAN + "[APPEL] : " + Fore.RESET + user.display_name + Fore.GREEN + " is here" + Fore.RESET)
        for k in range (0, len(self.listeEleve)):
            if self.listeEleve[k].nick != None :
                self.listeEleve[k] = self.listeEleve[k].nick
            else :
                self.listeEleve[k] = self.listeEleve[k].name
        messageListe = "  -" + "\n  -".join(list(set([*self.listeEleve]) - set([*self.nicknames])))
        if messageListe == "": await ctx.send("Tout le monde est présent ! Pas de gateau pour Ryan aujourd'hui !")
        else :
            await ctx.send("Les patissiers de la semaine prochaine sont : \n" + messageListe)
        self.nicknames = list()
        self.raised_hand_user = list()
        

def setup(bot):
    bot.add_cog(Appel(bot))
