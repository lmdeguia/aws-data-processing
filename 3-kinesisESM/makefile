NAME=TestStream

# 1. Create event source mapping to link kinesis stream and lambda function
# 2. write producer python script locally to produce data into kinesis stream
# 3. use lambda function to read data from stream and write data to s3 bucket

time_sync:
	@sudo ntpdate -u in.pool.ntp.org 

prepare:
	@cd lambda && zip deploy.zip s3Function.py
	@aws s3 cp lambda/deploy.zip s3://s3lambda-lmdeguia
	@aws s3 cp lambda/read.txt s3://s3lambda-lmdeguia


deploy_template_resources:
	@aws cloudformation create-stack --stack-name testTemplate --template-body file://CFT.yaml --capabilities CAPABILITY_IAM

remove_template_resources:
	@rm lambda/deploy.zip
	@aws s3 rm s3://s3lambda-lmdeguia --recursive
	@aws cloudformation delete-stack --stack-name testTemplate


create_stream:
	@aws kinesis create-stream --stream-name $(NAME)
delete_stream:
	@aws kinesis delete-stream --stream-name $(NAME)
view_stream:
	@aws kinesis describe-stream-summary --stream-name $(NAME)



