from ticton import TicTonAsyncClient
import asyncio
import logging
from dotenv import load_dotenv
import sys
import os

load_dotenv()
mnemonics = os.getenv("WALLET_MNEMONICS")
toncenter_api_key = os.getenv("TONCENTER_API_KEY")
LOGGER = logging.getLogger(__name__)


async def tick(client: TicTonAsyncClient, price: float):
    txhash = await client.tick(price)
    print(txhash)


async def ring(client: TicTonAsyncClient, alarm_id: int):
    txhash = await client.ring(alarm_id)
    print(txhash)


async def wind(client: TicTonAsyncClient, alarm_id: int, buy_num: int, price: float):
    txhash = await client.wind(alarm_id, buy_num, price)
    print(txhash)


async def main():
    print("Please choose the function you want to execute: ")
    print("1. tick")
    print("2. ring")
    print("3. wind")
    choice = int(input("Enter your choice (1/2/3): "))

    client = await TicTonAsyncClient.init(
        mnemonics=mnemonics,
        toncenter_api_key=toncenter_api_key,
        oracle_addr="kQBXgF5mlp3AY7eg1jc6gsWbpCdkzs8EvfkLR3mzIZ2xT1Ys",
        testnet=True,
        logger=LOGGER,
    )

    if choice == 1:
        price = float(input("Enter the price: "))
        await tick(client, price)
    elif choice == 2:
        alarm_id = int(input("Enter the alarm id: "))
        await ring(client, alarm_id)
    elif choice == 3:
        options = f"latest: {client.metadata.total_alarms-1}"
        alarm_id = int(input(f"Enter the alarm id ({options}): "))
        print("Loading alarm metadata...")
        alarm_addr = await client.get_alarm_address(alarm_id)
        alarm_state = await client.get_address_state(alarm_addr)
        if alarm_state != "active":
            sys.stdout.write("\033[F")
            print("Sorry, the alarm is not active, you can't wind it.")
            return
        alarm_metadata = await client.get_alarm_metadata(alarm_addr)
        remain_scale = alarm_metadata.remain_scale
        decimal_ratio = 10 ** (
            client.metadata.base_asset_decimals - client.metadata.quote_asset_decimals
        )
        old_price = alarm_metadata.base_asset_price * decimal_ratio / 2**64
        sys.stdout.write("\033[F")
        if remain_scale == 0:
            print("Sorry, the alarm remains 0 scale, you can't buy it.")
            return
        rng = "max: 1" if remain_scale == 1 else f"1~{remain_scale}"
        buy_num = int(input(f"Enter the buy num ({rng}): "))
        price = float(input(f"Enter the price (alarm price: {old_price}): "))
        await wind(client, alarm_id, buy_num, price)
    else:
        print("Invalid choice")


if __name__ == "__main__":
    asyncio.run(main())
