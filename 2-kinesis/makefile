NAME=TestStream

# 1. create kinesis stream using cloud formation
# 2. create and delete stream using CLI
# 3. make kinesis producer and consumer

time_sync:
	@sudo ntpdate -u in.pool.ntp.org 

deploy_template_resources:
	@aws cloudformation create-stack --stack-name testTemplate --template-body file://CFT.yaml --capabilities CAPABILITY_IAM
remove_template_resources:
	@aws cloudformation delete-stack --stack-name testTemplate


create_stream:
	@aws kinesis create-stream --stream-name $(NAME)
delete_stream:
	@aws kinesis delete-stream --stream-name $(NAME)
view_stream:
	@aws kinesis describe-stream-summary --stream-name $(NAME)



