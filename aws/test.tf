resource "aws_s3_bucket" "example" {
 server_side_encryption_configuration {
   rule {
       apply_server_side_encryption_by_default {
       sse_algorithm = "AES256"
       }
   }
   }
 metadata_options {
       http_endpoint = "desabled"
       http_tokens   = "required"
  }
}
