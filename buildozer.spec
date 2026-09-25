[app]
title = GOAT AI
package.name = goatai
package.domain = org.goat
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

requirements = python3,kivy,requests,urllib3,certifi,idna,charset-normalizer

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# Targets
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
