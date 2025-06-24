
# Hosting Langfuse on Amazon ECS Fargate with AWS CDK

This repository contains [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html) code for deploying the [Langfuse](https://langfuse.com/) application using Amazon Elastic Container Registry (ECR) and Amazon Elastic Container Service (ECS).

Langfuse is an open-source LLM engineering platform that helps teams collaboratively debug, analyze, and iterate on their LLM applications.

| Project | Architecture |
|---------|--------------|
| [langfuse-v2](./langfuse-v2/) | ![](./langfuse-v2/langfuse-on-aws-ecs-fargate-arch.svg "Architecture diagram for Langfuse v2 deployment") |
| [langfuse-v3](./langfuse-v3/) | ![](./langfuse-v3/doc/CDK-Langfuse-Architecture.png "Architecture diagram for Langfuse v3 deployment") |

## References

 * [(Official) Self-host Langfuse Guide](https://langfuse.com/self-hosting)
 * [(GitHub) langfuse](https://github.com/langfuse/langfuse/)
 * [(GitHub) langfuse-examples](https://github.com/langfuse/langfuse-examples)
 * [AWS CDK Reference Documentation](https://docs.aws.amazon.com/cdk/api/v2/)

## Security

See [CONTRIBUTING](./CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
