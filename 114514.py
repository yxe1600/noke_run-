from mcdreforged.api.all import *

PLUGIN_METADATA = {
    'id': 'nuke_launcher',
    'version': '1.0.0',
    'name': 'Nuke Launcher',
    'description': 'Launch a nuke by admin',
    'author': 'ChatGPT',
    'link': 'https://github.com/ChatGPT/nuke_launcher'
}

COMMAND_TRIGGER = '!!核弹启动!!'
TNT_AMOUNT = 114514
DELAY_SECONDS = 3

def explode_tnt(server: PluginServerInterface, player: str):
    for _ in range(TNT_AMOUNT):
        server.execute(f'execute at {player} run summon minecraft:tnt ~ ~ ~ {{"Fuse":{DELAY_SECONDS * 20}}}')

@new_thread('explode_tnt')
def handle_command(server: PluginServerInterface, source: CommandSource):
    if source.is_player and source.has_permission(level=2):  # level=2 corresponds to admin
        explode_tnt(server, source.player)

def on_load(server: PluginServerInterface, old_module):
    server.register_help_message(COMMAND_TRIGGER, 'Launch a nuke by admin')
    server.register_command(
        Literal(COMMAND_TRIGGER).runs(lambda src: handle_command(server, src))
    )
