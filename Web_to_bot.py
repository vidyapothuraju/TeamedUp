import asyncio

from Bot import send_massege_from_all_participants

def message_sender(id,sport):
   asyncio.run(send_massege_from_all_participants(id,sport))
