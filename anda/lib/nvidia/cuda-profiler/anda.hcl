project pkg {
   arches = ["x86_64", "aarch64", "i386"]
    rpm {
        spec = "cuda-profiler.spec"
        mock = 1
    }
}
