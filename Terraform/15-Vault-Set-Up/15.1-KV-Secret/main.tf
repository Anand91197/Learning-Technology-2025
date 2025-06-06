provider "aws" {
  region = "ap-south-1"
}

provider "vault" {
  address = "http://3.7.65.184:8200"
  skip_child_token = true

  auth_login {
    path = "auth/approle/login"

    parameters = {
      role_id   = "9fdac0eb-8bb5-5845-0dde-0eb7f3fcb3d9"
      secret_id = "189046c0-c852-f4ba-2c92-f34dcbc8e36e"
    }

  }
}

data "vault_kv_secret_v2" "example" {
  mount = "kv"
  name  = "my-secret"
}

resource "aws_instance" "my_instance" {
  ami           = "ami-0f535a71b34f2d44a"
  instance_type = "t2.micro"

  tags = {
    Name   = "test"
    Secret = data.vault_kv_secret_v2.example.data["username"]
  }
}
