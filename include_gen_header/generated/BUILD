package(default_visibility = ["//visibility:public"])

genrule(
    name = "gen",
    tools = ["gen.py"],
    outs = ["header.h"],
    cmd = "python $(location gen.py) $@"
)

cc_library(
    name = "include",
    hdrs = ["header.h"],
    strip_include_prefix = "",
    include_prefix = "",
    
)
