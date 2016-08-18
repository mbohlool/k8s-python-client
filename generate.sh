rm -rf client/*
rm -rf document/*
swagger-codegen generate -c config.json -i swagger.json -o client/ -l python
swagger-codegen generate -c config.json -i swagger.json -o document/ -l html

