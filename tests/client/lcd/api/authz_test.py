from cyber_sdk.client.lcd import LCDClient, PaginationOptions

bostrom = LCDClient(
    url="https://lcd.space-pussy-1.cybernode.ai/",
    chain_id="space-pussy-1",
)


def test_grants():
    result = bostrom.authz.grants(
        "bostrom1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
        "bostrom17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp",
    )
    assert len(result) == 0
