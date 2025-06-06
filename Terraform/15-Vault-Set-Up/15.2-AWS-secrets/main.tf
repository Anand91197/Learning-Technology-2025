/*
#vault kv put secret/aws access_key="AKIAXXXXXXXX" secret_key="your-secret-key"
kv = key-value secrets engine.
This saves a key under secret/aws with fields access_key and secret_key.
*/

provider "vault" {
  address = "http://127.0.0.1:8200"
}

data "vault_kv_secret_v2" "aws_creds" {
  mount = "secret"
  name  = "aws"
}

provider "aws" {
  region     = "us-east-1"
  access_key = data.vault_kv_secret_v2.aws_creds.data["access_key"]
  secret_key = data.vault_kv_secret_v2.aws_creds.data["secret_key"]
}
