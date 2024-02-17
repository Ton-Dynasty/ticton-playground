from pytoncenter import AsyncTonCenterClientV3
from pytoncenter.v3.models import *
from pytoncenter.utils import format_trace, create_address_mapping
from pytoncenter.extension.message import JettonMessage
from pytoncenter.address import Address
from tonpy import CellSlice
import asyncio


async def wait_tick_success(client: AsyncTonCenterClientV3, msg_hash: str, user_address: str):
    map = {
        Address(user_address): "Your Wallet",
        Address("kQBXgF5mlp3AY7eg1jc6gsWbpCdkzs8EvfkLR3mzIZ2xT1Ys"): "Oracle (TON/USDT)",
        Address("kQBdt8NeOWfqcFwKhckX--6JuuTr4O8MhEicaKHeJ5Qyfpzt"): "Oracle Jetton Wallet (USDT)",
    }
    while True:
        txs = await client.get_transaction_by_message(GetTransactionByMessageRequest(direction="in", msg_hash=msg_hash))
        for i in range(5):
            print("Waiting for tick success" + "." * i, end="\r")
            await asyncio.sleep(1)
        if len(txs) == 0:
            continue
        assert len(txs) == 1
        print("Analyzing transaction...")
        trace = await client.get_trace_alternative(GetTransactionTraceRequest(hash=txs[0].hash))
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
