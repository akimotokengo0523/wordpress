from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct

class WordpressStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        ###############################################
        ############### Network Section ###############
        ###############################################
        # VPC & Subnet
        wp_vpc = ec2.Vpc(self, "Vpc",
            vpc_name="wp-dev-vpc",
            cidr="10.0.0.0/16",
            max_azs=1,
            nat_gateways=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="wp-dev-public",
                    cidr_mask=24,
                    subnet_type=ec2.SubnetType.PUBLIC
                ),
                ec2.SubnetConfiguration(
                    name="wp-dev-private-with-nat",
                    cidr_mask=24,
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT
                ),
                ec2.SubnetConfiguration(
                    name="wp-dev-private-isolated",
                    cidr_mask=24,
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
                )
            ]
        )

        ######################################################
        ############### Security Group Section ###############
        ######################################################

        # Security Group(EC2)
        wp_sg_ec2 = ec2.SecurityGroup(self, "SgEC2",
            vpc=wp_vpc,
            security_group_name="wp-dev-sg-ec2",
            description="Security Group for EC2",
            allow_all_outbound=True
        )
        # Security Group(Endpoint)
        wp_sg_endpoing = ec2.SecurityGroup(self, "SgEndpont",
            vpc=wp_vpc,
            security_group_name="wp-dev-sg-endpoint",
            description="Security Group for Endpoint",
            allow_all_outbound=True
        )
