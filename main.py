from ticton import TicTonAsyncClient
from tonsdk.crypto import mnemonic_new
from tonsdk.contract.wallet import Wallets, WalletVersionEnum

import asyncio
import logging
from dotenv import load_dotenv
import sys
import os
from helper import wait_tick_success, wait_ring_success, wait_wind_success

load_dotenv()
mnemonics = os.getenv("WALLET_MNEMONICS")
toncenter_api_key = os.getenv("TONCENTER_API_KEY")
LOGGER = logging.getLogger(__name__)


async def init_client() -> TicTonAsyncClient:
    return await TicTonAsyncClient.init(
        mnemonics=mnemonics,
        toncenter_api_key=toncenter_api_key,
        oracle_addr="kQCQPYxpFyFXxISiA_c42wNYrzcGc29NcFHqrupDTlT3a9It",
        testnet=True,
        logger=LOGGER,
    )


async def tick(client: TicTonAsyncClient, price: float):
    sent_msg = await client.tick(price)
    print(sent_msg)
    await wait_tick_success(
        client=client.toncenter,
        msg_hash=sent_msg.message_hash,
        user_address=client.wallet.address.to_string(True, True, True),
    )


async def ring(client: TicTonAsyncClient, alarm_id: int):
    sent_msg = await client.ring(alarm_id)
    print(sent_msg)
    await wait_ring_success(client.toncenter, msg_hash=sent_msg.message_hash)


async def wind(
    client: TicTonAsyncClient,
    alarm_id: int,
    alarm_addr: str,
    buy_num: int,
    price: float,
):
    sent_msg = await client.wind(alarm_id, buy_num, price)
    print(sent_msg)
    await wait_wind_success(
        client.toncenter,
        msg_hash=sent_msg.message_hash,
        alarm_address=alarm_addr,
        alarm_id=alarm_id,
        user_address=client.wallet.address.to_string(True, True, True),
    )


async def main():
    show_prompt = False

    while True:
        client_task = asyncio.create_task(init_client())
        if show_prompt:
            while True:
                choice = input("Would you like to continue? ([Y, any key]/n): ")
                if choice.lower() == "n":
                    return
                break
        show_prompt = True

        print("Please choose the function you want to execute: ")
        print("0. generate new wallet")
        print("1. tick")
        print("2. ring")
        print("3. wind")
        raw_choice = input("Enter your choice (0/1/2/3): ")
        if raw_choice not in {"0", "1", "2", "3"}:
            print("Invalid choice, please try again.")
            continue

        choice = int(raw_choice)
        if choice == 0:
            wallet_mnemonic = mnemonic_new()
            version = WalletVersionEnum.v4r2
            _, _, _, wallet = Wallets.from_mnemonics(wallet_mnemonic, version)
            print("\033[95m===============Wallet Information===============\033[0m")
            print(
                "Wallet Mnemonics: \n",
                "\033[93m" + " ".join(wallet_mnemonic) + "\033[0m",
            )
            print("Wallet Version: \n", "\033[93m" + version + "\033[0m")
            print(
                "Wallet Address: \n",
                "\033[93m" + wallet.address.to_string(True, True, True) + "\033[0m",
            )
            print("\033[95m===============Instructions===============\033[92m")
            print("⭐️ Please keep the wallet mnemonics in a safe place ⭐️")
            print(
                "1. Import the mnemonics to your wallet software. (e.g. Browser Extension, TonKeeper, TonSpace, etc.)"
            )
            print(
                "2. Copy your address and go to https://t.me/testgiver_ton_bot to get some testnet TON."
            )
            print("3. Use the wallet address to receive TON from TestGiver.")
            print("4. Remember to edit `.env` with your new mnemonic\033[0m")
            print("🥳🥳🥳 Done 🥳🥳🥳")
            continue

        if choice == 1:
            client = await client_task
            price = float(input("Enter the price: "))
            await tick(client, price)
            continue
        if choice == 2:
            client = await client_task
            alarm_id = int(input("Enter the alarm id: "))
            await ring(client, alarm_id)
            continue
        if choice == 3:
            client = await client_task
            options = f"latest: {client.metadata.total_alarms-1}"
            alarm_id = int(input(f"Enter the alarm id ({options}): "))
            print("Loading alarm metadata...")
            alarm_addr = await client.get_alarm_address(alarm_id)
            alarm_state = await client.get_address_state(alarm_addr)
            if alarm_state != "active":
                sys.stdout.write("\033[F")
                print("Sorry, the alarm is not active, you can't wind it.")
                continue
            alarm_metadata = await client.get_alarm_metadata(alarm_addr)
            remain_scale = alarm_metadata.remain_scale
            decimal_ratio = 10 ** (
                client.metadata.base_asset_decimals
                - client.metadata.quote_asset_decimals
            )
            old_price = alarm_metadata.base_asset_price * decimal_ratio / 2**64
            sys.stdout.write("\033[F")
            if remain_scale == 0:
                print("Sorry, the alarm remains 0 scale, you can't buy it.")
                continue
            rng = "max: 1" if remain_scale == 1 else f"1~{remain_scale}"
            buy_num = int(input(f"Enter the buy num ({rng}): "))
            if buy_num < 1 or buy_num > remain_scale:
                print("Buy num out of range")
                continue
            price = float(input(f"Enter the price (alarm price: {old_price}): "))
            await wind(client, alarm_id, alarm_addr, buy_num, price)
            continue


if __name__ == "__main__":
    asyncio.run(main())
