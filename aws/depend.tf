resource "aws_instance" "web" {
  ami               = "ami-21f78e11"
  availability_zone = "us-west-2a"
  instance_type     = "t2.micro"

  tags = {
    Name = "HelloWorld"
  }
}

resource "aws_volume_attachment" "ok_attachment1" {
  device_name = "/dev/sdh3"
  volume_id   = aws_ebs_volume.ok_ebs2.id
  instance_id = aws_instance.web.id
}


resource "aws_ebs_volume" "ok_ebs2" {
  availability_zone = ""
  encrypted = true
}

 resource "aws_cloudtrail" "good_example" {
   is_multi_region_trail = true
   s3_bucket_name = "abcdefgh"
 
   event_selector {
     read_write_type           = "All"
     include_management_events = true
 
     data_resource {
       type = "AWS::S3::Object"
       values = ["${data.aws_s3_bucket.important-bucket.arn}/"]
     }
   }
 }

resource "aws_vpc" "ok_vpc" {
  cidr_block = "10.0.0.0/16"
}
