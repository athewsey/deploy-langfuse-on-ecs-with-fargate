#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# vim: tabstop=2 shiftwidth=2 softtabstop=2 expandtab

from aws_cdk import (
  Stack,
  aws_secretsmanager as secretsmanager,
)
from constructs import Construct


class SecretsStack(Stack):
  """CloudFormation stack managing Secrets Manager Secrets for Langfuse
  
  For details see: https://langfuse.com/self-hosting/configuration
  """
  encryption_key_secret: secretsmanager.ISecret
  nextauth_secret: secretsmanager.ISecret
  salt_secret: secretsmanager.ISecret

  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    self.encryption_key_secret = secretsmanager.Secret(self, "EncryptionKeySecret",
      description=(
        "Langfuse ENCRYPTION_KEY (Used to encrypt sensitive data. Must be 256 bits, 64 string "
        "characters in hex format)"
      ),
      generate_secret_string=secretsmanager.SecretStringGenerator(
        exclude_characters="ghijklmnopqrstuvxyz",
        exclude_punctuation=True,
        exclude_uppercase=True,
        include_space=False,
        password_length=64,
      ),
    )
    self.nextauth_secret = secretsmanager.Secret(self, "NextAuthSecret",
      description="Langfuse NEXTAUTH_SECRET (Used to encrypt login session cookies)",
      generate_secret_string=secretsmanager.SecretStringGenerator(
        exclude_punctuation=True,
        include_space=False,
        password_length=50,
      ),
    )
    self.salt_secret = secretsmanager.Secret(self, "SaltSecret",
      description="Langfuse SALT (Used to salt hashed API keys)",
      generate_secret_string=secretsmanager.SecretStringGenerator(
        exclude_punctuation=True,
        include_space=False,
        password_length=50,
      ),
    )
