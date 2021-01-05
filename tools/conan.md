# Conan

## General 

- Dependency and build manager for C/C++.
- Works for all platforms and build systems.
- Developed by JFrog, free and open source.
- Client/server model with different servers:
  - public ConanCenter repo
  - local artifactory server
  - local conan_server

## Principle

- Packages contain pre-built binaries for multiple platforms and/or configurations.
  Pre-built binaries reduce total build time.
  Reproducability and tracability are preserved.
- They are described by a `conanfile.py` recipe.

## Setup

- Install client with pip: `pip install conan` 

## Usage

### Using packages

Search for package:

```sh
$ conan search poco --remote=conan-center
```

Show metadata:
```sh
$ conan inspect poco/1.9.4
```

You can install dependencies explicitly:
```sh
$ conan install poco/1.9.4@
```

It is recommended to specify dependencies in a `conanfile.txt`:

```txt
[requires]
poco/1.9.4
openssl/1.0.2u
```

There you can also specify the generators (like cmake)
and the options (like static vs dynamic).

Install the depenencies from a conanfile:

```sh
$ mkdir build && cd build
$ conan install ..
```

> The conanfile.txt can always be replaced by a conanfile.py
> without build step.

Finally include the generated file in your `CMakeLists.txt`:

```cmake
cmake_minimum_required(VERSION 2.8.12)
project(MD5Encrypter)

add_definitions("-std=c++11")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(md5 md5.cpp)
target_link_libraries(md5 ${CONAN_LIBS})
```

and build the project:

```sh
$ cmake .. -G "Visual Studio 16"
$ cmake --build . --config Release
```


### Creating packages
