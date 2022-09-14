from aws_cdk import Stack
from aws_cdk import aws_events as events
from aws_cdk import aws_events_targets as targets
from aws_cdk import aws_sns as sns
from aws_cdk import aws_sns_subscriptions as subscriptions
from constructs import Construct


class ScanImageAndSendEmailStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        rule = events.Rule(self, "rule",
                           event_pattern=events.EventPattern(
                               source=["aws.ecr"],
                               detail_type=["ECR Image Scan"],
                               detail={
                                   "finding-severity-counts": {
                                       "HIGH": [{
                                           "numeric": [">", 0]
                                       }]
                                   }
                               }
                           )
                           )
        topic = sns.Topic(self, "topic",
                          topic_name="holamundo")
        topic.add_subscription(subscriptions.EmailSubscription(
            email_address="holamundo@some-domain.com"))
        rule.add_target(targets.SnsTopic(topic=topic))
