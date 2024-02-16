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

    # For example:
    # If you discover Alarm 0 quoting TON at 1 ton = 20u, but you believe 1 ton = 25u,
    # then you can directly spend 20u to buy one ton from Alarm 0. For you, this means earning a difference of 5u.
    # Besides arbitraging, you also need to provide a correct quote and offer twice the base asset compared to Alarm 0.
    # Therefore, you need to pay 2 tons and 50U (1 ton = 25u).

    alarm_id = 0  # The ID of the alarm you want to arbitrage. In this case, you want to arbitrage Alarm 0.
    buy_num = 1  # The number of asset you want to buy. In this case, you pay 20u to buy 1 ton.
    new_price = 25  # The price you think is accurate.

    await client.wind(alarm_id, buy_num, new_price)


if __name__ == "__main__":
    asyncio.run(main())
