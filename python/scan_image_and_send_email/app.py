#!/usr/bin/env python3

import aws_cdk as cdk

from scan_image_and_send_email.scan_image_and_send_email_stack import ScanImageAndSendEmailStack


app = cdk.App()
ScanImageAndSendEmailStack(app, "scan-image-and-send-email")

app.synth()
