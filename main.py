from discord_webhook import DiscordWebhook
import random

while True:
    nom = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLMNBVCXZ"
    totalgen = 16
    nitro_code = "".join(random.sample(nom,totalgen))
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1085897836186587206/C5qpcoAd1q3xViFJS3CURMsUcKyTf5QqExIgtCmWEu0lqVsU3YwhkjDc3j0SOVlI4p3H', content=f"https://discord.gift/{nitro_code}")
    try:
        response = webhook.execute()
    except:
        continue