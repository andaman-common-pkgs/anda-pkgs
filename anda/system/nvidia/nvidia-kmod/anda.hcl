project "pkg" {
    rpm {
        spec = "nvidia-kmod.spec"
    }
    labels {
        mock = 1
    }
}