import aws_cdk as core
import aws_cdk.assertions as assertions
from scan_image_and_send_email.scan_image_and_send_email_stack import ScanImageAndSendEmailStack


def test_sqs_queue_created():
    app = core.App()
    stack = ScanImageAndSendEmailStack(app, "scan-image-and-send-email")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })


def test_sns_topic_created():
    app = core.App()
    stack = ScanImageAndSendEmailStack(app, "scan-image-and-send-email")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)
