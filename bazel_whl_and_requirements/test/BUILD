load("@rules_python//python:defs.bzl", "py_library", "py_test")
load("@my_deps//:requirements.bzl", "requirement")

py_test(
    name = "test",
    srcs = ["test.py"],
    python_version = "PY3",
    #The name of the source file that is the main entry point of the application
    main = "test.py",
    deps = [
        requirement("numpy"),
        "@pytorch_whl_install//:pkg",
    ]
)
