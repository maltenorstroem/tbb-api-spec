# BFF-API SPEC the-blockchain-bar (TBB)

Furo contains helpful generators, converters, sanitizer for the furo specs. Read more about the single commands in the see also section below.

Calling furo without any arguments and flags will run the flow runner with the default flow. Modify your default flow in the .furo config file to your needs. You can set any of the sub commands as default.


[Furo Documentation](https://furo.pro/)

[Furo Interface Definition Language](https://fidl.furo.pro/)

## Getting started with Application & Library Templates
https://confluence.adcubum.com/pages/viewpage.action?pageId=176692074

## Set Up your Repository
Different steps are necessary to get a running project.

Add the correct module name e.g. git.adcubum.com/aat/adcubum-library-example-bff-spec and paths:
- .furo
- project.properties
- buf.yaml
- add module name to go.mod
- package.json.tmpl

> for a better understanding checkout the BFF API SPEC Example: https://git.adcubum.com/projects/AAT/repos/adcubum-library-example-bff-spec/browse

### Update Go vendor packages
```
go mod vendor
```

### Add a Go module file (go.mod) - if no go.mod file is available
```
go mod init // creates a new module, initializing the go.mod file that describes it.
go mod tidy // removes unused dependencies.
go mod vendor // The go mod vendor command constructs a directory named vendor in the main module's root directory that contains copies of all packages needed to support builds and tests of packages in the main module.
```

Sample go.mod
```gotemplate
module [MODULE e.g. git.adcubum.com/aat/adcubum-library-example-bff-spec]

go 1.15

require (
	...
)
```

## Local Development

### Use local container build
[Furo build environment docker container](https://github.com/theNorstroem/furoBEC)

https://hub.docker.com/r/thenorstroem/furo-bec

```shell script
docker pull thenorstroem/furo-bec:v1.28.5
```

Example Usage: docker run -it --rm -v $(pwd):$pwd/specs thenorstroem/furo-bec:v1.28.5

### Or use your local installation

#### furo
```shell script
brew tap theNorstroem/tap
brew install furo
```

#### Google protobuf compiler
(which is a standalone binary named protoc) needs to be installed somewhere on your $PATH.

##### macOS
If you have Homebrew (which you can get from https://brew.sh), just run:
```shell script
brew install protobuf
```

If you see any error messages, run brew doctor, follow any recommended fixes, and try again. If it still fails, try instead:
```shell script
brew upgrade protobuf
```

Alternately, run the following commands:
```shell script
PROTOC_VERSION=3.17.3 # Jenkins.Dockerfile

PROTOC_ZIP=protoc-$PROTOC_VERSION-osx-x86_64.zip
curl -OL https://github.com/protocolbuffers/protobuf/releases/download/v$PROTOC_VERSION/$PROTOC_ZIP
sudo unzip -o $PROTOC_ZIP -d /usr/local bin/protoc
sudo unzip -o $PROTOC_ZIP -d /usr/local 'include/*'
rm -f $PROTOC_ZIP
```

##### Linux
```shell script
PROTOC_VERSION=3.17.3 # Jenkins.Dockerfile

PROTOC_ZIP=protoc-$PROTOC_VERSION-linux-x86_64.zip
curl -OL https://github.com/protocolbuffers/protobuf/releases/download/v$PROTOC_VERSION/$PROTOC_ZIP
sudo unzip -o $PROTOC_ZIP -d /usr/local bin/protoc
sudo unzip -o $PROTOC_ZIP -d /usr/local 'include/*'
rm -f $PROTOC_ZIP
```

#### GO
- [install GO](https://golang.org/doc/install)

Add /usr/local/go/bin to the PATH environment variable.

## Repository Setup
It is recommended to equip the repository with the Go Module Package System.
- [Using go modules](https://blog.golang.org/using-go-modules)
- [cmd list](https://golang.org/cmd/go/#hdr-Module_maintenance)