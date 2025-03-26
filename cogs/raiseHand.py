import discord
from discord.ext import commands
from colorama import Fore
import vhconf as c


class RaiseHand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.raised_hand_users = list()
        self.raise_your_hand_message = None
        self.channel = None
        self.is_asking = False

    @commands.command()
    async def h(self, ctx):
        """
        Raises hand
        """
        print(Fore.MAGENTA + "[RAISE HAND] : " + Fore.RESET + "h is called")
        await ctx.message.delete()
        self.is_asking = True
        if c.raised_hand_nick_prefix not in ctx.message.author.display_name:
            # Rename the user
            try:
                display_name = ctx.message.author.display_name
                await ctx.message.author.edit(nick=c.raised_hand_nick_prefix +
                        ctx.message.author.display_name)
                self.raised_hand_users.append(
                    (ctx.message.author, display_name))

            except discord.errors.Forbidden as e:
                print(e)
                print(Fore.RED + "[RAISE HAND] : " + Fore.RESET +
                    "Tried to rename an admin (%s)" % ctx.message.author.display_name)
            await ctx.message.delete()

    @commands.command()
    async def d(self, ctx):
        """
        End the struggle
        """
        if self.is_asking:
            self.is_asking = False
            await ctx.message.delete()
            for r_user in self.raised_hand_users:
                if not r_user[0] == self.bot.user:
                    try:
                        await r_user[0].edit(nick=r_user[1])
                    except discord.errors.Forbidden:
                        print(Fore.RED + "[RAISE HAND] : " + Fore.RESET +
                            "Tried to rename an admin (%s)" % r_user[1])
            self.raised_hand_users = list()
            print(Fore.MAGENTA + "[RAISE HAND] : " + Fore.RESET +
                "everyone has been renamed in server " + Fore.GREEN +
                ctx.message.guild.name + Fore.RESET)


async def setup(bot):
    await bot.add_cog(RaiseHand(bot))
