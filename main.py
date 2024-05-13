import asyncio
from services import google_translate
from settings import CHANNELS, TIME_SLEEP_MIN


# main
async def main():
    print("Начал работу...")
    while True:
        print("Начал поиск новых постов")
        for channel in CHANNELS:
            await google_translate(
                channel
            )

        print("Закончил поиск новых постов")
        print(f"Sleeping for {TIME_SLEEP_MIN} minutes")
        await asyncio.sleep(TIME_SLEEP_MIN * 60)


if __name__ == "__main__":
    asyncio.run(main())
