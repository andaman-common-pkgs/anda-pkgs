project pkg {
    arches = ["x86_64", "aarch64", "i386"]
    rpm {
        spec = "x264-bootstrap.spec"
    }
    labels {
        mock = 1
   }
}