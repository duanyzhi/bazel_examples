package(default_visibility = ["//visibility:public"])

py_binary(
    name = "test",
    srcs = ["test.py"],
    testonly = 1,
    deps = [":lib"],
)

py_library(
    name = "lib",
    srcs = ["lib.py"],
    testonly = 1,
    data = [":data"],
)

filegroup(
    name = "data",
    testonly = 1,
    srcs = glob(["data/*.txt"]),
)
