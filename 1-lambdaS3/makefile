all: prepare deploy

prepare:
	@mkdir src
	@echo "Uploaded file to targetbucket-lmdeguia!" > test.txt
	@zip src/deploy.zip s3Function.py test.txt
	@echo "Reading from s3lambda-lmdeguia!" > src/readme.txt
	@aws s3 sync src s3://s3lambda-lmdeguia

deploy:
	@aws cloudformation create-stack --stack-name testTemplate --template-body file://CFT.yaml --capabilities CAPABILITY_IAM

test:
	@aws lambda invoke --function-name testCFTLambdaFunction --cli-binary-format raw-in-base64-out --payload '{"key":"value"}' out.txt
	@cat out.txt
	@rm out.txt

clean:
	@aws s3 rm s3://targetbucket-lmdeguia/test.txt
	@aws cloudformation delete-stack --stack-name testTemplate
	@rm src/* test.txt
	@rm -d src
	@aws s3 rm s3://s3lambda-lmdeguia --recursive

view:
	@aws cloudformation describe-stacks --stack-name testTemplate
	@aws s3 ls s3://s3lambda-lmdeguia

#aws lambda invoke --function-name testCFTLambdaFunction --cli-binary-format raw-in-base64-out --payload '{"key":"value"}' out.txt
# aws cloudformation describe-stacks --stack-name testTemplate
# SYNC TIME FOR AWS: sudo ntpdate -u in.pool.ntp.org 