
Terraform Workspaces allow you to manage multiple environments (dev, staging, prod) from the same codebase without copying or rewriting your .tf files.

Each workspace has its own state file. So dev, staging, and prod can use the same code but manage separate infrastructure.

Uses terraform.workspace to name/tag/label resources

#Check and Switch Workspaces
terraform workspace list        # Shows available workspaces
terraform workspace show        # Shows current workspace
terraform workspace select dev  # Switch to dev

#Workspaces do NOT isolate resources from each other in AWS — they only isolate Terraform state.

#Steps to Use Workspaces

# Step 1: Initialize Terraform
terraform init

# Step 2: Create a new workspace for dev
terraform workspace new dev

# Step 3: Apply for dev
terraform apply

# Step 4: Create a new workspace for prod
terraform workspace new prod

# Step 5: Apply for prod
terraform apply


#You must destroy the resources in that workspace before deleting it, otherwise Terraform will not allow you to delete it.

terraform workspace delete dev