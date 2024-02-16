import asyncio
from ticton import TicTonAsyncClient


async def main():
    client = await TicTonAsyncClient.init(
        mnemonics="word1 word2 word3 ... wordN",
        wallet_version="v4r2",
        oracle_addr="EQBENmfrJP6KwfBBtcHaixDHYCnBcD3QGBJ6NJtY3dwXI0go",
        toncenter_api_key="your_api_key",
        threshold_price=0.7,
    )

    # Step1: Tick (Quoting the TON/USDT Price)
    # Checking the Current TON/USDT Price and fill the price in the tick method
    price = 2.5
    await client.tick(price)

    # Go to check ring.py for the next steps.


if __name__ == "__main__":
    asyncio.run(main())
