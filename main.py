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

    # Step2: Go to Tonviewer and check your alarm ID.
    # For more details, please check the README.md file.
    alarm_id = 6  # Replace with your alarm ID

    # Step3: Ring (Closing this Quote)
    # When you believe a quote is no longer accurate, you can call Ring to close the quote.
    # If not closed, Timekeepers can arbitrage positions they consider to be mispriced.
    # When calling Ring, if the quote has existed for at least one minute and hasn't been arbitraged by Timekeeper, a reward can be claimed; otherwise, no reward is available.
    # await client.ring(alarm_id)

    # Step4: After the quote is closed, you can go to the Tonviewer to check whether you have received the reward.


if __name__ == "__main__":
    asyncio.run(main())
