from aws_cdk import (
    # Duration,
    Stack,
    aws_dynamodb as ddb,
    aws_lambda,
    CfnOutput,
    # aws_sqs as sqs,
)
from constructs import Construct

class BotayInfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create DDB table
        table = ddb.Table(self, "Tasks",
            partition_key=ddb.Attribute(name='task_id', type=ddb.AttributeType.STRING),
            billing_mode=ddb.BillingMode.PAY_PER_REQUEST,
            time_to_live_attribute='tt1'
        )

        # Add Global Secondary Index based on user_id
        table.add_global_secondary_index(
            index_name='user-index',
            partition_key=ddb.Attribute(name='user_id', type=ddb.AttributeType.STRING),
            sort_key=ddb.Attribute(name='created_time', type=ddb.AttributeType.NUMBER)
        )

        # Create lambda function for the API
        api = aws_lambda.Function(self, "API",
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            code=aws_lambda.Code.from_asset('../lambda_function.zip'),  # Load lambda from a local disk
            handler='app.botay.handler',
            environment={'TABLE_NAME': table.table_name}
        )

        # Create an URL so we can access the function
        function_url = api.add_function_url(
            auth_type=aws_lambda.FunctionUrlAuthType.NONE,
            cors=aws_lambda.FunctionUrlCorsOptions(
                allowed_origins=['*'],
                allowed_methods=[aws_lambda.HttpMethod.ALL],
                allowed_headers=['*']
            )
        )

        # Output the API function URL
        CfnOutput(self, "APIUrl",
            value=function_url.url,    
        )

        # Give lambda permission to read/write to the table
        table.grant_read_write_data(api)
