project pkg {
    arches = ["x86_64"]
    rpm {
        spec = "stardust-telescope.spec"
    }
    labels {
        nightly = 1
    }
}
