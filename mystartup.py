#!/usr/bin/python
from pubnub import Pubnub

pubnub = Pubnub(
    publish_key = "pub-c-5b4ed4d3-8921-45cb-8151-d48aaebb2467",
    subscribe_key = "sub-c-f7b16a98-a291-11e6-a1b1-0619f8945a4f")


channel = "onboard"
message = "done"
pubnub.publish(
    channel = channel,
    message = "done")