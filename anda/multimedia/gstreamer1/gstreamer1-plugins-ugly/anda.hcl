project pkg {
  arches = ["x86_64", "aarch64", "i386"]
  rpm {
    spec = "gstreamer1-plugins-ugly.spec"
  }
  labels {
        subrepo = "extras"
        mock = 1
    }
}
