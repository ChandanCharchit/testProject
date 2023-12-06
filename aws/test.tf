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

resource "aws_s3_bucket" "good_example" {
	bucket = "abcdefgh"
	acl = "private"
}

resource "aws_cloudtrail" "foobar" {
  name                          = "tf-trail-foobar"
  s3_bucket_name                = aws_s3_bucket.foo.id
  s3_key_prefix                 = "prefix"
  include_global_service_events = false
+ is_multi_region_trail = true
}

resource "aws_flow_log" "example" {
  iam_role_arn    = "arn"
  log_destination = "log"
  traffic_type    = "ALL"
+ vpc_id          = aws_vpc.ok_vpc.id
}
