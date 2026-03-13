import discord
from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {client.user}")

@tree.command(name="help", description="Get help with common issues")
async def help_command(interaction: discord.Interaction):
    select = discord.ui.Select(
        placeholder="Select an issue...",
        options=[
            discord.SelectOption(label="Version Mismatch", value="version_mismatch")
        ]
    )

    async def select_callback(select_interaction: discord.Interaction):
        if select.values[0] == "version_mismatch":
            await select_interaction.response.send_message(
                "## 🔧 Version Mismatch Fix\n"
                "Follow these steps:\n"
                "1. Run the **Roblox Updater**\n"
                "2. Delete everything inside:\n"
                "```\n%localappdata%/Roblox/Versions\n```\n"
                "3. **Reinstall Roblox**",
                ephemeral=True
            )

    select.callback = select_callback

    view = discord.ui.View()
    view.add_item(select)

    await interaction.response.send_message(
        "👋 What do you need help with?",
        view=view,
        ephemeral=True
    )

import os
client.run(os.environ["TOKEN"])