#!/usr/bin/env python3
import os

import aws_cdk as cdk

from wordpress.wordpress_stack import WordpressStack

my_account = "606417009885"
my_region = "ap-northeast-1"

envJP = cdk.Environment(account=my_account, region=my_region)


app = cdk.App()
WordpressStack(app, "WordpressStack",env=envJP)

app.synth()
