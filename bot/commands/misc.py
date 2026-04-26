import discord


def setup(client):
    @client.tree.command(name="help", description="Help command.")
    async def help(content: discord.Interaction):
        myEmbed = discord.Embed(
            title="DietRX",
            description=(
                "**Eat The RITE food**\n\n"
                "Create a profile 👤: </profile:1170722473633919026>\n"
                " Create Diet Plan 🍎: </diet:1170569290072719502>\n"
                " Find RWJ doctors 👨‍⚕️: </finddocs:1170612893314727967>\n"
                " Delete profile ❌: </deleteprofile:1170539459134107660>\n"
                " Point Leaderboard 🏆: </leaderboard:1170619099810889818>"
            ),
            color=0x00ff00,
        )
        await content.response.send_message(embed=myEmbed)

    @client.tree.command(name="leaderboard", description="Points")
    async def leaderboard(content: discord.Interaction):
        myEmbed1 = discord.Embed(
            title="Patzer Bot",
            description=(
                "**Leaderboard**\n"
                "1. Vijay (10 Points) 🥇\n"
                "2. Nandan Gondi (6 Points) 🥈\n"
                "3. Zarah (4 Points) 🥉\n"
                "4. Dhawal Arora (2 Points)"
            ),
            color=0x00ff00,
        )
        await content.response.send_message(embed=myEmbed1, ephemeral=True)
