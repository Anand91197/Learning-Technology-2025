

> Install Vault
https://developer.hashicorp.com/vault/install

https://medium.com/@phanindra.sangers/how-to-install-hashicorp-vault-in-amazon-ec2-linux-instance-89d250ef1330

sudo yum install -y yum-utils shadow-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
sudo yum -y install vault

vault -version

Starting as Dev
vault server -dev

Set Env
export VAULT_ADDR='http://127.0.0.1:8200'


>Direct Prod

Creating Configuration File
At Directory for example : mkdir vault-exp , i am creating at /home/ec2-user

Pwd : /home/ec2-user/vault-exp , named the filename as my_vault.hcl 
storage "file" {
path = "/home/ec2-user/vault-exp/vault-data"
}
listener "tcp" {
address = "0.0.0.0:8200"
tls_disable = 1
}
ui = "true" ### for ui to be enabled
#####Path = "/home/ec2-user/vault-data
####path we can provide vault automatically creates the path when we mention the path , we dont need to create the path ##########################################

>start vault server from configuration file
vault server -config my_vault.hcl

Initialize vault

In another terminal of my instance: export VAULT_ADDR="http://127.0.0.1:8200"

vault status

unseal the vault : vault operator init

copy paste atleast 3 unseal keys and provide root token to unseal the vault

Unseal Key 1: RNXdSUrHVM+urgBEpuD8ZIveUqgq6gU15nhB4G/Y59Fn
Unseal Key 2: 6zHcHC2+LMhaFeparaq7P7X/iyeDZz4Ig58HcnTKLu2y
Unseal Key 3: 0GzpofJY3lln2Q1igmAMdaHS3cP1a/+bcK7c8TRRa3gi
Unseal Key 4: fHRyjPg6tOE4+mSl4gFLe9lec5BuoO7M4MjG03x6MnwB
Unseal Key 5: dpp/bJxkcUGw94r9NTDXpBnWuSRsNwpSOhmBKMXjRcf8

Initial Root Token: ****

====Unsealing vault Via GUI

Enable KV Engine

create secret my-secret:- Username:Anand

API path: /v1/kv/data/my-secret
CLI path: -mount="kv" "my-secret"

Detailed steps to enable and configure AppRole authentication in HashiCorp Vault:

GUI: Access > Enable authentication > AppRole

CLI: vault auth enable approle

Create a Policy
vim my-vault-policy.hcl
path "*" {
  capabilities = ["list", "read"]
}

path "secrets/data/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}

path "kv/data/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}


path "secret/data/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}

path "auth/token/create" {
capabilities = ["create", "read", "update", "list"]
}

path "secret/data/my-secret" {
  capabilities = ["read"]
}

path "secret/metadata/*" {
  capabilities = ["read", "list"]
}

# For KV v2 engine mounted at "kv/"
path "kv/data/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}

path "kv/metadata/*" {
  capabilities = ["read", "list"]
}

>Create an AppRole (terraform) and Attach the Policy (my-vault-policy)

vault write auth/approle/role/terraform \
    secret_id_ttl=120m \
    token_num_uses=10 \
    token_ttl=120m \
    token_max_ttl=240m \
    secret_id_num_uses=40 \
    token_policies=my-vault-policy


Fetch the Role ID and Secret ID
vault read auth/approle/role/terraform/role-id

role_id    9fdac0eb-8bb5-5845-0dde-0eb7f3fcb3d9

vault write -f auth/approle/role/terraform/secret-id

8599ae46-96c2-9925-166c-418b415d3320


Upload Policy to vault
vault policy write terraform my-vault-policy.hcl 

===
vault write auth/approle/login \
  role_id="9fdac0eb-8bb5-5845-0dde-0eb7f3fcb3d9" \
  secret_id="eba90c44-be39-8436-f4c7-f385cc95efb4"

 ==
 vault write auth/approle/login role_id="9fdac0eb-8bb5-5845-0dde-0eb7f3fcb3d9" secret_id="189046c0-c852-f4ba-2c92-f34dcbc8e36e"

  
| Task                | Command                                                |
| ------------------- | ------------------------------------------------------ |
| Enable AppRole      | `vault auth enable approle`                            |
| Create policy       | `vault policy write my-role-policy my-role-policy.hcl` |
| Create role         | `vault write auth/approle/role/my-role ...`            |
| Get Role ID         | `vault read auth/approle/role/my-role/role-id`         |
| Generate Secret ID  | `vault write -f auth/approle/role/my-role/secret-id`   |
| Login using AppRole | `vault write auth/approle/login ...`                   |



vault secrets list -detailed

vault kv get -mount="kv" "my-secret"


>Enable Secret:
vault secrets enable -path=aws aws

>Policy
vault policy list

vault policy read my-policy

Attach token to policy:

export VAULT_TOKEN= "$(vault token create -field token -policy=my-policy)"

Write Creds:
vault kv put -mount=secret creds password="Anand"

Auth:
vault auth list

Enable AppRole:
vault auth enable approle

Assign Policy with Approle:
vault write auth/approle/role/terraform \
    secret_id_ttl=120m \
    token_num_uses=10 \
    token_ttl=120m \
    token_max_ttl=240m \
    secret_id_num_uses=40 \
    token_policies=my-vault-policy


>export ROLE_ID= "$(vault read -field=role_id auth/approle/role/my-role/role-id)"

>export SECRET_ID= "$(vault write -f -field=secret_id auth/approle/role/my-role/secret-id)"


>vault write auth/approle/login role_id="$ROLE_ID" secret_id= "$SECRET_ID"
