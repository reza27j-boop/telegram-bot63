from telethon import TelegramClient, events
from datetime import datetime

api_id = 30068618
api_hash = "44ecce7850da2ab799316e957db6b9b5"

client = TelegramClient("session", api_id, api_hash)

target = "@Mohamdbg"


keywords = [
    "تراست",
    "ولت",
    "والت",
    "کیف پول",
    "انتقال",
    "راهنمای",
    "نیومده",
    "تون کیپر",
    "سیف پال",
    "سیف‌پال",
    "متامسک",
    "خطا",
    "ارور",
    "سواپ",

    # کلمات جدید
    "صرافی ایرانی",
    "صرافی خارجی",
    "صرافی",
    "ترید",
    "تریدر",
    "اتمیک",
    "اتمیک ولت",
    "atomic",
    "exchange",
    "بایننس",
    "کوکوین",
    "کوینکس",
    "برداشت",
    "واریز",
    "شارژ",
    "شبکه",
    "کارمزد",
    "بلاکچین",
    "رمزارز",
    "ارز دیجیتال",
    "کریپتو",
    "توکن",
    "استیک",
    "فریز"
]


@client.on(events.NewMessage)
async def monitor(event):

    if not event.is_group:
        return

    text = event.raw_text.lower()

    if not text:
        return

    if any(word.lower() in text for word in keywords):

        sender = await event.get_sender()
        chat = await event.get_chat()

        if sender:
            name = (
                f"{getattr(sender, 'first_name', '') or ''} "
                f"{getattr(sender, 'last_name', '') or ''}"
            ).strip()

            username = getattr(sender, "username", None) or "ندارد"
            user_id = getattr(sender, "id", "ندارد")

        else:
            name = "نامشخص"
            username = "ندارد"
            user_id = "ندارد"


        info = f"""
🔔 پیام دارای کلمه کلیدی

👤 کاربر:
{name}

🆔 یوزرنیم:
@{username}

🔢 آیدی:
{user_id}

👥 گروه:
{getattr(chat, 'title', 'نامشخص')}

🕒 زمان:
{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""


        await client.send_message(target, info)

        await client.forward_messages(
            target,
            event.message
        )

        print("پیام ارسال شد")


client.start()

print("مانیتور فعال شد")

client.run_until_disconnected()
