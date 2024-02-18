from pytoncenter import AsyncTonCenterClientV3
from pytoncenter.v3.models import *
from pytoncenter.utils import format_trace, create_address_mapping
from pytoncenter.extension.message import JettonMessage
from pytoncenter.address import Address
from tonpy import CellSlice
import asyncio
import itertools

DEFAULT_MAP = {
    Address("kQBXgF5mlp3AY7eg1jc6gsWbpCdkzs8EvfkLR3mzIZ2xT1Ys"): "Oracle (TON/USDT)",
    Address("kQBdt8NeOWfqcFwKhckX--6JuuTr4O8MhEicaKHeJ5Qyfpzt"): "Oracle Jetton Wallet (USDT)",
}


async def spinner(msg: str = "Loading..."):
    """Asynchronous spinner function."""
    for frame in itertools.cycle(["-", "\\", "|", "/"]):
        print(f"{msg} {frame}", end="\r", flush=True)
        await asyncio.sleep(0.2)


async def wait_tick_success(client: AsyncTonCenterClientV3, msg_hash: str, user_address: str):
    map = {**DEFAULT_MAP, Address(user_address): "Your Wallet"}
    spinner1 = asyncio.create_task(spinner("Wait for the transaction to be confirmed"))

    try:
        tx = await anext(client.wait_message_exists(WaitMessageExistsRequest(msg_hash=msg_hash)))
    finally:
        spinner1.cancel()
        print()

    spinner2 = asyncio.create_task(spinner("Analyzing transaction"))
    try:
        trace = await client.get_trace_alternative(GetTransactionTraceRequest(hash=tx.hash))
        user_jetton_wallet = Address(trace.children[0].transaction.in_msg.destination)
        map.update({user_jetton_wallet: "Your Jetton Wallet"})
        address_mapping = create_address_mapping(map)
        # Search transaction by opcode 0x09c0fafb
        branches = trace.children[0].children[0]
        for branch in branches.children:
            if branch.transaction.in_msg.opcode == JettonMessage.TransferNotification.OPCODE:
                target_tx = branch.children[0].transaction
                body = target_tx.in_msg.message_content.body
                cs = CellSlice(body)
                _ = cs.load_uint(32)
                alarm_id = cs.load_uint(256)
                map.update({Address(target_tx.in_msg.destination): f"Alarm (ID: {alarm_id})"})
                print()
                print("Transaction Found \033[93m(0x09c0fafb)\033[0m:")
                print(f"\033[93mhttps://testnet.tonviewer.com/transaction/{target_tx.hash}\033[0m")
                print()
                print("🔥Your new alarm is now active!🔥")
                print("Your alarm ID is:", "\033[1m" + str(alarm_id) + "\033[0m")
                print("You can now ring or wind your alarm.")
                print()
                print(format_trace(trace, address_mapping=address_mapping))
                return
    finally:
        spinner2.cancel()


async def wait_ring_success(client: AsyncTonCenterClientV3, msg_hash: str):
    spinner_task = asyncio.create_task(spinner("Wait for the transaction to be confirmed"))
    try:
        tx = await anext(client.wait_message_exists(WaitMessageExistsRequest(msg_hash=msg_hash)))
        print()
        print("Transaction Found \033[93m(0xc3510a29)\033[0m:")
        print(f"\033[93mhttps://testnet.tonviewer.com/transaction/{tx.hash}\033[0m")
        print()
        return
    finally:
        spinner_task.cancel()


async def wait_wind_success(client: AsyncTonCenterClientV3, msg_hash: str):
    spinner_task = asyncio.create_task(spinner("Wait for the transaction to be confirmed"))
    try:
        tx = await anext(client.wait_message_exists(WaitMessageExistsRequest(msg_hash=msg_hash)))
        print()
        print("Analyzing transaction...")
        print("Transaction Found \033[93m(0x9e5d3112)\033[0m:")
        print(f"\033[93mhttps://testnet.tonviewer.com/transaction/{tx.hash}\033[0m")
        print()
        return
    finally:
        spinner_task.cancel()
