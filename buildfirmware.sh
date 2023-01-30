#!/bin/bash

dir_zmk="/Users/siddhant/Documents/Misc/Keyboard/ZMK/zmk/app"
dir_config="/Users/siddhant/Documents/Misc/Keyboard/ZMK/zmk-config/config"

cd $dir_zmk

west build -p -d build/reset -b nice_nano_v2 -- -DZMK_CONFIG=$dir_config -DSHIELD="settings_reset"
west build -p -d build/left -b nice_nano_v2 -- -DZMK_CONFIG=$dir_config -DSHIELD="cradio_left"
west build -p -d build/right -b nice_nano_v2 -- -DZMK_CONFIG=$dir_config -DSHIELD="cradio_right"


cp build/reset/zephyr/zmk.uf2 /Users/siddhant/Downloads/keyboardfirmware/reset.uf2
cp build/left/zephyr/zmk.uf2 /Users/siddhant/Downloads/keyboardfirmware/left.uf2
cp build/right/zephyr/zmk.uf2 /Users/siddhant/Downloads/keyboardfirmware/right.uf2