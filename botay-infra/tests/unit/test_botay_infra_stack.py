import aws_cdk as core
import aws_cdk.assertions as assertions

from botay_infra.botay_infra_stack import BotayInfraStack

# example tests. To run these tests, uncomment this file along with the example
# resource in botay_infra/botay_infra_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = BotayInfraStack(app, "botay-infra")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
