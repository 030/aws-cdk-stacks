import { Stack, StackProps } from "aws-cdk-lib";
import * as sns from "aws-cdk-lib/aws-sns";
import * as events from "aws-cdk-lib/aws-events";
import * as targets from "aws-cdk-lib/aws-events-targets";
import * as subscriptions from "aws-cdk-lib/aws-sns-subscriptions";
import { Construct } from "constructs";

export class ScanImageAndSendEmailStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const rule = new events.Rule(this, "ScanImageAndSendEmailQueue", {
      eventPattern: {
        source: ["aws.ecr"],
        detailType: ["ECR Image Scan"],
        detail: {
          "finding-severity-counts": {
            HIGH: [
              {
                numeric: [">", 0],
              },
            ],
          },
        },
      },
    });

    const topic = new sns.Topic(this, "ScanImageAndSendEmailTopic", {
      topicName: "holamundo",
    });
    topic.addSubscription(
      new subscriptions.EmailSubscription("holamundo@some-domain.com")
    );

    rule.addTarget(new targets.SnsTopic(topic));
  }
}
