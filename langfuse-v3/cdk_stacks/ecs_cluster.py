#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# vim: tabstop=2 shiftwidth=2 softtabstop=2 expandtab

import aws_cdk as cdk

from aws_cdk import (
  Stack,
  aws_ecs
)

from constructs import Construct


class ECSClusterStack(Stack):

  def __init__(self, scope: Construct, construct_id: str, vpc, service_discovery_namespace, **kwargs) -> None:

    super().__init__(scope, construct_id, **kwargs)

    cluster_name = self.node.try_get_context('ecs_cluster_name') or "langfuse"
    self.ecs_cluster = aws_ecs.Cluster(self, "ECSCluster",
      cluster_name=cluster_name,
      vpc=vpc
    )
    cdk.Tags.of(self.ecs_cluster).add('Name', 'langfuse')


    cdk.CfnOutput(self, 'ClusterName',
      value=self.ecs_cluster.cluster_name,
      export_name=f'{self.stack_name}-ClusterName')
    cdk.CfnOutput(self, 'ClusterArn',
      value=self.ecs_cluster.cluster_arn,
      export_name=f'{self.stack_name}-ClusterArn')
