# version
bazel : 2.0.0



## 1. include_gen_header

对于通过genrule生成的文件，如何在.cc文件中通过#include方式来调用呢？

首先需要在需要include的文件所在的BUILD里通过deps来依赖:

```
cc_binary(
    name = "hello",
    srcs = ["main.cpp"],
    deps = ["//generated:include"],
)
```



然后在generated文件夹中的BUILD里来填写:

```
cc_library(
    name = "include",
    hdrs = ["header.h"],
    strip_include_prefix = "",
    include_prefix = "",
    
)
```

这里的hdrs里面就是main.cpp需要依赖的文件的名字，如果依赖了多个文件，就需要都写在这里。strip_include_prefix和include_prefix是用来控制路径。可以先看下bazel-bin生成路径:

```
├── generated
│   ├── header.h
│   └── _virtual_includes
│       └── include
│           └── header.h -> root/.cache/bazel/_bazel_workspace/9e7b86792c85354f1dcd93ed839b948c/execroot/__main__/bazel-out/k8-fastbuild/bin/generated/header.h
├── hello
...
```

generated下面的header.h是生成的。_virtual_includes下面的内容可以直接在.cc文件中导入。其中include文件夹对应的是cc_library的name，include下面的header.h就是cc_library中的hdrs内容。可以直接在main.cpp函数中直接使用:#include <header.h> ，这里可以用导入系统库的形式<>来导入头文件了。