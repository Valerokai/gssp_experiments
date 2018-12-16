from discord.ext import commands

from gssp_experiments.checks import is_owner_or_admin
from gssp_experiments.settings.config import strings, config


class Fun():
    def __init__(self, client):
        self.client = client

    async def ping(self, ctx):
        return ctx.send("Pong!")


def setup(client):
    client.add_cog(Fun(client))
